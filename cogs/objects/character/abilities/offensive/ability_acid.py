'''
Acid ability.

Last update: 14/06/19
'''

# Dependancies

import asyncio

# Object

from cogs.objects.character.abilities.ability import Ability
from cogs.objects.character.abilities_effects.damages_over_time.acid import Acid
from cogs.objects.character.abilities_effects.buff.unity_is_strenght import Unity_is_strenght

# Utils

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.commands.fight.functions.damage_calculator import Damage_calculator
from cogs.utils.functions.commands.fight.displayer.display_move import Display_move

    # Effects
from cogs.utils.functions.commands.fight.functions.effect.has_effect import Has_dot, Has_buff
from cogs.utils.functions.commands.fight.functions.effect.get_effect import Get_dot

class Ability_Acid(Ability):
    '''
    Applies a DOT on the target that deals damage each turn.
    '''

    icon = '<:acid:583953112406949888>'
    id = 1

    def __init__(self):
        Ability.__init__(self)
        # Basic
        self.name = 'Acid'
        self.description = ''
        
        # Config
        self.can_target_ally = False
        self.need_target = True
        self.cost = 8
        self.cooldown = 0
    
    # Method

    async def init(self, client, ctx, caster):
        '''
        `coroutine` 

        Mainly translate the name and the descriptions of the ability.

        `client` : must be `discord.Client` object.

        `ctx` : must be `discord.ext.commands.Context` object.

        `caster` : must be `Character` object of the character who uses the ability.

        Return: void
        '''

        # Init

        _ = await Translate(client, ctx)

        # Translation

        self.name = _('Acid')
        self.description = _('Deals **25 %** of your Ki damage. Applies one stack of **[{}]**{} to the target for **4** turns.\nEach stack of {} inflicts **1 %** *(+{} %)* of the target maximum health as ki damages.\n*Maximum **3** stacks, new stack refresh duration. Once **3** stacks, {} damages are increased by **50** % for its duration.*').format(Acid().name, Acid().icon, Acid().icon, (caster.ki_damage_max/1000)*0.5, Acid().icon)

        return

    async def trigger(self, client, ctx, caster, target, team_a, team_b, move = None, ability = None):
        '''
        `coroutine`

        Apply a stack of acid on the target. If the target already have the dot, reset the timer.

        Return: move
        '''

        # Init

        new_acid = Acid()
        await new_acid.init(client, ctx)
        unity = False  # Check if there is the special buff or not
        caster.flag = 0  # Attack

            # init dot
        new_acid.stack = 1
        new_acid.total_damage = int(((1+((caster.ki_damage_max/1000)*0.5))*target.max_hp)/100)
        new_acid.tick_damage = int((new_acid.total_damage/new_acid.duration))*new_acid.stack

        # Check if the target already has the dot or not

        has_dot = await Has_dot(target, Acid())

        if has_dot:
            # If has dot, we get the dot, add a new stack, change the dmg if needed
            # remove it, then apply the new dot
            new_acid = await Get_dot(target, Acid())
            target.dot.remove(new_acid)  # Remove the old dot to apply a new one

            # If the old acid has less stacks than the maximum, we add a new one

            if(new_acid.stack < new_acid.max_stack):
                
                for character in team_a:
                    has_unity = await Has_buff(character, Unity_is_strenght())
                    if has_unity:
                        unity = True
                    
                    else:
                        pass
                
                if unity:
                    new_acid.stack += 2
                    new_acid.duration = 5
                
                else:
                    new_acid.stack += 1
            
            new_acid.duration = 4  # Reset the duration
            new_acid.tick_damage = int((new_acid.total_damage/new_acid.duration))*new_acid.stack  # Reset the damages

            target.dot.append(new_acid)
        
        else:  # If the target doesn't have the dot
            target.dot.append(new_acid)
        
        # Inflict Ki damages
        damage_done = await Damage_calculator(caster, target, is_ki = True)

        damage_done = int(damage_done*0.25)  # This ability inflicts only 25 % of the Ki damage

        await target.inflict_damage(caster, damage_done, team_a, team_b)

        move += await Display_move(client, ctx, self.name, self.icon, damage_done, caster, target, ki_gain = caster.ki_regen, is_ki = True)
        
        return(move)
'''
Acid ability.

Last update: 26/06/19
'''

# Dependancies

import asyncio
from random import randint

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
        self.can_target_enemy = True
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
        
        await new_acid.set_total_damage(caster, target, team_a, team_b)
        await new_acid.add_stack(caster, target, team_a, team_b)
        await new_acid.set_tick_damage(caster, target, team_a, team_b)
        
        # Inflict Ki damages

        damage = randint(caster.ki_damage_min, caster.ki_damage_max)
        damage_done = await Damage_calculator(caster, damage, target, damage_reduction = target.damage_reduction, is_ki = True, can_crit = True, crit_chance = caster.critical_chance, crit_bonus = caster.critical_bonus)

        damage_done[1] = int(damage_done[1]*0.25)  # This ability inflicts only 25 % of the Ki damage

        await target.inflict_damage(client, ctx, caster, damage_done[1], team_a, team_b)

        move += await Display_move(client, ctx, self.name, self.icon, damage_done[1], caster, target, ki_gain = caster.ki_regen, is_ki = True, crit = damage_done[0])
        
        return(move)
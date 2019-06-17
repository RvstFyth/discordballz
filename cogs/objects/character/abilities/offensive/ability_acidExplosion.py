'''
Manages the Acid explosion ability.

Last update: 15/06/19
'''

# Dependancies

import asyncio

# Object

from cogs.objects.character.abilities.ability import Ability

from cogs.objects.character.abilities_effects.damages_over_time.acid import Acid

from cogs.objects.character.abilities_effects.debuff.acid_explosion import Acid_Explosion

# Utils

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.commands.fight.displayer.display_move import Display_move
from cogs.utils.functions.commands.fight.functions.damage_calculator import Damage_calculator

from cogs.utils.functions.commands.fight.functions.effect.has_effect import Has_debuff, Has_dot
from cogs.utils.functions.commands.fight.functions.effect.get_effect import Get_debuff, Get_dot

class Ability_AcidExplosion(Ability):

    icon = '<:acid_explosion_ki:590111692751372288>'
    id = 3

    def __init__(self):
        Ability.__init__(self)

        self.name = 'Acid Explosion'
        self.description = ''

        self.cost = 30
        self.cooldown = 0

        self.need_target = True
        self.can_target_ally = False

    async def init(self, client, ctx, caster):
        '''
        `coroutine`
        '''

        _ = await Translate(client, ctx)

        self.name = _('Acid Explosion')
        self.description = _('Inflicts **50 %** of your Ki damage to the target.\nIf the target has **3** stacks of {} causes {} to **splash** onto all other units in **enemy team**. Add one stack of {} on them, they also take **2 %** more damage per {} stacks active on them.').format(Acid().icon, Acid().icon, Acid().icon, Acid().icon)
        
        return
    
    async def trigger(self, client, ctx, caster, target, team_a, team_b, move = None, ability = None):
        '''
        `coroutine`

        Applies the debuf Acid explosion on the target
        '''

        # Init

        has_debuff = await Has_debuff(target, Acid_Explosion())  # Check if the target has the debuff

        if has_debuff:  # If the target already has the debuff, we reset the duration
            acid_explosion = await Get_debuff(target, Acid_Explosion())

            target.debuff.remove(acid_explosion)
            acid_explosion.duration = 2
            target.debuff.append(acid_explosion)
        
        else:  # If not, we add the debuff
            acid_explosion = Acid_Explosion()
            target.debuff.append(acid_explosion)

        # Splash acid

        has_acid = await Has_dot(target, Acid())

        if has_acid:
            # If the target has acid 
            acid_ = await Get_dot(target, Acid())

            if acid_.stack >= 3:  # Spread if the target has at least 3 stacks
                # Now spread
                for char_a in team_b:  # For each character in enemy team
                    await asyncio.sleep(0)
                    
                    has_dot = await Has_dot(char_a, Acid())

                    if has_dot:  # If the character has dot we just add a stack
                        dot = await Get_dot(char_a, Acid())

                        char_a.dot.remove(dot)

                        if(dot.stack < dot.max_stack): 
                            dot.stack += 1
                        
                        else:
                            pass
                        
                        char_a.dot.append(dot)
                    
                    else:
                        dot = Acid()
                        dot.stack = 1
                        dot.total_damage = int(((1+((caster.ki_damage_max/100)*0.5))*char_a.max_hp)/100)
                        dot.tick_damage = int((dot.total_damage/dot.duration))*dot.stack

                        char_a.dot.append(dot)

        # inflict damages

        damage_done = await Damage_calculator(caster, target, is_ki = True)

        damage_done = int(damage_done*0.5)

        await target.inflict_damage(client, ctx, caster, damage_done, team_a, team_b)

        move += await Display_move(client, ctx, self.name, self.icon, damage_done, caster, target, is_ki = True)
        return(move)
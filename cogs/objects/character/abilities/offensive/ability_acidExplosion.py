'''
Manages the Acid explosion ability.

Last update: 26/06/19
'''

# Dependancies

import asyncio
from random import randint

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
        self.can_target_enemy = True

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
                    
                    await acid_.add_stack(caster, char_a, team_a, team_b)
                    
        # inflict damages
        damage = randint(caster.ki_damage_min, caster.ki_damage_max)
        damage_done = await Damage_calculator(caster, damage, target, is_ki = True, damage_reduction = target.damage_reduction, can_crit = True, crit_chance = caster.critical_chance, crit_bonus = caster.critical_bonus)

        damage_done[1] = int(damage_done[1]*0.5)

        await target.inflict_damage(client, ctx, caster, damage_done[1], team_a, team_b)

        move += await Display_move(client, ctx, self.name, self.icon, damage_done[1], caster, target, is_ki = True, crit = damage_done[0])
        return(move)
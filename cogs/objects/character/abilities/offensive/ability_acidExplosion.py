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

from cogs.utils.functions.commands.fight.functions.effect.has_effect import Has_debuff
from cogs.utils.functions.commands.fight.functions.effect.get_effect import Get_debuff

class Ability_AcidExplosion(Ability):

    icon = '<:acid_explosion_ki:589512689181786142>'
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
            target.debuf.append(acid_explosion)
        
        else:  # If not, we add the debuff
            acid_explosion = Acid_Explosion()
            target.debuff.append(acid_explosion)

        move += await Display_move(client, ctx, self.name, self.icon, 0, caster, target, is_ki = True)
        return(move)
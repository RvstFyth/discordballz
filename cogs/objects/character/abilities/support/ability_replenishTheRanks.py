'''
Manages the ability Replenish the Ranks

Last update: 16/06/19
'''

# dependancies

import asyncio

# object

from cogs.objects.character.abilities.ability import Ability
from cogs.objects.character.abilities_effects.buff.replenish_the_ranks import Buff_ReplenishTheRanks
from cogs.objects.character.abilities.offensive.ability_acid import Acid

# Utils

from cogs.utils.functions.commands.fight.displayer.display_move import Display_move
from cogs.utils.functions.translation.gettext_config import Translate

class Ability_ReplenishTheRanks(Ability):

    icon = '<:replenish_the_ranks_ki:589892321298874419>'
    id = 5
    
    def __init__(self):
        Ability.__init__(self)
        # Basics
        self.name = 'Replenish the Ranks'
        self.description = ''

        self.need_target = False
        self.cost = 80
        self.cooldown = 0
    
    async def init(self, client, ctx, caster):
        '''
        `coroutine`

        translate
        '''

        _ = await Translate(client, ctx)

        self.name = _('Replenish the Ranks')
        self.description = _('If a **Saibaiman** dies in the next **2 turns**, a copy of **Blue Saibaiman** replaces it.\nThe copy starts with **10** % of its maximum health and cannot use any ability except **[{}]**{}.').format(Acid().name, Acid().icon)
        
        return
    
    async def trigger(self, client, ctx, caster, target, team_a, team_b, move = None, ability = None):
        '''
        `coroutine`

        Applies the buff to all Saibaiman in your team.
        '''

        for character in team_a:
            await asyncio.sleep(0)

            if(character.id == 1 or character.id == 2 or character.id == 3):  # if the character is a saibaiman
                character.buff.append(Buff_ReplenishTheRanks())
        
        move += await Display_move(client, ctx, self.name, self.icon, 0, caster, caster)
        return(move)
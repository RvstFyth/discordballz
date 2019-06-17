'''
Manages the buff replenish the ranks.

Last update: 16/06/19
'''

# dependancies

import asyncio

# objects

from cogs.objects.character.abilities_effects.buff._buff_object import Buff
from cogs.objects.character.abilities_effects.on_dying.replenish_the_ranks import Dying_ReplenishTheRanks

class Buff_ReplenishTheRanks(Buff):

    name = 'Replenish the Ranks'
    id = 2
    icon = '<:replenish_the_ranks:589892376634458144>'

    def __init__(self):
        Buff.__init__(self)
        # basics

        self.duration = 2
        self.max_stack = 1
        self.stack = 1
    
    async def apply(self, client, ctx, target, team_a, team_b):
        '''
        `coroutine`

        We check if the target has this effect as .dying, if not we add it.
        '''

        # loop into the dying

        found = False

        for effect in target.dying:  # We loop in all the effect stored
            await asyncio.sleep(0)

            if(effect.id == Dying_ReplenishTheRanks().id):  # If we find the dying effect
                found = True
                break

        if(found == False):  # If the effect has not been found we add it
            target.dying.append(Dying_ReplenishTheRanks())
        
        else:
            pass
        
        return(0)

    async def on_remove(self, client, ctx, target, team_a, team_b):
        '''
        `coroutine`

        On remove we just remove this effect from the target.
        '''

        for effect_ in target.dying:  # Loop into the effects
            await asyncio.sleep(0)

            if(effect_.id == Dying_ReplenishTheRanks().id):  # if we fin the effect, remove it
                target.dying.remove(effect_)
                break
        
        return
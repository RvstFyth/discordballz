'''
Manages the debuff paralyzing burn.

Last update: 17/06/19
'''

# dependancies

import asyncio

# object

from cogs.objects.character.abilities_effects.debuff._debuff_object import Debuff

class Debuff_ParalyzingBurns(Debuff):

    name = 'Paralyzing Burns'
    icon = '<:paralyzing_burns:590183265886011392>'
    id = 2

    def __init__(self):
        Debuff.__init__(self)
        self.stack = 1
        self.max_stack = 1
        self.duration = 2
    
    async def apply(self, client, ctx, target, team_a, team_b):
        '''
        `coroutine`

        apply the flag = 3 to the target.
        '''
        
        target.flag = 3

        return(0)
    
    async def on_remove(self, client, ctx, target, team_a, team_b):
        '''
        `coroutine`

        reset the target flag to 0
        '''

        target.flag = 0

        return
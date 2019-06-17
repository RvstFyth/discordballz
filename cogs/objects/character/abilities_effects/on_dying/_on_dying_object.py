'''
Manages the .dying object.

Last update: 16/06/19
'''

# dependancies

import asyncio

class On_Dying:

    name = ''
    id = 0
    icon = ''

    def __init__(self):
        self.name = ''
        self.resurrect = False

    async def apply(self, client, ctx, target, team_a, team_b):
        pass
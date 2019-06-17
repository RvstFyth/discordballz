'''
Manages the buff object.

Last update: 03/06/19
'''

# Dependancies

import asyncio

class Buff:

    # Class attributes

    effect_type = 'buff'
    effect_description = 'Gives character bonus effects'

    name = ''
    id = 0
    icon = ''

    # Instance attributes

    def __init__(self):
        # Duration
        self.duration = 0

        # Stacks
        self.max_stack = 1
        self.stack = 0
    
    # Method

    async def apply(self, client, ctx, target, team_a, team_b):
        pass
    
    async def on_remove(self, client, ctx, target, team_a, team_b):  # Do seomthing when rempved
        pass
'''
Manages the debuff object.

Last update: 15/06/19
'''

# Dependancies

import asyncio

class Debuff:

    effect_type = 'debuff'
    effect_description = 'Gives character malus effects'

    def __init__(self):
        self.duration = 0

        self.max_stack = 1
        self.stack = 0

    async def apply(self):
        pass
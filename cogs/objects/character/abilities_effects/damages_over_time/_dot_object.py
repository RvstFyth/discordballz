'''
Manages the DoT object.

Last update: 23/06/19
'''

import asyncio

class Dot:
    '''
    Represent a damage over time effect.

    Attributes :
        Class :
        - effect_type
        - effect_description
    
        Instance :
        - duration : int
        - total_damage : int
        - tick_damage : int
        - max_stack : int
        - stack : int
    
    Method :
        - `coro` apply : return damage_done : int
    '''
    # Class attributes

    effect_type = 'dot'
    effect_description = 'Inflict damage over time.'

    # Instance attributes

    def __init__(self):
        # Infos
        self.name = ''
        # Duration
        self.duration = 1

        # Stacks
        self.max_stack = 1
        self.stack = 0

        # Damages
        self.total_damage = 0
        self.tick_damage = (self.total_damage/self.duration)*self.stack
    
    # Method

    async def set_tick_damage(self, caster, target, team_a, team_b):
        pass
    
    async def add_stack(self, caster, target, team_a, team_b):
        pass

    async def apply(self):
        '''
        Return: damage done (int)
        '''
        pass
    
    async def on_remove(self, client, ctx, target, team_a, team_b):  # Do seomthing when rempved
        pass
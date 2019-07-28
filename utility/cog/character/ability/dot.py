"""
Manages the DOT super class.

--

Author : DrLarck

Last update : 27/07/19
"""

# dependancies
import asyncio

# super dot class
class Dot:
    """
    Manages the DOT behaviour.

    - Parameter : 

    - Attribute :

    - Method :
    """

    # attribute
    def __init__(self, client, ctx, team):
        # client
        self.client = client
        self.ctx = ctx
        self.team = team

        # dot
        self.name = None
        self.description = None
        self.id = 0
        self.caster = None

        # duration
        self.initial_duration = 0
        self.duration = 0

        # stack
        self.max_stack = 0
        self.stack = 0

        # damage
        self.total_damage = 0
        self.tick_damage = 0

    # method
    async def apply(self):
        return

    # init
    async def set_tick_damage(self):
        return
    
    async def add_stack(self):
        return
    
    async def on_remove(self):
        return
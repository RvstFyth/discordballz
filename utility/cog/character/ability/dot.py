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
    def __init__(self, client, ctx):
        # client
        self.client = client
        self.ctx = ctx

        # dot
        self.name = None
        self.description = None
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
        """
        `coroutine`

        Applies the dot effect.

        -- 

        Return : str formatted string
        """

        return
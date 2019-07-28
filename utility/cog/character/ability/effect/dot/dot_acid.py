"""
Manages the Acid Dot.

--

Author : DrLarck

Last update : 28/07/19
"""

# dependance
import asyncio

# utils
from utility.cog.character.ability.dot import Dot

# dot acid
class Dot_acid(Dot):
    """
    Applies a DOT based on the target maximum health.
    """

    # attribute
    def __init__(self, client, ctx, target, team):
        # dot
        Dot.__init__(
            self,
            client,
            ctx,
            team
        )

        # attribute
        self.name = "Acid"
        self.caster = None
        self.target = target
        self.id = 1
        
            # duration
        self.initial_duration = 4
        self.duration = 4

            # stack
        self.max_stack = 3
        self.stack = 1
    
    # method
    async def add_stack(self):
        
        # applies dot
        _acid = await checker.get_effect(1)

        # check if the target already has acid on it
        has_acid = await checker.get_debuff(_acid)

        if(has_acid != None):  # if the target already has the effect on it
            _acid = has_acid
            

        else:  # the target doesn't have acid on it
            pass
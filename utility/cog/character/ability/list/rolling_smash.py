"""
Manages the rolling smash ability.

--

Author : DrLarck

Last update : 21/09/19
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability.ability import Ability

# ability
class Rolling_smash(Ability):
    """
    Deal physical damage and ignore the damage reduction.

    CD : 4 Turn
    """

    # attribute
    def __init__(self, client, ctx, caster, target, team_a, team_b):
        # inheritance
        Ability.__init__(
            self,
            client,
            ctx,
            caster,
            target,
            team_a,
            team_b
        )

        # stat
        self.name = "Rolling smash"
        self.cost = 0
        self.cooldown = 0  # can be used at first turn
    
    # method
    async def use(self):
        return
"""
Manages the Unity is Strenght ability.

--

Author : DrLarck

Last update : 30/08/19 (DrLarck)
"""

# dependancies
import asyncio

# utils
from utility.cog.displayer.move import Move_displayer
from utility.cog.character.ability.util.effect_checker import Effect_checker

# inheritance
from utility.cog.character.ability.ability import Ability

# spell
class Unity_is_strenght(Ability):
    """
    Applies the Unity is Strenght buff on the Saibaimen.
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

        # info
        self.name = "Unity is strenght"
        self.icon = ""
        self.cost = 60

        # special
        self.saibaimen = [1, 2, 3]  # represents the Saibaimen ids
    
    # method
    async def use(self):
        """
        `coroutine`

        Applies the Unity is strenght buff on all the allied Saibaimen.

        --

        Return : str
        """

        # init
        await self.caster.posture.change_posture("attacking")
        move = Move_displayer()
        checker = Effect_checker(self.caster)


"""
Represents the Unity is strenght buff

--

Author : DrLarck

Last update : 30/08/19 (DrLarck)
"""

# dependancies
import asyncio

# inheritance
from utility.cog.character.ability.buff import Buff

# unity is strenght
class Buff_unity_is_strenght(Buff):
    """
    Represents the unity is strenght buff
    """

    # attribute
    def __init__(self, client, ctx, team_a, team_b):
        # inheritance
        Buff.__init__(
            self,
            client,
            ctx,
            team_a,
            team_b
        )

        self.id = 2

    # method
    async def apply(self):
        """
        `coroutine`

        Applies the Buff on the targets

        -- 

        Return : None
        """

        return
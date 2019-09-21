"""
Manages the paralyzing burns debuff

--

Author : DrLarck

Last update : 21/09/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability._effect import Effect

# debuff
class Debuff_Paralyzing_burns(Effect):
    """
    Changes the target's posture each time the `.apply()` method is called.

    `.on_remove()` set the target's posture to attacking.
    """

    # attribute
    def __init__(self, client, ctx, carrier, team_a, team_b):
        # inheritance
        Effect.__init__(
            self,
            client,
            ctx,
            carrier,
            team_a,
            team_b
        )

        # info
        self.name = "Paralyzing burns"
        self.icon = "<:paralyzing_burns:590183265886011392>"
        self.id = 4

        # duration
        self.initial_duration = 2
        self.duration = 2
    
    # method
    async def apply(self):
        """
        `coroutine`

        Changes the posture of the carrier.

        --

        Return : None
        """

        # change the carrier's posture
        await self.carrier.posture.change_posture("stunned")

        return
    
    async def on_remove(self):
        """
        `coroutine`

        Set the carrier's posture to attacking.

        --

        Return : None
        """

        # change the carrier's posture
        await self.carrier.posture.change_posture("attacking")

        return
"""
Manages the Pilaf Barrier buff

--

Author : DrLarck

Last update : 28/09/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability._effect import Effect

# barrier buff
class Buff_pilaf_barrier(Effect):
    """
    Increases the unit's armor by 50 % for 1 turn and change its posture to defending.
    """

    # attribute
    def __init__(self, client, ctx, carrier, team_a, team_b):
        # inheritance
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        # duration
        self.name = "Pilaf barrier"
        self.icon = "<:pilaf_barrier_buff:627504114355535882>"
        self.id = 5
        self.initial_duration = 1
        self.duration = 1
    
    # method
    async def apply(self):
        """
        `coroutine`

        Increases the carrier's armor by 50 % and changes its posture.

        --

        Return : None
        """

        # change the posture
        await self.carrier.posture.change_posture("defending")

        # increase the armor
        self.carrier.defense.armor = int(self.carrier.defense.armor * 1.5)

        return
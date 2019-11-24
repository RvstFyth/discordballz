"""
Manages the red saibaiman's passive bonus.

--

Author : DrLarck

Last update : 20/10/19 (DrLarck)
"""

# dependancies
import asyncio

from utility.cog.character.ability._effect import Effect

class Buff_power_charge(Effect):
    """
    Make the saibaimans gain +2 ki per turn
    """

    # attribute
    def __init__(self, client, ctx, carrier, team_a, team_b):
        # inheritance
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        # info
        self.name = "Power charge"
        self.icon = self.game_icon["effect"]["red_saibaiman_leader"]
        self.description = "This unit gains **+2** :fire: per turn."

        self.is_permanent = True
    
    # method
    async def apply(self):
        """
        Add +2 ki gain to the carrier
        """

        self.carrier.regeneration.ki += 2

        return
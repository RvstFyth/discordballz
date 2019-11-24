"""
Red saibaiman passive

--

Author : DrLarck

Last update : 20/10/19 (DrLarck)
"""

# dependancies
import asyncio

from utility.cog.character.ability._effect import Effect
from utility.cog.character.ability.util.effect_checker import Effect_checker

class Passive_red_saibaiman(Effect):
    """
    Applies the Power charge passive to all allied saibaiman
    """

    # attribute
    def __init__(self, client, ctx, carrier, team_a, team_b):
        # inheritance
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        # info
        self.name = "Power charge"
        self.description = f"Applies **__Power Charge__**{self.game_icon['effect']['red_saibaiman_leader']} to the carrier"
        self.icon = self.game_icon["effect"]["red_saibaiman_leader"]
    
    # method
    async def apply(self):
        """
        Applies the Power charge bonus to the carrier
        """

        # init
        effect_checker = Effect_checker(self.carrier)
        power_ref = await effect_checker.get_effect(10, self.client, self.ctx, self.carrier, self.team_a, self.team_b)

        # check if the target already has the bonus
        has_power = await effect_checker.get_buff(power_ref)

        if(has_power == None):  # doesn't has the buff, add it
            self.carrier.bonus.append(power_ref)

        return
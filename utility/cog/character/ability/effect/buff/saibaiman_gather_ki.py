"""
Manages the Green Saibaiman's passive buff.

--

Author : DrLarck

Last update : 05/10/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability._effect import Effect
from utility.cog.character.ability.util.effect_checker import Effect_checker

# buff
class Buff_gather_ki(Effect):
    """
    The carrier gains 5 % of his allies Ki power
    """

    # attribute
    def __init__(self, client, ctx, carrier, team_a, team_b):
        # inheritance
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        # info
        self.name = "Saibaiman, gather our ki !"
        self.icon = self.game_icon['effect']['green_saibaiman_leader']
        self.id = 7

        # duration
        self.is_permanent = True

        # other
        self.saibaiman_list = [1, 2, 3]
    
    # method
    async def apply(self):
        """
        `coroutine`

        The carrier gains 5 % of the allied Saibaiman ki power.

        --

        Return : None
        """

        # init
        ki_bonus = 0

        for ally in self.team_a:
            await asyncio.sleep(0)

            if(ally.info.id != self.carrier.info.id):  # don't apply to the carrier
                if ally.info.id in self.saibaiman_list:
                    ki_bonus += int((5 * ally.damage.ki_max) / 100)  # 5 % of ally max ki
        
        # apply the ki bonus to the carrier
        self.carrier.damage.ki_min += ki_bonus
        self.carrier.damage.ki_max += ki_bonus

        return
"""
Manages the Green Saibaiman's passive.

--

Author : DrLarck

Last update : 29/09/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability._effect import Effect
from utility.cog.character.ability.util.effect_checker import Effect_checker

# icon

# green saibaiman passive
class Passive_green_saibaiman(Effect):
    """
    This saibaiman gains 5 % of his allied saibaiman's ki power
    """

    # attribute
    def __init__(self, client, ctx, carrier, team_a, team_b):
        # inheritance
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        # info
        self.name = "Saibaiman, gather our ki !"
        self.icon = self.game_icon['effect']['green_saibaiman_leader']
        self.description = f"Gains **5 %** of its allied Saibaiman's {self.game_icon['ki_ability']}."

    # method
    async def apply(self):
        """
        `coroutine`

        Applies a buff that makes the carrier gain 5 % of its allied Saibaiman ki power.

        --

        Return : None
        """

        # init
        effect_checker = Effect_checker(self.carrier)
        gather_ref = await effect_checker.get_effect(
            7,
            self.client,
            self.ctx,
            self.carrier,
            self.team_a,
            self.team_b
        )
        
        # check if the target has the buff
        has_gather = await effect_checker.get_buff(gather_ref)

        if(has_gather != None):  # pass, don't re add the buff
            pass 

        else:  # add the buff
            self.carrier.bonus.append(gather_ref)
        
        return

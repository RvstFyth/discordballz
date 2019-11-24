"""
Manages the red saibaiman leader skill

--

Author : DrLarck

Last update : 24/11/19 (DrLarck)
"""

# dependancies
import asyncio

from utility.cog.character.ability._effect import Effect
from utility.cog.character.ability.util.effect_checker import Effect_checker

class Leader_saibaiman_red(Effect):
    """
    Applies the Red Saibaiman passive to all saibaiman in the player's team.
    """

    # attribute
    def __init__(self, client, ctx, carrier, team_a, team_b):
        # inheritance
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        # info
        self.name = "Power Charge"
        self.description = f"The **allied** Saibaiman gain **__Power Charge__**{self.game_icon['effect']['red_saibaiman_leader']}."
        self.icon = self.game_icon['effect']['red_saibaiman_leader']

        # other
        self.saibaiman_list = [1, 2, 3]
    
    # method
    async def apply(self):
        """
        `coroutine`

        Add the Red Saibaiman's passive to all the allied Saibaiman.

        --

        Return : None
        """

        # init
        effect_checker = Effect_checker(self.carrier)
        passive_ref = await effect_checker.get_effect(
            10,
            self.client,
            self.ctx,
            self.carrier,
            self.team_a,
            self.team_b
        )

        # add the passive to all the allied saibaiman
        for ally in self.team_a:
            await asyncio.sleep(0)

            if ally.info.id in self.saibaiman_list:
                effect_checker = Effect_checker(ally)
                has_power = await effect_checker.get_buff(passive_ref)

            if(has_power == None):
                new_power = await effect_checker.get_effect(
                    10,
                    self.client,
                    self.ctx,
                    ally,
                    self.team_a,
                    self.team_b
                )
            
                ally.bonus.append(new_power)
        
        return
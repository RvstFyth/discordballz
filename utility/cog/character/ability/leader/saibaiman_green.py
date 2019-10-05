"""
Manages the Green Saibaiman's leader skill

--

Author : DrLarck

Last update : 05/10/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability._effect import Effect
from utility.cog.character.ability.util.effect_checker import Effect_checker

# leader
class Leader_green_saibaiman(Effect):
    """
    Applies the Green Saibaiman's base passive to all Saibaiman in the player's team.
    """

    # attribute
    def __init__(self, client, ctx, carrier, team_a, team_b):
        # inheritance
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        # info
        self.name = "Saibaiman, gather our ki !"
        self.icon = self.game_icon['effect']['green_saibaiman_leader']

        # other
        self.saibaiman_list = [1, 2, 3]

    # method
    async def apply(self):
        """
        `coroutine`

        Add green saibaiman's passive to all allied saibaiman.

        --

        Return : None
        """

        # init
        effect_checker = Effect_checker(self.carrier)
        passive_ref = await effect_checker.get_effect(
            7,
            self.client,
            self.ctx,
            self.carrier,
            self.team_a,
            self.team_b
        )

        # add the passive to all allied saibaiman
        for ally in self.team_a:
            await asyncio.sleep(0)

            if ally.info.id in self.saibaiman_list:
                # check if the ally has the buff

                effect_checker = Effect_checker(ally)
                has_gather = await effect_checker.get_buff(passive_ref)

                if(has_gather != None):
                    pass
            
                else:  # doesn't have the buff
                    new_gather = await effect_checker.get_effect(
                        7,
                        self.client,
                        self.ctx,
                        ally,
                        self.team_a,
                        self.team_b
                    )

                    ally.bonus.append(new_gather)
        
        self.triggered = True
        
        return
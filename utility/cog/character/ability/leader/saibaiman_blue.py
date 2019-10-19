"""
Manages the blue saibaiman leader skill.

--

Author : DrLarck

Last update : 18/10/19 (DrLarck)
"""

# dependancies
import asyncio

from utility.cog.character.ability._effect import Effect

from utility.cog.character.ability.util.effect_checker import Effect_checker

class Leader_blue_saibaiman(Effect):
    """
    Applies the passive Last will, Acid ! on the whole team.
    """

    # attribute
    def __init__(self, client, ctx, carrier, team_a, team_b):
        # inheritance
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        # info
        self.name = "Last will, Acid !"
        self.description = f"Applies the **__Last will, Acid !__** on death effect to the allied saibaiman."

        # other
        self.saibaiman_list = [1, 2, 3]

    # method
    async def apply(self):
        """
        Add the Blue saibaiman's passive to the other allied saibaiman.
        """

        # init
        effect_checker = Effect_checker(self.carrier)
        passive_ref = await effect_checker.get_effect(9, self.client, self.ctx, self.carrier, self.team_a, self.team_b)
    
        # add the passive to the allies
        for ally in self.team_a:
            await asyncio.sleep(0)

            if ally.info.id in self.saibaiman_list:
                # check if the ally has the passive

                effect_checker = Effect_checker(ally)
                has_last_will = await effect_checker.get_buff(passive_ref)

                if(has_last_will == None):
                    new_last = await effect_checker.get_effect(
                        9,
                        self.client,
                        self.ctx,
                        ally,
                        self.team_a,
                        self.team_b
                    )

                    ally.bonus.append(new_last)
        
        self.triggered = True

        return
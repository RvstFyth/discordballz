"""
Manages the blue saibaiman leader skill.

--

Author :

Last update : 02/02/2020 (RvStFyth)
"""

# dependencies
import asyncio

from utility.cog.character.ability._effect import Effect
from utility.cog.character.ability.util.effect_checker import Effect_checker


class Leader_power_of_youth(Effect):

    def __init__(self, client, ctx, carrier, team_a, team_b):
        # inheritance
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        # info
        self.name = "Power of youth!!"
        self.description = f"Applies the **__{self.name}__**other allies deal +10% damage with their first attack of the battle**."
        self.icon = ""

    async def apply(self):
        """
        other allies deal +10% damage with their first attack of the battle
        :return:
        """
        effect_checker = Effect_checker(self.carrier)
        skill_ref = effect_checker.get_effect(
            11,
            self.client,
            self.ctx,
            self.carrier,
            self.team_a,
            self.team_b
        )

        for ally in self.team_a:
            await asyncio.sleep(0)

            ally.bonus.append(skill_ref)

        self.triggered = True

        return


"""
Manages the saibaiman's passive last will, acid !

--

Author : DrLarck

Last update : 19/10/19 (DrLarck)
"""

# dependancies
import asyncio
from utility.cog.character.ability._effect import Effect

from utility.cog.character.ability.util.effect_checker import Effect_checker

class Buff_last_will_acid(Effect):
    """
    Add the on_death bonus.
    """

    # attribute
    def __init__(self, client, ctx, carrier, team_a, team_b):
        # inheritance
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        # info
        self.name = "Last will, Acid !"
        self.description = f"On death, applies **2** stacks of **__Acid__**{self.game_icon['effect']['acid']} on the enemy team."
        self.id = 9

        self.is_permanent = True

    # method
    async def apply(self):
        """
        Add on_death bonus.
        """

        effect_checker = Effect_checker(self.carrier)
        last_will_ref = await effect_checker.get_effect(8, self.client, self.ctx, self.carrier, self.team_a, self.team_b)

        # check if the carrier has the buff or not
        has_last_will = False

        for on_death in self.carrier.on_death:
            await asyncio.sleep(0)

            if(on_death.id == last_will_ref.id):
                has_last_will = True
    
        if not has_last_will:  # if the target doesn't have last will
            self.carrier.on_death.append(last_will_ref)
            self.triggered = True

        return
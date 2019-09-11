"""
Manages the Acid Explosion ability.

--

Author : DrLarck

Last update : 11/09/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability.ability import Ability

# acid explosion
class Acid_explosion(Ability):
    """
    Represents the Acid explosion ability.
    """

    # attribute
    def __init__(self, client, ctx, caster, target, team_a, team_b):
        # inheritance
        Ability.__init__(
            self,
            client,
            ctx,
            caster,
            target,
            team_a,
            team_b
        )

        self.name = "Acid explosion"
        self.icon = "<:acid_explosion_ki:590111692751372288>"
        self.cost = 30

        self.need_target = True
        self.target_enemy = True
    
    # method
    async def use(self):
        """
        `coroutine`

        Inflicts 50 % of the caster's ki damage to the target.

        If the target has at least 3 stacks of acid, splashes it onto all of the target's team members.

        Applies the Acid explosion debuff that increases the ki damages that they take by 2 %.

        --

        Return : str
        """

        
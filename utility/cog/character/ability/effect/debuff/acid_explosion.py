"""
Manages the acid explosion debuff

--

Author : DrLarck

Last update : 29/09/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability.util.effect_checker import Effect_checker
from utility.cog.character.ability._effect import Effect

# acid explosion debuf
class Debuff_acid_explosion(Effect):
    """
    Represents the acid_explosion debuff.
    """

    # attribute
    def __init__(self, client, ctx, carrier, team_a, team_b):
        # inheritance
        Effect.__init__(
            self,
            client,
            ctx,
            carrier,
            team_a,
            team_b
        )

        # info
        self.name = "Acid explosion"
        self.icon = self.icon['effect']['acid_explosion']
        self.id = 3

        # duration
        self.initial_duration = 2
        self.duration = 2

        # stacking
        self.max_stack = 1
        self.stack = 1
    
    # method
    async def apply(self):
        """
        `coroutine`

        Reduces the carrier's spirit amount by 2 %.

        --

        Return : None
        """

        # init
        effect_checker = Effect_checker(self.carrier)
        reduction = int(0.02 * self.carrier.defense.spirit)  # get 2 % of the carrier's spirit
        acid_ref = await effect_checker.get_effect(
            1,
            self.client,
            self.ctx,
            self.carrier,
            self.team_a,
            self.team_b
        )

        carrier_acid = await effect_checker.get_debuff(acid_ref)

        if(carrier_acid != None):
            reduction = int(reduction * carrier_acid.stack)
        
        # reduce the spirit of the carrier
        self.carrier.defense.spirit -= reduction

        return

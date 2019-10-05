"""
Manages the triple pilots passive skill.

--

Author : DrLarck

Last update : 28/09/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability._effect import Effect
from utility.cog.character.ability.util.effect_checker import Effect_checker

# passive
class Passive_triple_pilots(Effect):
    """
    Can only be triggered once : add 2 stacks of Triple pilots buff to the carrier.
    """

    # attribute
    def __init__(self, client, ctx, carrier, team_a, team_b):
        # inheritance
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        # info
        self.name = "Triple pilots"
        self.description = "Add 2 stacks of **__Triple pilots__** to the caster."
        self.icon = "<:triple_pilots_buff:627508545062961164>"

    # method
    async def apply(self):
        """
        `coroutine`

        Add the two stacks to the carrier.

        --

        Return : None
        """

        # init
        if not self.triggered:
            effect_checker = Effect_checker(self.carrier)
            triple_ref = await effect_checker.get_effect(
                6,
                self.client,
                self.ctx,
                self.carrier,
                self.team_a,
                self.team_b
            )

            # check if the target already has the buff
            has_triple = await effect_checker.get_buff(triple_ref)

            if(has_triple != None):
                # add 2 stacks
                has_triple.stack += 2
            
            else:  # doesn't have triple
                triple_ref.stack = 2
                self.carrier.bonus.append(triple_ref)
            
            self.triggered = True

        return
"""
Manages the On death Last will, acid ! effect.

--

Author : DrLarck

Last update : 19/10/19 (DrLarck)
"""

# dependancies
import asyncio

from utility.cog.character.ability._effect import Effect
from utility.cog.character.ability.util.effect_checker import Effect_checker

class Event_last_will_acid(Effect):
    """
    On death, applies 2 stacks of acids on the targets.
    """

    # attribute
    def __init__(self, client, ctx, carrier, team_a, team_b):
        # inheritance
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        # info
        self.name = "Last will, Acid !"
        self.description = f"On death, applies **2** stacks of {self.game_icon['effect']['acid']} on the enemy team."
        self.id = 8
    
        self.is_permanent = True

    # method
    async def apply(self):
        """
        Applies 2 stacks of acid on the enemy team.
        """

        for enemy in self.team_b:
            await asyncio.sleep(0)

            effect_checker = Effect_checker(enemy)
            acid_ref = await effect_checker.get_effect(1, self.client, self.ctx, enemy, self.team_a, self.team_b)

            # check if the target has acid
            has_acid = await effect_checker.get_debuff(acid_ref)

            if(has_acid != None):  # add 2 stack of acid to the current acid effect
                await has_acid.add_stack()
                await has_acid.add_stack()
            
            else:
                await acid_ref.add_stack()
                await acid_ref.add_stack()
        
        return
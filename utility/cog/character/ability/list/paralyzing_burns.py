"""
Manages the paralyzing burns ability.

--

Author : DrLarck

Last update : 21/09/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability.ability import Ability
from utility.cog.character.ability.util.effect_checker import Effect_checker

# ability
class Paralyzing_burns(Ability):
    """
    Stuns the target according how many active acid stacks it has on it.
    Remove the acid stacks.

    Stun duration : 2 turns if == 3 acid 

    4 turns if >=3 acid

    The stun will be a malus effect which stuns at each applying.
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

        # stat
        self.name = "Paralyzing burns"
        self.cost = 75
        
        # targetting
        self.need_target = True
        self.target_enemy = True
    
    # method
    async def use(self):
        """
        `coroutine`

        Applies the Paralyzing debuff on the target.

        If the target already has the debuff : reset the duration

        --

        Return : str
        """

        # init
        effect_checker = Effect_checker(self.target)


"""
Represents the Unity is strenght buff

--

Author : DrLarck

Last update : 07/09/19 (DrLarck)
"""

# dependancies
import asyncio

# inheritance
from utility.cog.character.ability.buff import Buff

# util
from utility.cog.character.ability.util.effect_checker import Effect_checker

# unity is strenght
class Buff_unity_is_strength(Buff):
    """
    Represents the unity is strenght buff
    """

    # attribute
    def __init__(self, client, ctx, carrier, team_a, team_b):
        # inheritance
        Buff.__init__(
            self,
            client,
            ctx,
            carrier,
            team_a,
            team_b
        )

        self.id = 2
        self.name = "Unity is strength"
        self.icon = "<:unity_is_strenght:585503883133059074>"

        self.initial_duration = 3
        self.stack = 1

    # method
    async def apply(self):
        """
        `coroutine`

        Heals up the carrier for each acid stacks active on the enemy team.

        -- 

        Return : None
        """

        # init
        checker = Effect_checker(None)
        acid_stacks = 0
        # we don't need to pass the target as we just want to get the acid.id (None)
        acid = await checker.get_effect(
            1,
            self.client,
            self.ctx,
            self.carrier,
            self.team_a,
            self.team_b
        )

        # check the enemy team
        for character in self.team_b:
            await asyncio.sleep(0)

            # check if the target has the acid effect on it
            checker = Effect_checker(character)
            _acid = await checker.get_debuff(acid)

            if(_acid != None):
                # count the stacks
                acid_stacks += _acid.stack

                # improve the debuff
                _acid.max_stack = 5
                _acid.initial_duration = 5

        # now heal the carrier
        if(acid_stacks > 0):
            heal = int(acid_stacks * (0.1 * self.carrier.damage.ki_max))
            self.carrier.health.current += heal 
            await self.carrier.health.health_limit()

        return
    
    async def on_remove(self):
        """
        Reset all the acid effects. (Duration and max stacks)
        """

        # now retrieve all the acid effects
        # team b because we reset the effect in the enemy team
        for character in self.team_b:
            await asyncio.sleep(0)

            # init the checker
            checker = Effect_checker(character)
            acid_ref = await checker.get_effect(
                1,
                self.client,
                self.ctx,
                character,
                self.team_a,
                self.team_b
            )
            acid_active = await checker.get_debuff(acid_ref)

            # now reset
            if(acid_active != None):
                # duration
                acid_active.initial_duration = acid_ref.initial_duration
                if(acid_active.duration > acid_ref.initial_duration):
                    acid_active.duration = acid_ref.initial_duration
                
                # stack
                acid_active.max_stack = acid_ref.max_stack
                if(acid_active.stack > acid_ref.max_stack):
                    acid_active.stack = acid_ref.max_stack
                
        return
"""
Manages the spreading acid ability.

--

Author : DrLarck

Last update : 21/09/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability.ability import Ability
from utility.cog.displayer.move import Move_displayer
from utility.cog.character.ability.util.effect_checker import Effect_checker

# spreading acid
class Spreading_acid(Ability):
    """
    Add a stack of acid to all the characters that have at least one stack of acid active on it.
    """

    # attribute
    def __init__(self, client, ctx, caster, target, team_a, team_b):
        # inheritance
        Ability.__init__(
            self,
            client,
            ctx,
            caster,
            caster,
            team_a,
            team_b
        )

        # ability
        self.name = "Spreading acid"
        self.icon = "<:spreading_acid_ki:590184731232960523>"
        self.cost = 30
    
    # method
    async def use(self):
        """
        `coroutine`

        Add a stack to all active acid debuff on the enemy team.

        --

        Return : str
        """

        # init
        move = Move_displayer()
        effect_checker = Effect_checker(self.caster)
        has_unity = False

        acid_ref = await effect_checker.get_effect(
            1,
            self.client,
            self.ctx,
            self.caster,
            self.team_a,
            self.team_b
        )

        unity_ref = await effect_checker.get_effect(
            2,
            self.client,
            self.ctx,
            self.caster,
            self.team_a,
            self.team_b
        )

        # check if there is a unity buff in the team a
        for ally in self.team_a:
            await asyncio.sleep(0)

            unity_checker = Effect_checker(ally)
            unity = await unity_checker.get_buff(unity_ref)

            if(unity != None):
                has_unity = True
                break
        
        # now increase the stack of acids
        for enemy in self.team_b:
            await asyncio.sleep(0)

            acid_checker = Effect_checker(enemy)
            acid = await acid_checker.get_debuff(acid_ref)

            if(acid != None):
                await acid.add_stack()

        # set up the move display
        _move = await move.get_new_move()

        _move["name"] = self.name
        _move["icon"] = self.icon
        _move["ki"] = True

        _move = await move.effect_move(_move)

        return(_move)
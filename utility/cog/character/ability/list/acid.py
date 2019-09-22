"""
Manages the Acid ability.

--

Author : DrLarck

Last update : 22/09/19 (DrLarck)
"""

# dependance
import asyncio
from random import randint

# utility
from utility.cog.displayer.move import Move_displayer
from utility.cog.fight_system.calculator.damage import Damage_calculator

from utility.cog.character.ability.ability import Ability
from utility.cog.character.ability.effect.dot.dot_acid import Dot_acid
from utility.cog.character.ability.util.effect_checker import Effect_checker

# ability
class Acid(Ability):
    """
    This ability applies a DOT on the target. This DOT inflicts damage
    at each turn.
    """

    # attribute
    def __init__(self, client, ctx, caster, target, team_a, team_b):
        Ability.__init__(
            self,
            client,
            ctx,
            caster,
            target,
            team_a,
            team_b
        )

        self.name = "Acid"

        self.icon = "<:acid:583953112406949888>"
        self.description = f"""Inflicts **25 %** of your {self.game_icon['ki_ability']} damage and applies a stack of **__Acid__** to the target.
Each stack of **__Acid__** inflicts an amount of **1.5 % (+ 5 % of the highest Saibaiman {self.game_icon['ki_ability']} /250 in your team)** of the target's **Maximum** :hearts: as {self.game_icon['ki_ability']} damage per stack each turn.
Lasts **3** turns."""

        self.cost = 8
        self.need_target = True
        self.target_enemy = True
    
    # method
    async def use(self):
        """
        `coroutine`

        Inflicts damage and applies a dot to the target.

        --

        Return : str
        """

        # init
        await self.caster.posture.change_posture("attacking")

        move = Move_displayer()
        calculator = Damage_calculator(self.caster, self.target)
        checker = Effect_checker(self.target)

        # get the damage
        damage = randint(self.caster.damage.ki_min, self.caster.damage.ki_max)
        damage = int(damage * 0.25)  # the ability inflicts only 25 % of the ki damage
        damage = await calculator.ki_damage(
            damage,
            critable = True,
            dodgable = True
        )

        # define move info
        _move = await move.get_new_move()

        _move["name"] = self.name
        _move["icon"] = self.icon
        _move["damage"] = damage["calculated"]
        _move["critical"] = damage["critical"]
        _move["dodge"] = damage["dodge"]
        _move["ki"] = True

        _move = await move.offensive_move(_move)

        # inflict damage
        await self.target.receive_damage(damage["calculated"])

        # add a stack of acid on the target
        _acid = Dot_acid(
            self.client,
            self.ctx,
            self.target,
            self.team_a,
            self.team_b
        )

        await _acid.add_stack()

        return(_move)
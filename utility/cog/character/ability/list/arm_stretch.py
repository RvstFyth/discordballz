"""
Manages the Arm Stretch ability

--

Author : Zyorhist

Last update : 30/01/20 (DrLarck)
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
class Arm_stretch(Ability):
    """
    This ability applies performs a sequence attack against any enemy
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

        self.name = "Arm Stretch"
        #self.icon = self.game_icon['ability']['arm_stretch']
        self.description = f"""Performs a sequence attack against any enemy"""

        self.cost = 5
        self.need_target = True
    
    # method
    async def set_tooltip(self):
        self.tooltip = f"Performs a sequence attack against any enemy"

        return

    async def use(self):
        """
        `coroutine`

        Performs a sequence attack against any enemy

        --

        Return : str
        """

        # init
        await self.caster.posture.change_posture("attacking")

        move = Move_displayer()
        calculator = Damage_calculator(self.caster, self.target)
        checker = Effect_checker(self.target)

        # get the damage
        damage = randint(self.caster.damage.physical_min, self.caster.damage.physical_max)
        damage = await calculator.physical_damage(
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
        _move["physical"] = True

        _move = await move.offensive_move(_move)

        # inflict damage
        await self.target.receive_damage(damage["calculated"])

        return(_move)

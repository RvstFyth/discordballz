"""
Manages the rolling smash ability.

--

Author : DrLarck

Last update : 21/09/19
"""

# dependancies
import asyncio
from random import randint

# util
from utility.cog.character.ability.ability import Ability

from utility.cog.fight_system.calculator.damage import Damage_calculator

from utility.cog.displayer.move import Move_displayer

# ability
class Rolling_smash(Ability):
    """
    Deal physical damage and ignore the damage reduction.

    CD : 4 Turn
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
        self.name = "Rolling smash"
        self.cost = 0
        self.cooldown = 0  # can be used at first turn

        # targetting
        self.need_target = True
        self.target_enemy = True
    
    # method
    async def use(self):
        """
        `coroutine`

        Inflicts 150 % of the character's physical damage and ignore the damage reduction.

        Cooldown : 4 turns.

        --

        Return : str
        """

        # init
        move = Move_displayer()
        damage_calculator = Damage_calculator(self.caster, self.target)

        roll_damage = int((randint(self.caster.damage.physical_min, self.caster.damage.physical_max)) * 1.5)
        damage_done = await damage_calculator.physical_damage(
            roll_damage,
            dodgable = True,
            critable = True,
            ignore_defense = True
        )
        
        # inflict the damage to the target
        await self.target.receive_damage(damage_done["calculated"])

        # set the cooldown
        self.cooldown = 4

        # set the move
        _move = await move.get_new_move()

        _move["name"] = self.name
        _move["icon"] = self.icon
        _move["damage"] = damage_done["calculated"]
        _move["dodge"] = damage_done["dodge"]
        _move["critical"] = damage_done["critical"]
        _move["physical"] = True

        _move = await move.offensive_move(_move)

        return(_move)
"""
Manages the Acid ability.

--

Author : DrLarck

Last update : 27/07/19
"""

# dependance
import asyncio
from random import randint

# utility
from utility.cog.fight_system.calculator.damage import Damage_calculator
from utility.cog.displayer.move import Move_displayer
from utility.cog.fight_system.calculator.damage import Damage_calculator
from utility.cog.character.ability.ability import Ability

# ability
class Acid(Ability):
    """
    This ability applies a DOT on the target. This DOT inflicts damage
    at each turn.

    - Parameter :

    - Attribute :

    - Method :
    """

    # attribute
    def __init__(self, client, ctx, caster, target, team):
        Ability.__init__(
            self,
            client,
            ctx,
            caster,
            target,
            team
        )

        self.name = "Acid"
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
        move = Move_displayer()
        calculator = Damage_calculator(self.caster, self.target)

        # get the damage
        damage = randint(self.caster.damage.ki_min, self.caster.damage.ki_max)
        damage = int(damage * 0.25)  # the ability inflicts only 25 % of the ki damage
        damage = await calculator.ki_damage(damage)

        _move = {
            "name" : self.name,
            "icon" : self.icon,
            "damage" : damage["calculated"],
            "critical" : damage["critical"],
            "dodge" : damage["dodge"],
            "physical" : False,
            "ki" : True
        }

        _move = await move.offensive_move(_move)

        # inflict damage
        await self.target.receive_damage(damage["calculated"])

        return(_move)
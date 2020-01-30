"""
Manages the rolling special beam canon ability

--

Author : Zyorhist

Last update : 30/01/20 (DrLarck)
"""

# dependancies
import asyncio
from random import randint

# util
from utility.cog.character.ability.ability import Ability

from utility.cog.fight_system.calculator.damage import Damage_calculator

from utility.cog.displayer.move import Move_displayer

# ability
class Special_beam_cannon(Ability):
    """
    Deal true damage to opponent
    
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
        self.name = "Special Beam Cannon"
        self.description = f"""Inflicts **50 %** of your  {self.game_icon['ki_ability']} damage as true damage"""
        
        self.icon = self.game_icon['ability']['specual_beam_cannon']

        self.cost = 40

        # targetting
        self.need_target = True
        self.target_enemy = True
    
    # method
    async def set_tooltip(self):
        self.tooltip = f"Inflicts **{int(self.caster.damage.ki_min * 0.5):,}** - **{int(self.caster.damage.ki_max * 0.5):,}** true damage."

        return
        
    async def use(self):
        """
        `coroutine`

        Inflicts 50% of users ki as true damage 

        --

        Return : str
        """

        # init
        move = Move_displayer()
        damage_calculator = Damage_calculator(self.caster, self.target)

        roll_damage = int((randint(self.caster.damage.ki_min, self.caster.damage.ki_max)) * 0.5)
        damage_done = await damage_calculator.physical_damage(
            roll_damage,
            dodgable = True,
            critable = False,
            ignore_defense = True
        )
        
        # inflict the damage to the target
        await self.target.receive_damage(damage_done["calculated"])

        # set the move
        _move = await move.get_new_move()

        _move["name"] = self.name
        _move["icon"] = self.icon
        _move["damage"] = damage_done["calculated"]
        _move["dodge"] = damage_done["dodge"]
        _move["critical"] = damage_done["critical"]
        _move["physical"] = False
        _move["ki"] = False

        _move = await move.offensive_move(_move)

        return(_move)

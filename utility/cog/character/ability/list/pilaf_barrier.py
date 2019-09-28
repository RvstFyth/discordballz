"""
Manages the Pilaf Barrier ability

--

Author : DrLarck

Last update : 28/09/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability.ability import Ability
from utility.cog.character.ability.util.effect_checker import Effect_checker
from utility.cog.displayer.move import Move_displayer

# ability
class Pilaf_barrier(Ability):
    """
    Pilaf takes 50 % reduced physical damage and is considered defending this turn.

    Cooldown : 3 turns
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

        # info
        self.name = "Pilaf barrier"
        self.description = f"""Applies **__Pilaf Barrier__** bonus on this unit which makes it take **50 %** less :punch: damage for **1** turn and change its posture to :shield:.
{self.game_icon['cooldown']}**Cooldown** : **3** turns.
        """
        self.icon = "<:pilaf_barrier:627504111792816128>"

        self.cost = 0
    
    # method
    async def use(self):
        """
        `coroutine`

        Applies the Pilaf Barrier buff on the caster.

        --

        Return : str
        """

        # init
        # change the posture
        move = Move_displayer()
        _move = await move.get_new_move()

        effect_checker = Effect_checker(self.caster)
        barrier_ref = await effect_checker.get_effect(
            5,
            self.client,
            self.ctx,
            self.caster,
            self.team_a,
            self.team_b
        )

        await self.caster.posture.change_posture("defending")

        # first check if the target (caster) already have the buff active
        has_barrier = await effect_checker.get_buff(barrier_ref)

        if(has_barrier != None):
            # just reset the duration
            has_barrier.duration = has_barrier.initial_duration
        
        else:  # if the target doesn't have the buff
            self.caster.bonus.append(barrier_ref)

        # set cooldown
        self.cooldown = 3

        # define the move
        _move["name"] = self.name
        _move["icon"] = self.icon
        
        _move = await move.effect_move(_move)

        return(_move)
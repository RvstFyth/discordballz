"""
Manages the syphon ability

--

Author : DrLarck

Last update : 22/09/19 (DrLarck)
"""

# dependancies
import asyncio
from random import randint

# util
from utility.cog.character.ability.ability import Ability
from utility.cog.displayer.move import Move_displayer
from utility.cog.character.ability.util.effect_checker import Effect_checker
from utility.cog.fight_system.calculator.damage import Damage_calculator

# syphon
class Syphon(Ability):
    """
    Represents the syphon ability.

    Consums all the acid stacks on the target and inflict huge damage according to the

    target missing health.
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

        self.name = "Syphon"
        self.description = f"""Inflicts **10 % (+ 2 % of the target's Missing :hearts: per __Acid__ stacks on the target)** of your {self.game_icon['ki_ability']} damage.
Heals you for an amount of **50 %** of the damage dealt."""

        self.icon = "<:syphon:585503902846418961>"
        self.cost = 25

        # targetting
        self.need_target = True
        self.target_enemy = True
    
    # method
    async def use(self):
        """
        `coroutine`

        See class description.

        --

        Return : str
        """

        # init
        move = Move_displayer()
        effect_checker = Effect_checker(self.target)
        damager = Damage_calculator(self.caster, self.target)

        missing_health = self.target.health.maximum - self.target.health.current
        roll_damage = randint(self.caster.damage.ki_min, self.caster.damage.ki_max)
        damage_done = await damager.ki_damage(
            roll_damage,
            dodgable = True,
            critable = True
        )

        # init the damage done
        damage_done["calculated"] = int(damage_done["calculated"] * 0.1)

        # special effect
        if not damage_done["dodge"]:  # if the damage has not been dodged
            # check if the target has acid stack active on it
            acid = await effect_checker.get_effect(
                1,
                self.client,
                self.ctx,
                self.target,
                self.team_a,
                self.team_b
            )

            has_acid = await effect_checker.get_debuff(acid)

            if(has_acid != None):
                damage_done["calculated"] += int(((2 * missing_health)/100) * has_acid.stack)
                
                # remove the acid debuff to the target
                # consums it
                self.target.malus.remove(has_acid)
            
            else:  # doesn't have acid active on it
                pass
        
        # deal damage to the target
        await self.target.receive_damage(damage_done["calculated"])
        
        # heal the caster
        # of 50 % of damage done
        healing = int(damage_done["calculated"] / 2)
        self.caster.health.current += healing
        await self.caster.health.health_limit()

        # setting up the move    
        _move = await move.get_new_move()
        _move["name"] = self.name
        _move["icon"] = self.icon
        _move["damage"] = damage_done["calculated"]
        _move["critical"] = damage_done["critical"]
        _move["dodge"] = damage_done["dodge"]
        _move["ki"] = True

        _move = await move.offensive_move(_move)

        # healing display
        if(healing > 0):
            _move += f"__Heal__ : +**{healing}** :hearts:\n"

        return(_move)
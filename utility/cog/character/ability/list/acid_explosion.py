"""
Manages the Acid Explosion ability.

--

Author : DrLarck

Last update : 21/09/19 (DrLarck)
"""

# dependancies
import asyncio
from random import randint

# util
from utility.cog.character.ability.ability import Ability
from utility.cog.fight_system.calculator.damage import Damage_calculator
from utility.cog.character.ability.util.effect_checker import Effect_checker
from utility.cog.displayer.move import Move_displayer

# acid explosion
class Acid_explosion(Ability):
    """
    Represents the Acid explosion ability.
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

        self.name = "Acid explosion"
        self.icon = "<:acid_explosion_ki:590111692751372288>"
        self.cost = 30

        self.need_target = True
        self.target_enemy = True
    
    # method
    async def use(self):
        """
        `coroutine`

        Inflicts 50 % of the caster's ki damage to the target.

        If the target has at least 3 stacks of acid, splashes it onto all of the target's team members.

        Applies the Acid explosion debuff that increases the ki damages that they take by 2 %.

        --

        Return : str
        """

        # init
        move = Move_displayer()
        effect_checker = Effect_checker(self.target)
        damage_calculator = Damage_calculator(self.caster, self.target)
        
        # debuff
        acid_ref = await effect_checker.get_effect(
            1,
            self.client,
            self.ctx,
            self.target,
            self.team_a,
            self.team_b
        )

        explosion_ref = await effect_checker.get_effect(
            3,
            self.client,
            self.ctx,
            self.target,
            self.team_a,
            self.team_b
        )

        # set the damage
        damage = randint(self.caster.damage.ki_min, self.caster.damage.ki_max)
        damage /= 2  # 50 % of the ki damage
        damage = await damage_calculator.ki_damage(
            damage,
            critable = True
        )

        # check if the target has acid
        has_acid = await effect_checker.get_debuff(acid_ref)

        if(has_acid != None):  # the target has an acid dot active on it
            # now check if the target has at least 3 stacks of acid
            if(has_acid.stack >= 3):
                # spread the dot onto the enemy members
                
                for unit in self.team_b:
                    await asyncio.sleep(0)

                    # init
                    effect_checker = Effect_checker(unit)

                    # check if the unit has acid stack
                    unit_has_acid = await effect_checker.get_debuff(acid_ref)

                    if(unit_has_acid != None):
                        await unit_has_acid.add_stack()
                        unit_has_acid.duration = unit_has_acid.initial_duration
                    
                    else:  # the unit doesn't have acid active on it
                        # create a new acid instance for the target
                        unit_acid = await effect_checker.get_effect(
                            1,
                            self.client,
                            self.ctx,
                            unit,
                            self.team_a,
                            self.team_b
                        )
                        # applies the new acid instance
                        await unit_acid.add_stack()
        
        # now check if the target already have explosion debuff active
        has_explosion = await effect_checker.get_debuff(explosion_ref)

        if(has_explosion != None):
            # reset the duration
            has_explosion.duration = has_explosion.initial_duration
        
        else:
            self.target.malus.append(explosion_ref)
        
        # setting up the move display
        _move = await move.get_new_move()

        _move["name"] = self.name
        _move["icon"] = self.icon
        _move["damage"] = damage["calculated"]
        _move["critical"] = damage["critical"]
        _move["dodge"] = damage["dodge"]
        _move["ki"] = True

        _move = await move.offensive_move(_move)

        return(_move)
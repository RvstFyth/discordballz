"""
Manages the Acid Dot.

--

Author : DrLarck

Last update : 06/09/19 (DrLarck)
"""

# dependance
import asyncio

# utils
from utility.cog.character.ability.dot import Dot
from utility.cog.character.ability.util.effect_checker import Effect_checker

# damage
from utility.cog.fight_system.calculator.damage import Damage_calculator

# dot acid
class Dot_acid(Dot):
    """
    Applies a DOT based on the target maximum health.
    """

    # attribute
    def __init__(self, client, ctx, target, team_a, team_b):
        # dot
        Dot.__init__(
            self,
            client,
            ctx,
            team_a,
            team_b
        )

        # attribute
        self.name = "Acid"
        self.icon = "<:acid:583953112406949888>"
        self.caster = None
        self.target = target
        self.id = 1
        
            # duration
        self.initial_duration = 4
        self.duration = 4

            # stack
        self.max_stack = 3
        self.stack = 1

        # unique
        self.damager = Damage_calculator(self.caster, self.target)
        self.saibaiman_id = [1, 2, 3]

    # method
    async def apply(self):
        """
        `coroutine`

        Inflicts the dot's damages to the target and returns its custom display.

        --

        Return : str formated for the acid's displaying
        """

        # init
        _damage = 0

        # increase the damage if the target has 3 or more active stacks on it
        if(self.stack >= 3):
            _damage = self.tick_damage * 1.5
        
        else:
            _damage = self.tick_damage
        
        _damage *= self.stack

        # get the damage
        # force it to be non-dodgable and non-critable to avoid the target dodge and the acid critical
        damage = await self.damager.ki_damage(
            _damage,
        )

        # apply the calculated damages to the target
        await self.target.receive_damage(damage["calculated"])

        return

    async def set_damage(self):
        # init
        highest_ki = 0

        # get the highest ki amount
        for ally in self.team_a:
            await asyncio.sleep(0)
            
            if(ally != None):
                if ally.info.id in self.saibaiman_id:  # only compare with saibaimen in the team.
                    if(ally.damage.ki_max > highest_ki):
                        highest_ki = ally.damage.ki_max
                
                else:
                    pass
        
        # set the total damage
        self.total_damage = int(((1.5 + ((highest_ki / 250) * 0.05)) * self.target.health.maximum) / 100) 

        self.tick_damage = self.total_damage

        return

    async def add_stack(self):
        # init
        checker = Effect_checker(self.target)
        unity = False

        _acid = await checker.get_effect(
            1,
            self.client,
            self.ctx,
            self.target,
            self.team_a,
            self.team_b
        )

        # check if the target already has acid on it
        has_acid = await checker.get_debuff(self)
        
        # look for someone in the team_a who has the unity is strength buff
        for ally in self.team_a:
            await asyncio.sleep(0)

            # get the character
            checker = Effect_checker(ally)
            
            unity_buff = await checker.get_effect(
                2,
                self.client,
                self.ctx,
                ally,
                self.team_a,
                self.team_b
            )

            if(ally != None):
                if ally.info.id in self.saibaiman_id:
                    _unity = await checker.get_buff(unity_buff)

                    if(_unity != None):  # if someone has the buff active
                        unity = True
                        break

        # increase acid stack   
        # get existing acid stack
        if(has_acid != None):  # if the target already has the effect on it
            _acid = has_acid
            self.target.malus.remove(_acid)
        
            # increase only if the max stack hasn't been reached
            if(_acid.stack < _acid.max_stack):
                if(unity):  # if an ally has the unity buff
                    _acid.stack += 2
                    
                    if(_acid.stack > _acid.max_stack):
                        _acid.stack = _acid.max_stack

                    _acid.duration = _acid.initial_duration
                
                else:  # if no unity in the team
                    _acid.stack += 1
                    _acid.duration = _acid.initial_duration

            # add or re-add the malus
            self.target.malus.append(_acid)

        else:  # if the target doesn't have acid on it
            if(unity):
                _acid.stack = 2
                _acid.initial_duration = 5

                await _acid.set_damage()
            
            else:
                _acid.stack = 1
                
                await _acid.set_damage()
                
            # add or re-add the malus
            self.target.malus.append(_acid)

        return
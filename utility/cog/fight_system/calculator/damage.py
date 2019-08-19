"""
Manages the damage calculator.

--

Author : DrLarck

Last update : 19/08/19 (DrLarck)
"""

# dependancies
import asyncio
from random import uniform

# damage calculator
class Damage_calculator:
    """
    Manages the damage calculation.

    - Parameter : 

    `attacker` : Represents the character that is attacking

    `target` : Represents the character that is attacked.

    - Attribute :

    `damage` {
        "calculated" : 0,
        "dodge" : False,
        "critical" : False
    }

    `type_bonus` : Represents type advantage multiplier

    `critical_bonus` : Represents the critical multiplier bonus

    `damage_reduction` : Damage reduction multiplier

    `armor` : Armor value (phy dmg)

    `spirit` : Spirit value (ki dmg)

    - Method :

    :coro:`get_type_advantage()` : Returns the type_advantage mutliplier

    :coro:`physical_damage(damage, dodgable, critable, ignore_defense) : Calculate physical damage
    returns the `damage` dict.

    :coro:`ki_damage(same as physical method)` : Same as physical but for ki.
    """

    # attribute
    def __init__(self, attacker, target):
        # param
        self.attacker = attacker
        self.target = target

        # attr
        self.damage = {
            "calculated" : 0,
            "dodge" : False,
            "critical" : False
        }
        self.type_bonus = 1
        self.critical_bonus = 1
        self.damage_reduction = 1 + self.target.defense.damage_reduction
        self.armor = 2500/(2500 + self.target.defense.armor)
        self.spirit = 2500/(2500 + self.target.defense.spirit)

    # method
    async def get_type_advantage(self):
        """
        `coroutine`

        Check if the attacker has a type advantage onto the target.

        --

        Return : directly modify the `type_bonus` value and return the multiplier bonus.
        """

        # init
        multiplier = 1
        target, attacker = self.target.type.value, self.attacker.type.value

        # advantage
            # phy > int
        if(attacker == 3 and target == 4):
            multiplier = 1.2

            # int > teq
        elif(attacker == 4 and target == 1):
            multiplier = 1.2

            # agl > str
        elif(attacker == 0 and target == 2):
            multiplier = 1.2

            # str > phy
        elif(attacker == 2 and target == 3):
            multiplier = 1.2

            # teq > agl
        elif(attacker == 1 and target == 0):
            multiplier = 1.2
        
        # disadvantage
            # just reverse
        elif(attacker == 4 and target == 3):
            multiplier = 0.8

        elif(attacker == 1 and target == 4):
            multiplier = 0.8
        
        elif(attacker == 2 and target == 0):
            multiplier = 0.8
        
        elif(attacker == 3 and target == 2):
            multiplier = 0.8
        
        elif(attacker == 0 and target == 1):
            multiplier = 0.8
        
        # if not found
        else:
            pass

        # modify the type advantage
        self.type_bonus = multiplier

        return(multiplier)

    async def physical_damage(self, roll_damage, dodgable = False, critable = False, ignore_defense = False):
        """
        `coroutine`

        Calculates the physical damages done to the target.

        - Parameter :

        `roll_damage` : Represents the generated damages.
        
        `ignore_defense`[Optional] : Default False, ignore the defense of the target or not.

        --

        Return : dict
        - calculated (int)
        - dodge (bool)
        - critical (bool)
        """

        # init
        await self.get_type_advantage()

        # roll to check if the target has dodged
        # if the target has dodged, return the dict 
        # with no calculated dmg
        if(dodgable):
            roll_dodge = uniform(0, 100)
            if(roll_dodge <= self.target.defense.dodge):
                # dodged
                self.damage["dodge"] = True
        
        # not dodged
        if(self.damage["dodge"] == False):
            # roll the crit
            if(critable):
                roll_crit = uniform(0, 100)
                if(roll_crit <= self.attacker.critical_chance):
                    # crit
                    self.damage["critical"] = True
                    self.critical_bonus = 1.5 + (self.attacker.critical_bonus)/100
        
            if(ignore_defense == False):
                self.damage["calculated"] = (roll_damage) * self.type_bonus * self.damage_reduction * self.armor * self.critical_bonus
            
            else:  # ignore the armor
                self.damage["calculated"] = (roll_damage) * self.type_bonus * self.damage_reduction * self.critical_bonus
            
            self.damage["calculated"] = int(self.damage["calculated"])
            
        return(self.damage)
    
    async def ki_damage(self, roll_damage, dodgable = False, critable = False, ignore_defense = False):
        """
        `coroutine`

        Calculates the ki damages done to the target.

        - Parameter :

        `roll_damage` : Represents the generated damages.
        
        `ignore_defense`[Optional] : Default False, ignore the defense of the target or not.

        --

        Return : dict
        - calculated (int)
        - dodge (bool)
        - critical (bool)
        """

        # roll to check if the target has dodged
        # if the target has dodged, return the dict 
        # with no calculated dmg
        if(dodgable):
            roll_dodge = uniform(0, 100)
            if(roll_dodge <= self.target.defense.dodge):
                # dodged
                self.damage["dodge"] = True
        
        # not dodged
        if(self.damage["dodge"] == False):
            # roll the crit
            if(critable):
                roll_crit = uniform(0, 100)
                if(roll_crit <= self.attacker.critical_chance):
                    # crit
                    self.damage["critical"] = True
                    self.critical_bonus = 1.5 + (self.attacker.critical_bonus)/100
        
            if(ignore_defense == False):
                self.damage["calculated"] = (roll_damage) * self.type_bonus * self.damage_reduction * self.spirit * self.critical_bonus
            
            else:  # ignore the spirit
                self.damage["calculated"] = (roll_damage) * self.type_bonus * self.damage_reduction * self.critical_bonus
            
            self.damage["calculated"] = int(self.damage["calculated"])
            
        return(self.damage)
"""
Manages the damage calculator.

--

Author : DrLarck

Last update : 21/07/19 (DrLarck)
"""

# dependancies
import asyncio
from random import uniform

# damage calculator
class Damage_calculator:
    """
    Manages the damage calculation.

    - Parameter : 

    - Attribute :

    - Method :
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
    async def physical_damage(self, roll_damage, ignore_defense = False):
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

        # roll to check if the target has dodged
        # if the target has dodged, return the dict 
        # with no calculated dmg
        roll_dodge = uniform(0, 100)
        if(roll_dodge <= self.target.defense.dodge):
            # dodged
            self.damage["dodge"] = True
        
        # not dodged
        if(self.damage["dodge"] == False):
            # roll the crit
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
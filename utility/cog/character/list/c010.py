"""
Represents Launch

--

Author : Zyorhist

Last update : 30/01/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_010(Character):
    """
    Represents the Launch unit from the General Blue saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Launch"
        self.info.id = 10
        self.info.saga = "General Blue"

        # stat
        self.health.maximum = 2000
        
        self.damage.physical_max = 625
        self.damage.ki_max = 700

        self.defense.armor = 475
        self.defense.spirit = 400
        self.defense.dodge = 3

        self.critical_chance = 35
        self.regeneration.ki = 3
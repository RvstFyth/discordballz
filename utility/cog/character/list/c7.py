"""
Represents Buu

--

Author : DrLarck

Last update : 25/01/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_7(Character):
    """
    Represents the Buu unit from the Buu saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Buu"
        self.info.id = 7
        self.info.saga = "Buu"

        # stat
        self.health = 1625
        
        self.damage.physical_max = 475
        self.damage.ki_max = 1000

        self.defense.armor = 400
        self.defense.spirit = 550
        self.defense.dodge = 0

        self.critical_chance = 0
        self.regeneration.ki = 4
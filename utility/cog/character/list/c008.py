"""
Represents Goten

--

Author : Zyorhist

Last update : 30/01/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_008(Character):
    """
    Represents the Goten unit from the Buu saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Goten"
        self.info.id = 8
        self.info.saga = "Buu"

        # stat
        self.health.maximum = 1250
        
        self.damage.physical_max = 550
        self.damage.ki_max = 1000

        self.defense.armor = 550
        self.defense.spirit = 400
        self.defense.dodge = 15

        self.critical_chance = 0
        self.regeneration.ki = 4
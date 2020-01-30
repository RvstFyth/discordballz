"""
Represents Turles

--

Author : Zyorhist

Last update : 30/01/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_009(Character):
    """
    Represents the Turles unit from the Tree of Might saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Turles"
        self.info.id = 9
        self.info.saga = "Tree of Might"

        # stat
        self.health.maximum = 3675
        
        self.damage.physical_max = 550
        self.damage.ki_max = 725

        self.defense.armor = 550
        self.defense.spirit = 400
        self.defense.dodge = 10

        self.critical_chance = 10
        self.regeneration.ki = 2
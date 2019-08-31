"""
Manages the character 5
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

# Piccolo
class Character_5(Character):
    """
    Represents Picolo
    """

    def __init__(self):
        # inheritance
        Character.__init__(self)

        # info
        self.info.id = 5
        self.info.name = "Piccolo"
        self.info.saga = "Saiyan"
        self.rarity.value = 0

        # image
        self.image.image = "https://imgur.com/pCv2cyO"

        # stat
        # health
        self.health.maximum = 3875
        
        # damage 
        self.damage.physical_max = 325
        self.damage.ki_max = 400

        # defense
        self.defense.armor = 625
        self.defense.spirit = 625
        self.defense.dodge = 10

        # crit
        self.critical_chance = 10
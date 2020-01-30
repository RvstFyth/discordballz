"""
Represents the character 6

--

Author : DrLarck

Last update : 06/09/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

# test
from utility.cog.character.ability.list.acid import Acid

# Bardock
class Character_006(Character):
    """
    Represents Bardock
    """

    def __init__(self):
        # inheritance
        Character.__init__(self)

        # info
        self.info.id = 6
        self.info.name = "Bardock"
        self.info.saga = "Bardock"
        self.rarity.value = 0

        # image
        self.image.image = "https://i.imgur.com/FWJSzJb.png"
        self.image.thumb = "https://i.imgur.com/60PB1UY.png"
        self.image.icon = "<:bardock:619492509864820737>"
        
        # stat
        # health
        self.health.maximum = 3500
        
        # damage
        self.damage.physical_max = 475
        self.damage.ki_max = 325

        # defense
        self.defense.armor = 700
        self.defense.spirit = 550
        self.defense.dodge = 10

        # crit
        self.critical_chance = 15

        self.ability = [Acid]
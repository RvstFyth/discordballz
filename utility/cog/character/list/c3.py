"""
Manages the character 3
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

# Red Saibaiman
class Character_3(Character):
    """
    Represents a Red Saibaiman
    """

    def __init__(self):
        # inheritance
        Character.__init__(self)

        # info
        self.info.id = 3
        self.info.name = "Red Saibaiman"
        self.info.saga = "Saiyan"
        self.rarity.value = 0

        # image
        self.image.image = "https://i.imgur.com/mIIt7jL.png"
        self.image.thumb = "https://i.imgur.com/LEjhrtw.png"
        self.image.icon = "<:saibaiman_c:589492379447197699>"

        # stat
        # health
        self.health.maximum = 1625
        self.health.current = 1625

        # damage
        self.damage.physical_max = 475
        self.damage.ki_max = 550

        # defense
        self.defense.armor = 625
        self.defense.spirit = 475
        self.defense.dodge = 10

        # crit
        self.critical_chance = 10
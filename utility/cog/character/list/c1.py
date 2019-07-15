"""
Manages the character 1

--

Author : DrLarck

Last update : 15/07/19
"""

# dependancies
import asyncio

# utils
from utility.cog.character.character import Character

# saibaiman
class Character_1(Character):
    """
    Represents a Green Saibaiman.
    """

    def __init__(self):
        # inheritance
        Character.__init__(self)

        # characteristics
            # infos
        self.info["id"] = 1
        self.info["name"] = "Green Saibaiman"
        self.info["saga"] = "Saiyan"
        self.info["rarity"]["value"] = 0 

            # health
        self.health["maximum"] = 3500
        self.health["current"] = 3500

            # damage
        self.damage["physical"]["maximum"] = 400
        self.damage["physical"]["minimum"] = 360
        self.damage["ki"]["maximum"] = 850
        self.damage["ki"]["minimum"] = 765

            # defense
        self.defense["armor"] = 475
        self.defense["spirit"] = 400
        self.defense["dodge"] = 10

            # critical
        self.critical["chance"] = 10
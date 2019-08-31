"""
Represents the character 6
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

# Bardock
class Character_6(Character):
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
        self.image.image = ""
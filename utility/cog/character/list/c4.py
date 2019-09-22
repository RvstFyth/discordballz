"""
Manages the character 4

--

Author : DrLarck

Last update : 22/09/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

# test
from utility.cog.character.ability.list.rolling_smash import Rolling_smash

# Pilaf Machine
class Character_4(Character):
    """
    Represents Pilaf Machine
    """

    def __init__(self):
        # inheritance
        Character.__init__(self)

        # info
        self.info.id = 4
        self.info.name = "Pilaf Machine"
        self.info.saga = "Emperor Pilaf"
        self.rarity.value = 0

        # image
        self.image.image = "https://i.imgur.com/j4V5Qxm.png"
        self.image.thumb = "https://i.imgur.com/tt2Aoh0.png"
        self.image.icon = "<:pilaf_machine:619492931920723980>"
        
        # stat
        # health
        self.health.maximum = 3875
        self.health.current = 3875

        # ki
        # this unit doesn't have ki
        self.ki.maximum = 0

        # damage
        self.damage.physical_max = 400
        self.damage.ki_max = 250

        # defense
        self.defense.armor = 700
        self.defense.spirit = 625
        self.defense.dodge = 15

        # crit
        self.critical_chance = 10

        self.ability = [Rolling_smash]
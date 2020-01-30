"""
Manages the character 5

--

Author : DrLarck

Last update : 30/01/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

# ability
from utility.cog.character.ability.list.arm_stretch import Arm_stretch
from utility.cog.character.ability.list.special_beam_cannon import Special_beam_cannon

# Piccolo
class Character_005(Character):
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
        self.image.image = "https://i.imgur.com/pCv2cyO.png"
        self.image.thumb = "https://i.imgur.com/kDoU9ZH.png"
        self.image.icon = "<:piccolo:619492513673248778>"

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

        self.ability = [Arm_stretch, Special_beam_cannon]
"""
Manages the character 1

--

Author : DrLarck

Last update : 29/09/19 (DrLarck)
"""

# dependancies
import asyncio

# utils
from utility.cog.character.character import Character

# abilities
from utility.cog.character.ability.list.acid import Acid
from utility.cog.character.ability.list.syphon import Syphon
from utility.cog.character.ability.list.unity_is_strength import Unity_is_strength

# passive
from utility.cog.character.ability.passive.saibaiman_green import Passive_green_saibaiman
from utility.cog.character.ability.leader.saibaiman_green import Leader_green_saibaiman

# saibaiman
class Character_001(Character):
    """
    Represents a Green Saibaiman.
    """

    def __init__(self):
        # inheritance
        Character.__init__(self)

        # characteristics
            # infos
        self.info.id = 1
        self.info.name = "Green Saibaiman"
        self.info.saga = "Saiyan"

            # image
        self.image.icon = "<:saibaiman_a:589485375685263373>"
        self.image.image = "https://i.imgur.com/1m8rA7L.png"
        self.image.thumb = "https://i.imgur.com/SITD9VY.png"

        self.rarity.value = 0

            # health
        self.health.maximum = 3500

            # damage
        self.damage.physical_max = 400
        self.damage.physical_min = 360
        self.damage.ki_max = 850
        self.damage.ki_min = 765

            # defense
        self.defense.armor = 475
        self.defense.spirit = 400
        self.defense.dodge = 10

            # critical
        self.critical_chance = 10
        
            # ki gain
        self.regeneration.ki = 3

        # ability
        self.ability = [Acid, Syphon, Unity_is_strength]
        self.passive = [Passive_green_saibaiman]
        self.leader = [Leader_green_saibaiman]

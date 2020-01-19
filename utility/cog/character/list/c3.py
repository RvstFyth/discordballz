"""
Manages the character 3

--

Author : DrLarck

Last update : 24/11/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

# test
from utility.cog.character.ability.list.acid import Acid
from utility.cog.character.ability.list.spreading_acid import Spreading_acid
from utility.cog.character.ability.list.paralyzing_burns import Paralyzing_burns

from utility.cog.character.ability.passive.saibaiman_red import Passive_red_saibaiman
from utility.cog.character.ability.leader.saibaiman_red import Leader_saibaiman_red

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
        
        #ki regeneration
        self.regeneration.ki = 4

        # ability
        self.ability = [Acid, Spreading_acid, Paralyzing_burns]
        self.leader = [Leader_saibaiman_red]
        self.passive = [Passive_red_saibaiman]

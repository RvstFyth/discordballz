"""
Represents the character 2

--

Author : DrLarck

Last update : 18/10/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

# test
from utility.cog.character.ability.list.acid import Acid
from utility.cog.character.ability.list.acid_explosion import Acid_explosion

from utility.cog.character.ability.leader.saibaiman_blue import Leader_blue_saibaiman
from utility.cog.character.ability.effect.buff.saibaiman_last_will_acid import Buff_last_will_acid

# blue saibaiman
class Character_2(Character):
    """
    Represents a Blue Saibaiman
    """

    def __init__(self):
        # inheritance
        Character.__init__(self)

        # stats
        self.info.id = 2
        self.info.name = "Blue Saibaiman"
        self.info.saga = "Saiyan"
        self.rarity.value = 0

        # image
        self.image.icon = "<:saibaiman_b:589492373130706964>"
        self.image.image = "https://i.imgur.com/syjNBd2.png"
        self.image.thumb = "https://i.imgur.com/wcKoXiB.png"

        # health
        self.health.maximum = 4250
        self.health.current = 4250

        # damage
        self.damage.physical_max = 250
        self.damage.ki_max = 400

        # def
        self.defense.armor = 700
        self.defense.spirit = 625
        self.defense.dodge = 20

        # crit
        self.critical_chance = 10
        
        #ki regeneration
        self.regeneration.ki = 2

        # ability
        self.ability = [Acid, Acid_explosion]
        self.passive = [Buff_last_will_acid]
        self.leader = [Leader_blue_saibaiman]

"""
Represents the mission n°1

--

Author : DrLarck

Last update : 02/02/20 (DrLarck)
"""

# dependancies
import asyncio
import random

# util
from utility.cog.mission.mission import Mission

# opponent
from utility.cog.character.list.c001 import Character_001
from utility.cog.character.list.c002 import Character_002
from utility.cog.character.list.c003 import Character_003

class Mission_1(Mission):
    """
    Opponent : Team of Saibaiman

    Reward :

    - dragonstone 10

    - zenis 100

    - team xp 150

    Level : [5, 10]
    """

    # attribute
    def __init__(self):
        Mission.__init__(self)
        self.level_range = {
            "min" : 5,
            "max" : 10
        }

    async def set_opponent(self):
        
        # init
        self.opponent = [
            Character_001(),
            Character_002(),
            Character_003()
        ]

        # set the level
        for character in self.opponent:
            await asyncio.sleep(0)

            rand_level = random.randint(self.level_range["min"], self.level_range["max"])

            character.level = rand_level

        return(self.opponent)
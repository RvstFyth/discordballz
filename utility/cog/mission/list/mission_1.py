"""
Represents the mission n°1

--

Author : DrLarck

Last update : 02/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.mission.mission import Mission

# opponent
from utility.cog.character.list.c001 import Character_001

class Mission_1(Mission):
    """
    Test
    """

    # attribute
    def __init__(self):
        Mission.__init__(self)

    async def set_opponent(self):
        opponent = Character_001()

        opponent.level = 150

        self.opponent.append(opponent)

        return(self.opponent)
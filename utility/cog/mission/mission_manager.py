"""
Mission system

--

Author : DrLarck

Last update : 02/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.fight_system.fight import Fight

class Mission_manager():
    """
    Manages the mission feature by launching a mission, managing the rewards, storing the missions etc.

    - Attribute

    `mission` (`list`) : List the `Mission()` objects (list of missions)
    """

    # attribute
    def __init__(self):
        self.missions = []
    
    # method
    async def start_mission(self, ctx, client, player, mission_id = 0):
        """
        Start a mission

        - Parameter : 

        `ctx` (`discord.ext.commands.context`)

        `client` (`discord.ext.commands.Bot`)

        `player` (`Player()`)

        `mission_id` (`int`) : The mission to start (stored in `self.missions`)

        --

        Return : `bool` (`True` if the player has won the mission), `None` if mission Not found
        """

        # init
        success = False

        if(mission_id <= len(self.missions)):
            combat = Fight(client, ctx, player)
        
        else:
            return

        return(success)
"""
Mission system

--

Author : DrLarck

Last update : 02/02/20 (DrLarck)
"""

# dependancies
import asyncio

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
    async def start_mission(self, player, mission_id = 0):
        """
        Start a mission

        - Parameter : 

        `player` (`Player()`)

        `mission_id` (`int`) : The mission to start (stored in `self.missions`)

        --

        Return : `bool` (`True` if the player has won the mission), `None` if mission Not found
        """

        # init
        success = False

        if(mission_id <= len(self.missions)):
            pass
        
        else:
            return

        return(success)
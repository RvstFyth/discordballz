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

# mission
from utility.cog.mission.list.mission_1 import Mission_1

class Mission_manager():
    """
    Manages the mission feature by launching a mission, managing the rewards, storing the missions etc.

    - Attribute

    `mission` (`list`) : List the `Mission()` objects (list of missions)
    """

    # attribute
    def __init__(self):
        self.missions = [Mission_1()]
    
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
        mission_id -= 1

        if(mission_id < len(self.missions)):
            # init the combat system
            combat = Fight(client, ctx, player)
            mission = self.missions[mission_id]

            await mission.init()

            # get the player's team
            player_team = await player.character()
            opponent_team = mission.opponent

            if(len(opponent_team) > 0 and len(player_team) > 0):
                teams = [player_team, opponent_team]

                winner = await combat.run_fight(teams)
        
        else:
            return

        return(success)
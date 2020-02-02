"""
Mission system

--

Author : DrLarck

Last update : 02/02/20 (DrLarck)
"""

# dependancies
import asyncio

# graphic
from configuration.icon import game_icon

# util
from utility.cog.fight_system.fight import Fight
from utility.cog.level.level import Leveller

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
        leveller = Leveller(client, ctx)

        # limit
        if(mission_id < 0):
            mission_id = 0

        if(mission_id <= len(self.missions) and mission_id > 0):
            mission_id -= 1  # get the index

            # init the combat system
            combat = Fight(client, ctx, player)
            mission = self.missions[mission_id]

            await mission.init()

            # get the player's team
            player_team = await player.team.character()
            opponent_team = mission.opponent

            if(len(opponent_team) > 0 and len(player_team) > 0):
                teams = [player_team, opponent_team]

                winner = await combat.run_fight(teams)

                # if the player won
                if(winner == 1):
                    # get the unique id of the player's characters
                    player_team_id = await player.team.get_team()

                    player_team_id = [
                        player_team_id["a"], player_team_id["b"], player_team_id["c"]
                    ]

                    await leveller.team_add_xp(player, player_team_id, mission.reward["team_xp"])

                    # give player the resources he has won
                    await player.resource.add_dragonstone(mission.reward["dragonstone"])
                    await player.resource.add_zenis(mission.reward["zenis"])

                    # message
                    await ctx.send(f"Congratulations ! You have earned **{mission.reward['dragonstone']:,}**{game_icon['dragonstone']} as well as **{mission.reward['zenis']:,}**{game_icon['zenis']}")

        else:
            return

        return(success)
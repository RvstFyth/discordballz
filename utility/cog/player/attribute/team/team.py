"""
Represents the player's team.

--

Author : DrLarck

Last update : 29/08/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.database.database_manager import Database

# player's team
class Team:
    """
    Represents and manages the player's team.

    - Parameter :

    `client` : Represents a `discord.Client`. This client must handle a connection pool to the database.

    `player` : Represents a `Player`.

    - Attribute :

    `team` : dict - Represents the player's team ["a", "b", "c"]. None if the slot is not defined.
    """

    # attribute
    def __init__(self, client, player):
        # basic
        self.client = client
        self.player = player
        self.db = Database(self.client.db)

        # team
        self.team = {
            "a" : None,
            "b" : None,
            "c" : None
        }

    # method
    async def get_team(self):
        """
        `coroutine`

        Get the player's team.

        --

        Return : dict
        """

        self.team["a"] = await self.db.fetchval(
            f"""
            SELECT player_fighter_a FROM player_combat_info WHERE player_id = {self.player.id};
            """
        )

        self.team["b"] = await self.db.fetchval(
            f"""
            SELECT player_fighter_b FROM player_combat_info WHERE player_id = {self.player.id};
            """
        )

        self.team["c"] = await self.db.fetchval(
            f"""
            SELECT player_fighter_c FROM player_combat_info WHERE player_id = {self.player.id};
            """
        )

        # last setup
        if(self.team["a"] == "NONE"):
            self.team["a"] = None
        
        if(self.team["b"] == "NONE"):
            self.team["b"] = None
        
        if(self.team["b"] == "NONE"):
            self.team["b"] = None

        return(self.team)
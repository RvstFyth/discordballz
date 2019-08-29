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
from utility.cog.character.getter import Character_getter

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
    async def update_team(self):
        """
        `coroutine`

        Updates the player's team infos.

        --

        Return : None
        """
        
        await self.db.execute(
            f"""
            UPDATE SET player_combat_info SET player_fighter_a = {self.team['a']} WHERE player_id = {self.player.id};
            UPDATE SET player_combat_info SET player_fighter_b = {self.team['b']} WHERE player_id = {self.player.id};
            UPDATE SET player_combat_info SET player_fighter_c = {self.team['c']} WHERE player_id = {self.player.id};
            """
        )

        return

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
    
    async def set_fighter(self, slot, character_unique):
        """
        `coroutine`

        Set a fighter at the passed slot with the specified unique id.

        - Parameter :

        `slot` : str - Represents the slot to set ("a", "b", "c").

        `character_unique` : str - Represents the unique id of the character to set at the slot.

        --

        Return : None
        """

        # The player cannot have copy of a same character in his team
        # we get the character's global id and we compare it with the 
        # other team members

        # init
        team = {
            "a" : None,
            "b" : None,
            "c" : None
        }
        team_id = []
        in_team = False

        # remove the slot
        await self.remove(slot)
        
        getter = Character_getter()
        await self.get_team()

        # get the team ids
        if(self.team["a"] != None):
            team["a"] = await getter.get_from_unique(self.client, self.team["a"])
            team_id.append(team["a"].info.id)
        
        if(self.team["b"] != None):
            team["b"] = await getter.get_from_unique(self.client, self.team["b"])
            team_id.append(team["b"].info.id)
        
        if(self.team["c"] != None):
            team["c"] = await getter.get_from_unique(self.client, self.team["c"])
            team_id.append(team["c"].info.id)
        
        # now get the id of the fighter the player wants to set
        character = await getter.get_from_unique(self.client, character_unique)

        # check if the character is in the team
        if character.info.id in team_id:
            in_team = True
        
        # if the character isn't in the team, add it to it
        self.team[slot] = character_unique
        await self.update_team()

        return
    
    async def remove(self, slot):
        """
        `coroutine`

        Reset a character slot.

        - Parameter :

        `slot` : str - Represents the slot to reset ("a", "b", "c")

        --

        Return : None
        """

        await self.db.execute(
            f"""
            UPDATE player_combat_info SET player_fighter_{slot} = 'NONE'
            WHERE player_id = {self.player.id};
            """
        )

        return
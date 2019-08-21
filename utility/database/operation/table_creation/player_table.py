"""
Manages the creation of the player table.

--

Author : DrLarck

Last update : 21/08/19 (DrLarck)
"""

# dependancies
import asyncio

# utils
from utility.database.operation.database_table import Table_creator

class Player_table_creator:
    """
    Creates the players table

    - Parameter :

    `client` : Represents a `discord.Client`. The discord client must contain a database pool.

    - Method :

    :coro:`create_player_info()` : Returns the characteristics of the player_info table.

    :coro:`create_player_combat_info()` : Same as `create_player_info()` but for player_combat_info table.

    :coro:`create_player_resource()` : Return the player_resource table characteristics.
    """

    # attribute
    def __init__(self, client):
        self.client = client
        self.creator = Table_creator(self.client)
        self.creator.tables = [
            self.create_player_info,
            self.create_player_combat_info,
            self.create_player_resource
        ]

    # method
    async def create_player_info(self):
        """
        `coroutine`

        Creates the table player_info.

        - Parameter : 

        `client` : Represents a `discord.Client`.

        --

        Return : dict i.e self.get_creation_pattern
        """

        # init
        player_info = await self.creator.get_creation_pattern()

        player_info["name"] = "player_info"
        player_info["need_ref"] = True

        # attribute
        player_id = {
            "name" : "player_id",
            "type" : "BIGINT",
            "default" : None
        }

        player_name = {
            "name" : "player_name",
            "type" : "TEXT",
            "default" : None
        }

        player_register_date = {
            "name" : "player_register_date",
            "type" : "TEXT",
            "default" : None
        }

        player_lang = {
            "name" : "player_lang",
            "type" : "TEXT",
            "default" : "EN"
        }

        player_location = {
            "name" : "player_location",
            "type" : "TEXT",
            "default" : "UNKNOWN"
        }

            # add the attribute
        player_info["attribute"] = [
            player_id, player_name, player_register_date, player_lang, player_location
        ]

        # unique index
        player_info["unique_index"] = [
            player_id["name"]
        ]

        return(player_info)

    async def create_player_combat_info(self):
        """
        `coroutine`

        Creates the player_combat_info table.
        
        --

        Return : dict
        """

        # init
        player_combat = await self.creator.get_creation_pattern()

        player_combat["name"] = "player_combat_info"
        
        # attribute
        player_id = {
            "name" : "player_id",
            "type" : "BIGINT",
            "default" : None
        }

        player_name = {
            "name" : "player_name",
            "type" : "TEXT",
            "default" : None
        }

        player_leader = {
            "name" : "player_leader",
            "type" : "TEXT",
            "default" : "NONE"
        }

        fighter_a = {
            "name" : "player_fighter_a",
            "type" : "TEXT",
            "default" : "NONE"
        }

        fighter_b = {
            "name" : "player_fighter_b",
            "type" : "TEXT",
            "default" : "NONE"
        }

        fighter_c = {
            "name" : "player_fighter_c",
            "type" : "TEXT",
            "default" : "NONE"
        }

        player_combat["attribute"] = [
            player_id,
            player_name,
            player_leader,
            fighter_a,
            fighter_b,
            fighter_c
        ]

        # unique index
        player_combat["unique_index"] = [
            player_id["name"]
        ]

        return(player_combat)
    
    async def create_player_resource(self):
        """
        `coroutine`

        Create the player_resource table.

        --

        Return : dict
        """

        # init 
        resource = await self.creator.get_creation_pattern()
        resource["name"] = "player_resource"
        resource["need_ref"] = True

        # attribute
        id = {
            "name" : "player_id",
            "type" : "BIGINT",
            "default" : None
        }

        name = {
            "name" : "player_name",
            "type" : "TEXT",
            "default" : None
        }

        dragonstone = {
            "name" : "player_dragonstone",
            "type" : "BIGINT",
            "default" : 0
        }

        zenis = {
            "name" : "player_zenis",
            "type" : "BIGINT",
            "default" : 0
        }

        # add attr
        resource["attribute"] = [
            id,
            name,
            zenis,
            dragonstone
        ]

        # unique index
        resource["unique_index"] = [
            id["name"]
        ]

        return(resource)
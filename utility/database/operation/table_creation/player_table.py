"""
Manages the creation of the player table.

--

Author : DrLarck

Last update : 20/08/19 (DrLarck)
"""

# dependancies
import asyncio

# utils
from utility.database.operation.database_table import Table_creator

# player table creation
async def create_player_info(client):
    """
    `coroutine`

    Creates the table player_info.

    - Parameter : 

    `client` : Represents a `discord.Client`.

    --

    Return : dict i.e self.get_creation_pattern
    """

    # init
    creator = Table_creator(client)
    player_info = await creator.get_creation_pattern()

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

# get the functions
player_table = [
    create_player_info
]
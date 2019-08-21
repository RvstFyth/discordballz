"""
Manages the character tables.

--

Author : DrLarck

Last update : 21/08/19 (DrLarck)
"""

# dependancies
import asyncio

# utils
from utility.database.operation.database_table import Table_creator

# character tables
class Character_table_creator:
    """
    Creates the character tables.

    - Parameter :

    `client` : Represents a `discord.Client`. The client must have a databse connection pool (i.e Databse().init())

    - Method :


    """

    # attribute
    def __init__(self, client):
        self.client = client
        self.creator = Table_creator(self.client)
        self.creator.tables = [
            self.create_character_unique
        ]
    
    # method
    async def create_character_unique(self):
        """
        `coroutine`

        Returns the character_unique table characteristics.

        --

        Return : dict
        """

        # init
        char_unique = await self.creator.get_creation_pattern()

        char_unique["name"] = "character_unique"
        char_unique["need_ref"] = True

        # attribiute
        owner_id = {
            "name" : "character_owner_id",
            "type" : "BIGINT",
            "default" : None
        }

        owner_name = {
            "name" : "character_owner_name",
            "type" : "TEXT",
            "default" : "NONE"
        }

        unique_id = {
            "name" : "character_unique_id",
            "type" : "TEXT",
            "default" : "NONE"
        }

        global_id = {
            "name" : "character_global_id",
            "type" : "BIGINT",
            "default" : None
        }

        char_type = {
            "name" : "character_type",
            "type" : "INTEGER",
            "default" : 0
        }

        char_rarity = {
            "name" : "character_rarity",
            "type" : "INTEGER",
            "default" : 0
        }

        char_level = {
            "name" : "character_level",
            "type" : "BIGINT",
            "default" : 1
        }

        char_exp = {
            "name" : "character_experience",
            "type" : "BIGINT",
            "default" : 0
        }

        char_star = {
            "name" : "character_star",
            "type" : "INTEGER",
            "default" : 0
        }

        char_health = {
            "name" : "character_training_health",
            "type" : "INTEGER",
            "default" : 0
        }

        char_armor = {
            "name" : "character_training_armor",
            "type" : "INTEGER",
            "default" : 0
        }

        char_spirit = {
            "name" : "character_training_spirit",
            "type" : "INTEGER",
            "default" : 0
        }

        char_physical = {
            "name" : "character_training_physical",
            "type" : "INTEGER",
            "default" : 0
        }

        char_ki = {
            "name" : "character_training_ki",
            "type" : "INTEGER",
            "default" : 0
        }

        # add the attr
        char_unique["attribute"] = [
            owner_id,
            owner_name,
            unique_id,
            global_id,
            char_type,
            char_rarity,
            char_level,
            char_exp,
            char_star,
            char_health,
            char_armor,
            char_spirit,
            char_physical,
            char_ki
        ]

        return(char_unique)
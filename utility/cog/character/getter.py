"""
Manages the character getter.

--

Author : DrLarck

Last update : 22/08/19 (DrLarck)
"""

# dependancies
import asyncio

# database
from utility.database.database_manager import Database

# getter
class Character_getter:
    """
    Manages the character getters.

    - Attribute :

    `character_list` : List of all the characters existing in the game.

    `special_character` : List of non-summonable characters.

    - Method : 

    :coro:`get_character(character_id)` : Returns an instance of a character. The character id must be type int. Return None if not found.

    :coro:`get_summonable()` : Returns the list of summonable characters (id).

    :coro:`get_from_unique(unique_id)` : Get a character instance from its unique id
    """

    # attribute
    def __init__(self):
        # non-summonable characters
        self.special_character = []

        # list of all the characters in the game
        self.character_list = [
            1
        ]

    # method
    async def get_character(self, character_id):
        """
        `coroutine`

        Get a character instance according to the passed id.

        --

        Return : Character instance, otherwise : None
        """

        # init
        character = None

        if(character_id == 1):  # Green Saibaiman
            from utility.cog.character.list.c1 import Character_1

            character = Character_1()

        return(character)
    
    async def get_summonable(self):
        """
        `coroutine`

        Get the list of summonable characters. Remove the special characters.

        --

        Return : list of summonable characters
        """

        # init
        summonable = self.character_list

        for character in summonable:
            await asyncio.sleep(0)

            if character in self.special_character:  # if the character is a special one
                summonable.remove(character)
            
            else:
                pass

        return(summonable)
    
    async def get_from_unique(self, client, unique_id):
        """
        `coroutine`

        Get a character instance from its unique id.

        - Parameter : 

        `client` : Represents a `discord.Client`. The client must contain a connection pool to the database.

        `unique_id` : str - Represents the character's unique id to look for.

        --

        Return : character instance. None if not found.
        """

        # init
        db = Database(client.db)
        character = None
        get_father = await db.fetchval(
            f"SELECT character_global_id FROM character_unique WHERE character_unique_id = '{unique_id}';"
        )

        # get the character instance
        character = await self.get_character(get_father)

        return(character)
    
    async def get_character_stat(self, client, unique_id):
        """
        `coroutine`

        Returns a character instance with the stats from the db

        --

        Return : new character instance with the correct stats.
        """
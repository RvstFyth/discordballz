"""
Manages the character getter.

--

Author : DrLarck

Last update : 30/01/20 (DrLarck)
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

        # Green Saibaiman
        if(character_id == 1):
            from utility.cog.character.list.c001 import Character_001

            character = Character_001()
        
        # Blue Saibaiman
        if(character_id == 2):
            from utility.cog.character.list.c002 import Character_002

            character = Character_002()
        
        # Red Saibaiman
        if(character_id == 3):
            from utility.cog.character.list.c003 import Character_003

            character = Character_003()
        
        # Pilaf Machine
        if(character_id == 4):
            from utility.cog.character.list.c004 import Character_004

            character = Character_004()
        
        # Piccolo
        if(character_id == 5):
            from utility.cog.character.list.c005 import Character_005

            character = Character_005()

        # Bardock
        if(character_id == 6):
            from utility.cog.character.list.c006 import Character_006

            character = Character_006()
        
        if(character_id == 7):
            from utility.cog.character.list.c007 import Character_007

            character = Character_007()
        
        if(character_id == 8):
            from utility.cog.character.list.c008 import Character_008

            character = Character_008()
        
        if(character_id == 9):
            from utility.cog.character.list.c009 import Character_009

            character = Character_009()
        
        if(character_id == 7):
            from utility.cog.character.list.c010 import Character_010

            character = Character_010()
                    
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
        char_father = await db.fetch(
            f"SELECT * FROM character_unique WHERE character_unique_id = '{unique_id}';"
        )

        if(len(char_father) > 0):
            # sort the data
            char_id = char_father[0][4]
            char_type = char_father[0][5]
            char_rarity = char_father[0][6]
            char_level = char_father[0][7]
            char_star = char_father[0][9]
            char_training = {
                "health" : char_father[0][10],
                "armor" : char_father[0][11],
                "spirit" : char_father[0][12],
                "physical" : char_father[0][13],
                "ki" : char_father[0][14]
            }

            # get the character instance
            character = await self.get_character(char_id)

            # set the character's stats
            character.type.value = char_type
            character.rarity.value = char_rarity
            character.level = char_level
            
                # training items
            character.enhancement["star"] = char_star
            character.enhancement["training"]["defense"]["health"] = char_training["health"]
            character.enhancement["training"]["defense"]["armor"] = char_training["armor"]
            character.enhancement["training"]["defense"]["armor"] = char_training["spirit"]
            character.enhancement["training"]["damage"]["physical"] = char_training["physical"]
            character.enhancement["training"]["damage"]["ki"] = char_training["ki"]

            # init the object
            await character.init()

        return(character)
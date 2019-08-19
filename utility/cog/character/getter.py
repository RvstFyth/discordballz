"""
Manages the character getter.

--

Author : DrLarck

Last update : 19/08/19 (DrLarck)
"""

# dependancies
import asyncio

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
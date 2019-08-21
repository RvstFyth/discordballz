"""
Manages all the summon tools.

-- 

Authod : DrLarck

Last update : 21/08/19 (DrLarck)
"""

# dependancies
import asyncio
from string import ascii_letters

# util
from utility.database.database_manager import Database
from utility.cog.character.getter import Character_getter
from utility.cog.banner._sorted_banner import Sorted_banner

# summon tools
class Summoner:
    """
    Manages all the utilities for the summon feature.
    
    - Parameter :

    `client` : Represents a `discord.Client`. The client must contain a database pool (i.e Database.init())
    """

    # attribute
    def __init__(self, client):
        self.db = Database(client.db)
        self.sorted = None

    # method
    async def sort(self, character_list, banner = None):
        """
        `coroutine`

        Sort the character contained in `character_list`.

        - Parameter : 

        `character_list` : A list of characters (global id) to sort

        `banner` : Banner name : "basic", "expansion", "muscle

        --

        Return : dict 

        - Key

        LIST OF GLOBAL ID
        `n` : list - The normal characters.

        `r` : list - The rare characters.

        `sr` : list - The super rare characters.

        `ssr` : list - The super super rare characters.

        `ur` : list - The ultra rare characters.

        `lr` : list - The legendary characters.
        """

        # init
        if(banner == None):
            banner = "basic"

        getter = Character_getter()
        self.sorted = {
            "n" : [],
            "r" : [],
            "sr" : [],
            "ssr" : [],
            "ur" : [],
            "lr" : []
        }
        characters = []

        # get characters' instance
        for character in character_list:
            await asyncio.sleep(0)

            _character = await getter.get_character(character)
            characters.append(_character)
        
        # now sort the characters
        for char in characters:
            await asyncio.sleep(0)

            if(char != None):  # getter return None if the character has not been found
                # get the rarity of the character
                rarity = char.rarity.value

                # sort it
                # append the global id of the character
                    # N
                if(rarity == 0):
                    self.sorted["n"].append(char.info.id)
                    
                    # R
                elif(rarity == 1):
                    self.sorted["r"].append(char.info.id)

                    # SR
                elif(rarity == 2):
                    self.sorted["sr"].append(char.info.id)

                    # SSR
                elif(rarity == 3):
                    self.sorted["ssr"].append(char.info.id)

                    # UR
                elif(rarity == 4):
                    self.sorted["ur"].append(char.info.id)

                    # LR
                elif(rarity == 5):
                    self.sorted["lr"].append(char.info.id)
        
        # storing the dict
        if(banner == "basic"):
            Sorted_banner.basic = self.sorted
        
        elif(banner == "expansion"):
            Sorted_banner.expansion = self.sorted
        
        elif(banner == "muscle"):
            Sorted_banner.muscle_tower = self.sorted

        # returns the dict
        return(self.sorted)
        
    async def generate_unique_id(self, reference) :
        """
        `coroutine`

        Generates a unique id according to the LLLLN form.

        - Parameter :

        `reference` : Represents an integer to convert into a unique id.

        --

        Return : unique id (str) form LLLLN
        """

        # init
        unique_id = ""

            # tiers
            # numerical value
        n, t1, t2, t3, t4 = 0, 0, 0, 0, 0

            # alphabetical value
        letter = ascii_letters

        # generation
            # storing the biggest value in n
        n = int(reference / pow(52, 4))
        reference -= n * pow(52, 4)  # substract as the lower tiers cannot handle a huge amount

            # now dispatching the value through the tiers
            # each tier can store 52^tier_index - 1 values
            # the lowest tier (1) can only store 52 values
        t4 = int(reference / pow(52, 3))
        reference -= t4 * pow(52, 3)

        t3 = int(reference / pow(52, 2))
        reference -= t3 * pow(52, 2)

        t2 = int(reference / 52)
        reference -= t2 * 52

        t1 = reference

        # get the unique id generated
        unique_id = f"{letter[t1]}{letter[t2]}{letter[t3]}{letter[t4]}{n}"

        return(unique_id)
    
    async def set_unique_id(self):
        """
        `coroutine`

        Set a unique id for all the characters stored in the database with 'NONE' as unique id value.

        --

        Return : None
        """

        # init
        characters = []
        query_fetch = "SELECT * FROM character_unique WHERE character_unique_id = 'NONE';"

        characters = await self.db.fetch(query_fetch)

        # now generate a unique id for the characters

        for character in range(len(characters)):
            await asyncio.sleep(0)
            
            # get the reference value
            reference = characters[character][0]
            unique_id = await self.generate_unique_id(reference)

            # query
            query_update = f"UPDATE character_unique SET character_unique_id = '{unique_id}' WHERE reference = {reference};"
            await self.db.execute(query_update)
        
        return
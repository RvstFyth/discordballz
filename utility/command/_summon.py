"""
Manages all the summon tools.

-- 

Authod : DrLarck

Last update : 20/08/19 (DrLarck)
"""

# dependancies
import asyncio
from string import ascii_letters

# util
from utility.database.database_manager import Database

# summon tools
class Summon:
    """
    Manages all the utilities for the summon feature.
    
    - Parameter :

    `client` : Represents a `discord.Client`. The client must contain a database pool (i.e Database.init())
    """

    # attribute
    def __init__(self, client):
        self.db = Database(client.db)

    # method
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
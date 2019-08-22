"""
Manages the background tasks

--

Authod : DrLarck

Last update : 22/08/19 (DrLarck)
"""

# dependacies
import asyncio

# utils
from utility.database.operation.database_table import Table_creator
    # database
from utility.database.operation.table_creation.player_table import Player_table_creator
from utility.database.operation.table_creation.character_table import Character_table_creator
    # summon
from utility.command._summon import Summoner
from utility.cog.banner._sorted_banner import Sorted_banner
from utility.cog.banner.basic import Basic_banner

# background 
class Background_manager:
    """
    Launches all the background tasks.

    - Parameter : 

    `client` : Represents a `discord.Client`. The client must contain a connection pool (i.e Database().init())

    - Method :

    :coro:`run_task()` : Launches all the background tasks.
    """

    # attribute
    def __init__(self, client):
        self.client = client
        self.client.loop.run_until_complete(self.run_task())
    
    # method
    async def run_task(self):
        """
        `coroutine`

        Launches all the background tasks.

        --

        Return : None
        """

        # init
        # database
            # player tables creation
        player_table = Player_table_creator(self.client)
        await player_table.creator.create_all()

        character_table = Character_table_creator(self.client)
        await character_table.creator.create_all()

        # sort all the character
        summoner = Summoner(self.client)
        await summoner.sort(Basic_banner().all, banner = "basic")
            # set sorted to true
        Sorted_banner.is_sorted = True

        print("BACKGROUND : DONE")
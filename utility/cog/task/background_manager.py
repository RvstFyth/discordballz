"""
Manages the background tasks

--

Authod : DrLarck

Last update : 20/08/19 (DrLarck)
"""

# dependacies
import asyncio

# utils
from utility.database.operation.database_table import Table_creator
    # database
from utility.database.operation.table_creation.player_table import Player_table_creator

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

        print("BACKGROUND : DONE")
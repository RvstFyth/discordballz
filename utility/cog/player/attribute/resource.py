"""
Manages the player's resources.

--

Author : DrLarck

Last update : 26/08/19
"""

# dependancies
import asyncio

# util
from utility.database.database_manager import Database

# resource manager
class Player_resource:
    """
    Get and manages the player's resources.

    - Parameter :

    `client` : Represents a `discord.Client`. The client must handle a database connection pool (i.e Database().init())

    `player` : Represents a `Player()` instance.

    - Method :

    # get
    :coro:`update()` : Update the player object by getting the resources from the database.

    :coro:`get_dragonstone() : Update and return the player's dragonstone amount.

    # remove
    """

    # attribute
    def __init__(self, client, player):
        # basics
        self.client = client
        self.player = player
        self.db = Database(self.client.db)

        # resource
        self.dragonstone = 0
        self.zenis = 0
    
    # method
    async def update(self):
        """
        `coroutine`

        Updates the player object by getting the resources from the database.

        --

        Return : None
        """

        # init
        get_zenis = f"SELECT player_zenis FROM player_resource WHERE player_id = {self.player.id};"
        get_ds = f"SELECT player_dragonstone FROM player_resource WHERE player_id = {self.player.id};"

        # get resource
        self.zenis = await self.db.fetchval(get_zenis)
        self.dragonstone = await self.db.fetchval(get_ds)

        return
    
    # getter
    async def get_dragonstone(self):
        """
        `coroutine`

        Get the player's stones and update it.

        --

        Return : player's dragonstone
        """

        # init
        get_ds = f"SELECT player_dragonstone FROM player_resource WHERE player_id = {self.player.id};"

        # get resource
        self.dragonstone = await self.db.fetchval(get_ds)

        return(self.dragonstone)
    
    async def get_zenis(self):
        """
        `coroutine`

        Get the player's zenis and update it.

        --

        Return : player's zenis
        """

        # init
        get_zenis = f"SELECT player_zenis FROM player_resource WHERE player_id = {self.player.id};"

        # get resource
        self.zenis = await self.db.fetchval(get_zenis)

        return(self.zenis)
    
    # remove
    async def remove_dragonstone(self, amount):
        """
        `coroutine`

        Remove a certain amount of dragonstone from the player's resources.

        - Parameter :

        `amount` : int - The amount of stone to remove

        --

        Return : None
        """

        # init
        await self.get_dragonstone()  # update the player's resource
        update_stone = f"UPDATE player_resource SET player_dragonstone = {self.dragonstone} WHERE player_id = {self.player.id};"

        # update 
        self.dragonstone -= amount
        await self.db.execute(update_stone)

        return
    
    async def remove_zenis(self, amount):
        """
        `coroutine`

        Remove a certain amount of zenis from the player's resources.

        - Parameter : 

        `amount` : int - The amount of zenis to remove.

        --

        Return : None
        """

        # init
        await self.get_zenis()
        update_zenis = f"UPDATE player_resource SET player_zenis = {self.player.zenis} WHERE player_id = {self.player.id};"

        # update
        self.zenis -= amount
        await self.db.execute(update_zenis)

        return
'''
Manages the player's informations.

Last update: 12/07/19
'''

# Dependancies

import asyncio

# object

from cogs.objects.database import Database
from cogs.objects.player.slot import Slot
from cogs.objects.player.fighter import Fighter

class Player:
    '''
    Represent a player.

    `client` : must be `discord.Client` object.

    `player` : must be `discord.Member` object.

    Attributes :
        name : str - Player name.
        id : int - Player id.
        avatar : str - Player avatar url.
        register_date : str - Player register date, format : DD/MM/YY (None)
        language : str - Player language, format : LL (None)
        location : str - Player location, default : UNKNOWN (None)

        stone : int - Player stone amount. (None)
        zenis : int - Player zenis amount. (None)
        level : int - Player level. (None)
        xp : int - Player xp amount. (None)

        Subclass :
            slot : Slot()
    
    Method : 
        :coro:`init()` : Init the object. Get the resources values.

        :coro:`remove_dragonstones(amount)` : Remove the passed amount of dragonstones from the player resources.

        :coro:`remove_zenis(amount)` : Same as remove_dragonstones method but for zenis.
    '''

    def __init__(self, client, player):
        self.client = client
        self.player = player
        self.db = Database(self.client)

        # attr
            # infos
        self.name = player.name
        self.id = self.player.id
        self.avatar = player.avatar_url
        self.register_date = None
        self.language = None
        self.location = None

            # ressources
        self.stone = None
        self.zenis = None

            # exp
        self.level = None
        self.xp = None

        # subclass
        self.slot = Slot(self.client, self)
        self.fighter = Fighter(self.client, self)
    
    # method

    async def init(self):
        '''
        `coroutine`

        Init the object. Set the informations.
        '''

        # queries

        register_date = 'SELECT player_register_date FROM player_info WHERE player_id = {};'.format(self.player.id)

        language = 'SELECT player_lang FROM player_info WHERE player_id = {};'.format(self.player.id)

        location = 'SELECT player_location FROM player_info WHERE player_id = {};'.format(self.player.id)

        stone = 'SELECT player_dragonstone FROM player_resource WHERE player_id = {};'.format(self.player.id)

        zenis = 'SELECT player_zenis FROM player_resource WHERE player_id = {};'.format(self.player.id)

        # execute the queries
        # set the attr
        self.register_date = await self.db.fetchval(register_date)
        self.language = await self.db.fetchval(language)
        self.location = await self.db.fetchval(location)

        self.stone = int(await self.db.fetchval(stone))
        self.zenis = int(await self.db.fetchval(zenis))

        return
    
    async def remove_dragonstone(self, amount: int):
        '''
        `coroutine`

        Remove the amount of ds passed as `amount` from the player's inventory.

        Return: void
        '''

        # init
        await self.init()

        self.stone -= amount

        if(self.stone < 0):
            self.stone = 0

        new_amount = 'UPDATE player_resource SET player_dragonstone = {} WHERE player_id = {};'.format(self.stone, self.id)

        await self.db.execute(new_amount)
        # update the object
        await self.init()

        return
    
    async def remove_zenis(self, amount: int):
        '''
        `coroutine`

        Remove the amount of zenis passed as `amount` from the player's inventory.

        Return: void
        '''

        # init
        await self.init()

        self.zenis -= amount

        if(self.zenis < 0):
            self.zenis = 0
        
        new_amount = 'UPDATE player_resource SET player_zenis = {} WHERE player_id = {};'.format(self.zenis, self.id)

        await self.db.execute(new_amount)
        # update the object
        await self.init()

        return
    
    async def add_dragonstones(self, amount):
        """
        `coroutine`

        Add a certain amount of stones to the player dragonstone count.
        """

        # init
        await self.init()

        new_amount = self.stone + amount

        update = f"UPDATE player_resource SET player_dragonstone = {new_amount} WHERE player_id = {self.id};"

        await self.db.execute(update)

        await self.init()

        return
    
    async def add_zenis(self, amount):
        """
        `coroutine`

        Add a certain amount of zenis to the player resources.
        """

        # init
        await self.init()

        new_amount = self.zenis + amount

        update = f"UPDATE player_resource SET player_zenis = {new_amount} WHERE player_id = {self.id};"
        await self.db.execute(update)

        await self.init()

        return
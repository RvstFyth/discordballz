'''
Manages the player's informations.

Last update: 30/06/19
'''

# Dependancies

import asyncio

# object

from cogs.objects.database import Database

# Database
    # Select

from cogs.utils.functions.database.select.player.player import Select_player_register_date, Select_player_language, Select_player_location, Select_player_fighter
from cogs.utils.functions.database.select.player.player_ressources import Select_player_stones, Select_player_zenis
from cogs.utils.functions.database.select.player.player_experience import Select_player_level, Select_player_xp

    # Update

from cogs.utils.functions.database.update.player_experience import Update_player_level, Update_player_xp
from cogs.utils.functions.database.update.player.player_ressources import Update_player_ressources_stones, Update_player_ressources_zenis

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
    
    Method : 
        coroutine - init() - Init the object.
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
    
    # method

    async def init(self):
        '''
        `coroutine`

        Init the object. Set the informations.
        '''

        # init

        await self.db.init()

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

        await self.db.close()

        return
    
    async def remove_dragonstone(self, amount: int):
        '''
        `coroutine`

        Remove the amount of ds passed as `amount` from the player's inventory.

        Return: void
        '''

        # init

        await self.db.init()

        self.stone -= amount

        if(self.stone < 0):
            self.stone = 0

        new_amount = 'UPDATE player_resource SET player_dragonstone = {} WHERE player_id = {};'.format(self.stone, self.id)

        await self.db.execute(new_amount)

        await self.db.close()

        return
    
    async def remove_zenis(self, amount: int):
        '''
        `coroutine`

        Remove the amount of zenis passed as `amount` from the player's inventory.

        Return: void
        '''

        # init

        await self.db.init()

        self.zenis -= amount

        if(self.zenis < 0):
            self.zenis = 0
        
        new_amount = 'UPDATE player_resource SET player_zenis = {} WHERE player_id = {};'.format(self.zenis, self.id)

        await self.db.execute(new_amount)

        await self.db.close()

        return
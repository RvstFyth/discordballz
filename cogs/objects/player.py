'''
Manages the player's informations.

Last update: 14/05/19
'''

# Dependancies

import asyncio

# Database
    # Select

from cogs.utils.functions.database.select.player.player import Select_player_register_date, Select_player_language, Select_player_location
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

    *Method list* :
    
    1. Infos
    - `avatar` : Returns the player's avatar url.
    - `register_date` : Returns the player's register date.
    - language : Returns the player's language.

    2. Experience :
    - `level` : Returns the player's level.
    - `xp` : Returns the player's xp amount.

    3. Ressources
    - `stones` : Returns the player's stones.
    - `zenis` : Returns the player's zenis.
    - `remove_stones` : Remove a certain amount of stones.
    - `remove_zenis` : Remove a certain amount of zenis.
    '''

    def __init__(self, client, player):
        self.client = client
        self.player = player
    
    # Infos

    def avatar(self):
        '''
        Returns the player's avatar url.

        Return: str
        '''

        return(self.player.avatar_url)
    
    async def register_date(self):
        '''
        Returns the player's register date.

        Return : str
        '''

        date = await Select_player_register_date(self.client, self.player)

        return(date)
    
    async def language(self):
        '''
        `coroutine`

        Return the player's language.

        Return: str
        '''

        # Init

        player_lang = await Select_player_language(self.client, self.player)

        return(player_lang)
    
    async def location(self):
        '''
        `coroutine`

        Return the player's location.

        Return: str
        '''

        player_location = await Select_player_location(self.client, self.player)

        return(player_location)

    # Experience

    async def level(self):
        '''
        `coroutine`

        Returns the player's level.

        Return: int
        '''

        level = await Select_player_level(self.client, self.player)

        return(level)
    
    async def xp(self):
        '''
        `coroutine`

        Returns player's xp amount.

        Return: int
        '''

        xp = await Select_player_xp(self.client, self.player)

        return(xp)
    
    # Add

    async def add_xp(self, value: int):
        '''
        `coroutine`

        Increases the amount of player's xp.

        `value` : must be of type `int`.

        Return: void
        '''

        # Init

        player_xp = await Select_player_xp(self.client, self.player)

        player_xp += value

        await Update_player_xp(self.client, self.player, player_xp)

    # Ressources

    async def stones(self):
        '''
        `coroutine`

        Returns the player's stones.

        Return: int
        '''

        stone = await Select_player_stones(self.client, self.player)

        return(stone)
    
    async def zenis(self):
        '''
        `coroutine`

        Returns the player's zenis.

        Return: int
        '''

        zenis = await Select_player_zenis(self.client, self.player)

        return(zenis)
    
    async def remove_stones(self, amount):
        '''
        `coroutine`

        Remove a certain amount of player's stones.

        `amount` : must be type `int` and represent the amount of stones to remove.

        Return: void
        '''

        # Init 

        stones = await Select_player_stones(self.client, self.player)
        stones -= amount 

        await Update_player_ressources_stones(self.client, self.player, stones)

    async def remove_zenis(self, amount):
        '''
        `coroutine`

        Remove a certain amount of player's zenis.

        `amount` : must be type `int` and represent the amount of zenis to remove.

        Return: void
        '''

        # Init

        zenis = await Select_player_zenis(self.client, self.player)
        zenis -= amount

        await Update_player_ressources_zenis(self.client, self.player, zenis)
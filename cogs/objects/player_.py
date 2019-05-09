'''
Manages the player's informations.

Last update: 09/05/19
'''

# Dependancies

import asyncio

# Database

from cogs.utils.functions.database.select.player.player_ressources import Select_player_stones, Select_player_zenis

class Player_:
    '''
    Represent a player.

    `client` : must be `discord.Client` object.

    `player` : must be `discord.Member` object.

    *Method list* :
    
    1. Infos
    - `avatar` : Returns the player's avatar url.

    2. Ressources
    - `stones` : Returns the player's stones.
    - `zenis` : Returns the player's zenis.
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
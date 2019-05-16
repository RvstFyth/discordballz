'''
Store the character's basic informations using its global id.

Last update: 16/05/19
'''

# Dependancies

import asyncio

# Database

from cogs.utils.functions.database.select.character.character import Select_character_infos, Select_unique_characters_amount, Select_global_id_from_unique
from cogs.utils.functions.database.update.unique_characters import Update_unique_id_summon

# Id

from cogs.utils.functions.commands.summon.id_generator import Unique_id_generator

class Character:
    '''
    Return the character's informations.

    `client` : must be `discord.Client` object.

    `player` : must be `discord.Member` object.

    `character` : must be type `int` and represent the character's `global id`.

    `unique_id` : must be type `str`.

    Method list :

    1. Informations :

    - name : Returns the character name.
    - image : Returns the image url of the character.
    - rarity : Returns the character's rarity.
    - _type : Returns the character's type.
    - base_hp
    - damages
    
    2. Methods :

    - new_unique
    - global_id_from_unique : Return the character's global id from its unique one.
    '''

    def __init__(self, client, player, character = None, unique_id = None):
        self.client = client
        self.global_id = character
        self.unique_id = unique_id
        self.player = player
    
    # Basic informations

    async def name(self):
        '''
        `coroutine`

        Return the name of the character.

        Return: str
        '''

        character = await Select_character_infos(self.client, self.global_id)
        name = character['name']

        return(name)
    
    async def image(self):
        '''
        `coroutine`

        Return the image url of the character.

        Return: str (url)
        '''

        character = await Select_character_infos(self.client, self.global_id)
        url = character['image']

        return(url)
    
    async def rarity(self):
        '''
        `coroutine`

        Return the rarity of the character.

        Return: str
        '''

        character = await Select_character_infos(self.client, self.global_id)
        rarity = character['rarity']

        return(rarity)
    
    async def _type(self):
        '''
        `coroutine`

        Return the type of the character.

        Return: str
        '''

        character = await Select_character_infos(self.client, self.global_id)
        _type = character['type']

        return(_type)
    
    async def base_hp(self):
        '''
        `coroutine`

        Return the character base hp.

        Return: int
        '''

        character = await Select_character_infos(self.client, self.global_id)
        hp = character['base hp']

        return(hp)
    
    async def damages(self):
        '''
        `coroutine`

        Return the character's damages.

        Return: dict

        Index :

        - min
        - max
        '''

        character = await Select_character_infos(self.client, self.global_id)
        damages = {}
        damages['min'] = character['min dmg']
        damages['max'] = character['max dmg']

        return(damages)

    # Unique id

    async def new_unique(self, player):
        '''
        `coroutine`

        `player` : must be `discord.Member` object.

        Create a new unique character.
        '''

        reference = await Select_unique_characters_amount(self.client)
        unique_id = await Unique_id_generator(self.client, reference)

        await Update_unique_id_summon(self.client, reference, unique_id, player)
    
    async def global_id_from_unique(self):
        '''
        `coroutine`

        Return the character's global id from the unique passed one
        
        Return: int
        '''

        if(self.unique_id != None):
            global_id = await Select_global_id_from_unique(self.client, self.player, self.unique_id)
            self.global_id = global_id

            return(global_id)
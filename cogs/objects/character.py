'''
Store the character's basic informations using its global id.

Last update: 13/05/19
'''

# Dependancies

import asyncio

# Database

from cogs.utils.functions.database.select.character.character import Select_character_infos, Select_unique_characters_amount
from cogs.utils.functions.database.update.unique_characters import Update_unique_id_summon

# Id

from cogs.utils.functions.commands.summon.id_generator import Unique_id_generator

class Character:
    '''
    Return the character's informations.

    `client` : must be `discord.Client` object

    `character` : must be type `int` and represent the character's `global id`.

    Index :

    1. name
    2. image
    3. rarity
    4. _type
    5. new_unique
    '''

    def __init__(self, client, character):
        self.client = client
        self.character = character
    
    # Basic informations

    async def name(self):
        '''
        `coroutine`

        Return the name of the character.

        Return: str
        '''

        character = await Select_character_infos(self.client, self.character)
        name = character['name']

        return(name)
    
    async def image(self):
        '''
        `coroutine`

        Return the image url of the character.

        Return: str (url)
        '''

        character = await Select_character_infos(self.client, self.character)
        url = character['image']

        return(url)
    
    async def rarity(self):
        '''
        `coroutine`

        Return the rarity of the character.

        Return: str
        '''

        character = await Select_character_infos(self.client, self.character)
        rarity = character['rarity']

        return(rarity)
    
    async def _type(self):
        '''
        `coroutine`

        Return the type of the character.

        Return: str
        '''

        character = await Select_character_infos(self.client, self.character)
        _type = character['type']

        return(_type)
    
    async def new_unique(self, player):
        '''
        `coroutine`

        `player` : must be `discord.Member` object.

        Create a new unique character.
        '''

        reference = await Select_unique_characters_amount(self.client)
        unique_id = await Unique_id_generator(self.client, reference)

        await Update_unique_id_summon(self.client, reference, unique_id, player)
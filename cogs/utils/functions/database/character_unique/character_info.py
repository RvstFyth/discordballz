'''
Manages the informations about a character from the character_unique table.

last update: 07/07/19
'''

# dependancies

import asyncio

# object

from cogs.objects.database import Database

# utils

from cogs.objects.character.characters_list.all_char import Get_char

async def Character_from_unique(client, ctx, player, unique_id):
    '''
    `coroutine`

    Return a `Character()` instance based on the informations stored at its unique id.

    `client` : must be `discord.Client` instance

    `ctx` : must be `discord.ext.commands.Context`

    `player` : must be `discord.Member` instance

    `unique_id` : must be `str` and represent the character's unique id.

    Return : Character() instance
    '''

    # init
    db = Database(client)

    # queries

    fetch_char_infos = f"SELECT character_global_id, character_level, character_type, character_rarity FROM character_unique WHERE character_owner_id = {player.id} AND character_unique_id = '{unique_id}';"

    # fetching
    await db.init()
    character_info = await db.fetch(fetch_char_infos)
    await db.close()

    character_info = character_info[0]

    # get values    
    global_id, level, type, rarity = character_info[0], character_info[1], character_info[2], character_info[3]

    character = await Get_char(global_id)
    character.level, character.type_value, character.rarity_value = level, type, rarity

    await character.init(client, ctx)

    return(character)
'''
Manages the select SQL statments on the characters table.

Last update: 15/05/19
'''

# Dependancies

import asyncpg
from time import strftime, gmtime

async def Select_character_infos(client, character):
    '''
    `coroutine`

    Returns all the informations about the passed character.

    `client` : must be `discord.Client` object.

    `character` : must be type `int` and represent the character's `global id`.

    Return: dict

    Index :

    1. global id
    2. name
    3. image
    4. rarity
    5. type
    6. base hp
    7. min dmg
    8. max dmg
    '''

    # Init
    character_fetch, character_infos = None, {}
    conn = await client.db.acquire()
    
    query = 'SELECT * FROM characters WHERE global_id = $1;'

    try:
        character_fetch = await conn.fetch(query, character)
    
    except Exception as error:
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} Error in cogs.utils.functions.database.select.character.character.Select_character_infos() : l.35 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)

    character_infos['global id'] = character_fetch[0][1]
    character_infos['name'] = character_fetch[0][2]
    character_infos['image'] = character_fetch[0][3]
    character_infos['rarity'] = character_fetch[0][4]
    character_infos['type'] = character_fetch[0][5]
    character_infos['base hp'] = character_fetch[0][6]
    character_infos['min dmg'] = character_fetch[0][7]
    character_infos['max dmg'] = character_fetch[0][8]

    return(character_infos)

async def Select_unique_characters_amount(client):
    '''
    `couroutine` 

    Return the total amount of unique characters.

    `client` : must be `discord.Client` object.

    Return: int
    '''

    # Init

    total = None
    conn = await client.db.acquire()

    query = 'SELECT reference FROM unique_characters;'

    try:
        total = await conn.fetch(query)
        total = len(total)
    
    except Exception as error:
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} Error in cogs.utils.functions.database.select.character.character.Select_unique_characters_amount() : l.77 - 78: {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
    
    return(total)

async def Select_global_id_from_unique(client, player, unique_id):
    '''
    `coroutine`

    Return the global id of the character using his unique id.
    
    `client` : must be `dicord.Client` object.

    `player` : must be `discord.Member` object.

    `unique_id` : must be type `str`.

    Return: int
    '''

    # Init

    global_id = None
    conn = await client.db.acquire()

    query = 'SELECT global_id FROM unique_characters WHERE unique_id = $1 AND player_id = $2;'

    try:
        global_id = await conn.fetchval(query, unique_id, player.id)
    
    except Exception as error:
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} Error in cogs.utils.functions.database.select.character.character.Select_global_id_from_unique() : l.119: {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
    
    if(global_id != None):
        return(int(global_id))
    
    else:
        return(global_id)
'''
Functions that manages the insert statment into the unique_characters table.

Last update: 12/05/19
'''

# Dependancies

import asyncpg, time
from time import strftime, gmtime

async def Insert_unique_character(client, player, global_id):
    '''
    Insert a unique character into the unique_characters table.

    `client` : must be `discord.Client` object.

    `player` : must be `discord.Member` object.

    `global_id` : must be type `int`, represents the global id of a character.

    Return: void
    '''

    # Init

    conn = await client.db.acquire()

    query = 'INSERT INTO unique_characters(player_id, global_id) VALUES($1, $2);'

    try:
        await conn.execute(query, player.id, global_id)
    
    except Exception as error:
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} Error in cogs.utils.functions.database.insert.characters.Insert_unique_character() : l.32 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
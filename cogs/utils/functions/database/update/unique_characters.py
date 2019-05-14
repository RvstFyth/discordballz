'''
These functions update the unique_characters table.

Last update: 12/05/19
'''

# Dependancies

import asyncpg, time
from time import strftime, gmtime

async def Update_unique_id_summon(client, reference, new_id, player):
    '''
    Updates the unique_id of a character at the passed reference number.

    `client` : must be `discord.Client` object.

    `reference` : must be type `int`.

    `new_id` : must be type `str`.

    `player` : must be `discord.Member` object.

    Return: void
    '''

    # Init

    conn = await client.db.acquire()

    query = 'UPDATE unique_characters SET unique_id = $1 WHERE reference = $2 AND player_id = $3;'

    try:
        await conn.execute(query, new_id, reference, player.id)
    
    except asyncpg.UniqueViolationError:
        pass
    
    except Exception as error:
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} Error in cogs.utils.functions.database.update.unique_characters.Update_unique_id_summon() : l.34 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
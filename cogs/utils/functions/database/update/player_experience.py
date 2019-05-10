'''
These functions update the values of the player_experience table.

Last update: 10/05/19
'''

# Dependancies

import asyncpg, time
from time import strftime, gmtime

async def Update_player_xp(client, player, value):
    '''
    Updates the player_xp value.

    `client` : must be `discord.Client` object.

    `player` : must be `discord.Member` object.

    `value` : must be type `int`

    Return: void
    '''

    # Init

    conn = await client.db.acquire()

    query = 'UPDATE player_experience SET player_xp = $1 WHERE player_id = $2;'

    try:
        await conn.execute(query, value, player.id)
    
    except Exception as error:
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} Error in cogs.utils.functions.database.update.player_experience.Update_player_xp() : l.32 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)

async def Update_player_level(client, player, value):
    '''
    Updates the player_level value.

    `client` : must be `discord.Client` object.

    `player` : must be `discord.Member` object.

    `value` : must be type `int`

    Return: void
    '''

    # Init

    conn = await client.db.acquire()

    query = 'UPDATE player_experience SET player_level = $1 WHERE player_id = $2;'

    try:
        await conn.execute(query, value, player.id)
    
    except Exception as error:
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} Error in cogs.utils.functions.database.update.player_experience.Update_player_level() : l.62 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
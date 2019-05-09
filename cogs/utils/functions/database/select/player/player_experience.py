'''
These functions return the player's experience informations

Last update: 09/05/19
'''

# Dependancies

import asyncpg, time
from time import strftime, gmtime

async def Select_player_level(client, player):
    '''
    Returns the player's level.

    `client` : must be `discord.Client` object.

    `player` : must be `discord.Member` object.

    Return: int
    '''

    # Init

    level = None
    conn = await client.db.acquire()

    query = 'SELECT player_level FROM player_experience WHERE player_id = $1;'

    try:
        level = await conn.fetchval(query, player.id)
        level = int(level)
    
    except Exception as error:
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} Error in cogs.utils.functions.database.select.player.player_experience.Select_player_level() : l.31 - 32 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)

    
    return(level)

async def Select_player_xp(client, player):
    '''
    Returns the player's xp amount.

    `client` : must be `discord.Client` object.

    `player` : must be `discord.Member` object.

    Return: int
    '''

    # Init

    xp = None
    conn = await client.db.acquire()

    query = 'SELECT player_xp FROM player_experience WHERE player_id = $1;'

    try:
        xp = await conn.fetchval(query, player.id)
        xp = int(xp)
    
    except Exception as error:
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} Error in cogs.utils.functions.database.select.player.player_experience.Select_player_xp() : l.64 - 65 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)

    
    return(xp)
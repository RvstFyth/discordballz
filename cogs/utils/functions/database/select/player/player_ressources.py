'''
Returns informations stored in the player_ressources table.

Last update: 09/05/19
'''

# Dependancies

import asyncpg, time
from time import strftime, gmtime

async def Select_player_stones(client, player):
    '''
    Returns the amount of dragon stones the player has.

    `client` : must be `discord.Client` object.

    `player` : must be `discord.Member` object.

    Return: int
    '''

    # Init

    player_stones = None

    conn = await client.db.acquire()

    query = 'SELECT player_stones FROM player_ressources WHERE player_id = $1;'

    try:
        player_stones = await conn.fetchval(query, player.id)
        player_stones = int(player_stones)
    
    except Exception as error :
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} - Error in cogs.utils.functions.database.select.player.player_ressources.Select_player_stones() : l. 32 - 33 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
    
    return(player_stones)

async def Select_player_zenis(client, player):
    '''
    Returns the player's zenis.

    `client` : must be `discord.Client` object.

    `player` : must be `discord.Member` object.

    Return: int
    '''

    # Init

    player_zenis = None

    conn = await client.db.acquire()

    query = 'SELECT player_zenis FROM player_ressources WHERE player_id = $1;'

    try:
        player_zenis = await conn.fetchval(query, player.id)
        player_zenis = int(player_zenis)
    
    except Exception as error:
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} - Error in cogs.utils.functions.database.select.player.player_ressources.Select_player_zenis() : l. 65 - 66 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
    
    return(player_zenis)
'''
Manages the update statment for the player's ressources.

Last update: 14/05/19
'''

# Dependancies

import asyncpg
from time import strftime, gmtime

async def Update_player_ressources_stones(client, player, value):
    '''
    `coroutine` 

    Update the value of the player's stones.

    `client` : must be `discord.Client` object.

    `player` : must be `discord.Member` object.

    `value` : must be type `int`.

    Return: void
    '''

    # Init

    conn = await client.db.acquire()

    query = 'UPDATE player_ressources SET player_stones = $1 WHERE player_id = $2;'

    try:
        await conn.execute(query, value, player.id)
    
    except Exception as error:
        error_time = strftime('%d/%m/%y', gmtime())
        print('{} Error in cogs.utils.functions.database.update.player.player_ressources.Update_player_ressources_stones() : l.34 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)

async def Update_player_ressources_zenis(client, player, value):
    '''
    `coroutine` 

    Update the value of the player's zenis.

    `client` : must be `discord.Client` object.

    `player` : must be `discord.Member` object.

    `value` : must be type `int`.

    Return: void
    '''

    # Init

    conn = await client.db.acquire()

    query = 'UPDATE player_ressources SET player_zenis = $1 WHERE player_id = $2;'

    try:
        await conn.execute(query, value, player.id)
    
    except Exception as error:
        error_time = strftime('%d/%m/%y', gmtime())
        print('{} Error in cogs.utils.functions.database.update.player.player_ressources.Update_player_ressources_zenis() : l.66 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
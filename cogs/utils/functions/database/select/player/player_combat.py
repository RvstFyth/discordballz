'''
Return the player_combat tables informations.

Last update: 26/05/19
'''

# Dependancies

import asyncpg, asyncio
from time import strftime, gmtime

async def Select_player_team(client, player):
    '''
    Return the player's team and the leader.

    Returns unique id.

    `client` : must be `discord.Client` object.

    `player` : must be `discord.Member` object.

    Return: dict

    Index :
    - fighter a : str (unique id)
    - fighter b : str (unique id)
    - fighter c : str (unique id)
    - leader : str (unique id)
    '''

    # Init

    player_team_fetch = None
    player_team = {}
    conn = await client.db.acquire()

    query = '''
    SELECT * FROM player_combat_info WHERE player_id = $1;
    '''

    try:
        player_team_fetch = await conn.fetch(query, player.id)

    except Exception as error:
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} Error in cogs.utils.functions.database.select.player.player_combat.Select_player_team() : l.42 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
    
    player_team['fighter a'] = player_team_fetch[0][2]
    player_team['fighter b'] = player_team_fetch[0][3]
    player_team['fighter c'] = player_team_fetch[0][4]
    player_team['leader'] = player_team_fetch[0][5]

    return(player_team)
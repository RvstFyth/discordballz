'''
Get the player team informations.

Last update: 01/07/19
'''

# Dependancies

import asyncio

# Utils

from cogs.utils.functions.database.select.character.character import Select_global_id_from_unique
from cogs.utils.functions.database.select.player.player_combat import Select_player_team
from cogs.objects.character.characters_list.all_char import Get_char

# Objects

from cogs.objects.database import Database
from cogs.objects.character.character import Character

async def Get_player_team(client, player):
    '''
    `coroutine`
    
    Return the fighter object of the player's team.

    `client` : must be `discord.Client` object.

    `player` : must be `discord.Member` object.

    Return: list of `Character` object.

    Index :
    - 0 : fighter a
    - 1 : fighter b
    - 2 : fighter c
    - 3 : leader
    '''

    # Init

    db = Database(client)
    await db.init()

    # Now we retrieve the global id of the characters from their unique one

    leader = int(await db.fetchval('SELECT player_leader FROM player_combat_info WHERE player_id = {};'.format(player.id)))
    fighter_a = int(await db.fetchval('SELECT player_fighter_a FROM player_combat_info WHERE player_id = {};'.format(player.id)))
    fighter_b = int(await db.fetchval('SELECT player_fighter_b FROM player_combat_info WHERE player_id = {};'.format(player.id)))
    fighter_c = int(await db.fetchval('SELECT player_fighter_c FROM player_combat_info WHERE player_id = {};'.format(player.id)))

    '''fighter_a = await Select_global_id_from_unique(client, player, player_team['fighter a']) 
    fighter_b = await Select_global_id_from_unique(client, player, player_team['fighter b'])
    fighter_c = await Select_global_id_from_unique(client, player, player_team['fighter c'])
    leader = await Select_global_id_from_unique(client, player, player_team['leader'])'''

    # Convert the fighter var into object
    player_team = []
    
    if(leader > 0):
        leader = await Get_char(leader)
        player_team.append(leader)

    if(fighter_a > 0):
        fighter_a = await Get_char(fighter_a)
        player_team.append(fighter_a)
    
    if(fighter_b > 0):
        fighter_b = await Get_char(fighter_b)
        player_team.append(fighter_b)
    
    if(fighter_c > 0):
        fighter_c =  await Get_char(fighter_c)
        player_team.append(fighter_c)

    return(player_team)
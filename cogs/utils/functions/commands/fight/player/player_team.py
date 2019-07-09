'''
Get the player team informations.

Last update: 09/07/19
'''

# Dependancies

import asyncio

# Utils

from cogs.utils.functions.database.select.character.character import Select_global_id_from_unique
from cogs.utils.functions.database.select.player.player_combat import Select_player_team
from cogs.utils.functions.database.character_unique.character_info import Character_from_unique

# Objects

from cogs.objects.database import Database
from cogs.objects.character.character import Character

async def Get_player_team(client, ctx, player):
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

    # Now we retrieve the global id of the characters from their unique one

    leader = await db.fetchval('SELECT player_leader FROM player_combat_info WHERE player_id = {};'.format(player.id))
    fighter_a = await db.fetchval('SELECT player_fighter_a FROM player_combat_info WHERE player_id = {};'.format(player.id))
    fighter_b = await db.fetchval('SELECT player_fighter_b FROM player_combat_info WHERE player_id = {};'.format(player.id))
    fighter_c = await db.fetchval('SELECT player_fighter_c FROM player_combat_info WHERE player_id = {};'.format(player.id))

    # Convert the fighter var into object
    player_team = []

    if(fighter_a == "NONE"):
        player_team.append(fighter_a)
    
    else:  # a
        fighter_a = await Character_from_unique(client, ctx, player, fighter_a)
        player_team.append(fighter_a)

    if(fighter_b == "NONE"):
        player_team.append(fighter_b)
    
    else:  # b
        fighter_b = await Character_from_unique(client, ctx, player, fighter_b)
        player_team.append(fighter_b)
    
    if(fighter_c == "NONE"):
        player_team.append(fighter_c)
    
    else:  # c
        fighter_c = await Character_from_unique(client, ctx, player, fighter_c)
        player_team.append(fighter_c)
    
    if(leader == "NONE"):
        player_team.append(leader)
    
    else:  # leader
        leader = await Character_from_unique(client, ctx, player, leader)
        player_team.append(leader)

    return(player_team)
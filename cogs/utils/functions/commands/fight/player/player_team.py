'''
Get the player team informations.

Last update: 27/05/19
'''

# Dependancies

import asyncio

# Utils

from cogs.utils.functions.database.select.character.character import Select_global_id_from_unique
from cogs.utils.functions.database.select.player.player_combat import Select_player_team
from cogs.objects.character.characters_list.all_char import Get_char

# Objects

from cogs.objects.character.character import Character
from cogs.objects.character.fighter import Fighter

async def Get_player_team(client, player):
    '''
    `coroutine`
    
    Return the fighter object of the player's team.

    `client` : must be `discord.Client` object.

    `player` : must be `discord.Member` object.

    Return: list of `Fighter` object.

    Index :
    - 0 : fighter a
    - 1 : fighter b
    - 2 : fighter c
    - 3 : leader
    '''

    # Init

    player_team = await Select_player_team(client, player)

    # Now we retrieve the global id of the characters from their unique one

    fighter_a = await Select_global_id_from_unique(client, player, player_team['fighter a'])
    fighter_b = await Select_global_id_from_unique(client, player, player_team['fighter b'])
    fighter_c = await Select_global_id_from_unique(client, player, player_team['fighter c'])
    leader = await Select_global_id_from_unique(client, player, player_team['leader'])

    # Convert the fighter var into object

    fighter_a, fighter_b, fighter_c = await Get_char(fighter_a), await Get_char(fighter_b), await Get_char(fighter_c)
    leader = await Get_char(leader)

    # Creating the list

    fighter_a, fighter_b, fighter_c = Fighter(fighter_a), Fighter(fighter_b), Fighter(fighter_c)
    player_team = [fighter_a, fighter_b, fighter_c, leader]

    return(player_team)
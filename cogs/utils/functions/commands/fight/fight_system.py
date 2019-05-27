'''
Manages the fight system.

Last update: 27/05/19
'''

# Dependancies

import asyncio

# Object

from cogs.objects.fighter import Fighter
from cogs.objects.enemy import Enemy
from configuration.characters.characters_list.char_1 import Char_1

# Utils

from cogs.utils.functions.readability.embed import Basic_embed
from cogs.utils.functions.readability.displayer.character_displayer import Display_character
from cogs.utils.functions.commands.fight.player.player_team import Get_player_team

async def Pve_Fight(client, ctx, player, enemy):
    '''
    `coroutine`

    This functions is made for the Pve fights.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `player` : must be `discord.Member` object.

    `enemy` : must be a list of `Enemy` objects.

    Return: void
    '''

    # Init

    player_team = await Get_player_team(client, player)  # Represent the player team (Character Objects)
    enemy_team = enemy

    # Init the player team

    fighter_leader = player_team[3]
    fighter_a, fighter_b, fighter_c = player_team[0], player_team[1], player_team[2]

    player_team = [fighter_a, fighter_b, fighter_c]

    # Init Teams

    for fighter in player_team :
        await asyncio.sleep(0)

        await fighter.stat.init(client, ctx)
    
    for enemy in enemy_team :
        await asyncio.sleep(0)

        await enemy.stat.init(client, ctx)

    await Display_character(client, ctx, fighter_a.stat)

    # Turn

    turn = 1  # Begin at 1

    while fighter_a.stat.current_hp > 0 :
        await asyncio.sleep(0)
        print('Tour {}'.format(turn))

        # Trigger the effects
            # Enemy team
        
        for enemy in enemy_team:
            await asyncio.sleep(0)

            for dot in enemy.dot :
                await asyncio.sleep(0)

                # If one of the effect is over
                if(dot.duration <= 0):
                    enemy.dot.remove(dot)

                    if(len(enemy.dot) == 0):
                        break

                # If the effect is not over, apply the effect

                await dot.apply_dot(enemy)

        # End of turn

        turn += 1
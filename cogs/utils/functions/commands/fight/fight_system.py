'''
Manages the fight system.

Last update: 28/05/19
'''

# Dependancies

import asyncio

# Object

from cogs.objects.character.fighter import Fighter
from cogs.objects.character.characters_list import char_1

# Utils

from cogs.utils.functions.commands.fight.displayer.display_teams import Pve_display_team
from cogs.utils.functions.readability.embed import Basic_embed
from cogs.utils.functions.readability.displayer.character_displayer import Display_character
from cogs.utils.functions.commands.fight.player.player_team import Get_player_team
from cogs.utils.functions.commands.fight.displayer.display_fighter import Pve_display_fighter

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

    enemy_fighter = Fighter(enemy[0])

    player_team = await Get_player_team(client, player)  # Represent the player team (Character Objects)
    enemy_team = [enemy_fighter]

    # Init the player team

    fighter_leader = player_team[3]
    fighter_a, fighter_b, fighter_c = player_team[0], player_team[1], player_team[2]

    player_team = [fighter_a, fighter_b, fighter_c]

    # Init Teams

    for fighter in player_team :
        await asyncio.sleep(0)

        await fighter.stat.init(client, ctx)
        await fighter.init()
    
    for enemy in enemy_team :
        await asyncio.sleep(0)

        await enemy.stat.init(client, ctx)
        await enemy.init()

    # Turn

    turn = 1  # Begin at 1

    while fighter_a.stat.current_hp > 0 :
        await asyncio.sleep(0)

        # Display both team

        if(turn == 1):
            await Pve_display_team(client, ctx, player, player_team, enemy_team)

        # Test

        await player_team[0].stat.first_ability(client, ctx, player_team[0], player_team, enemy_team)

        # Trigger the effects

            # Player team
        
        for fighter in player_team:
            await asyncio.sleep(0)

            # Dot
            for dot in fighter.dot:
                await asyncio.sleep(0)

                if(dot.duration <= 0):
                    fighter.dot.remove(dot)

                    if(len(fighter.dot) == 0):
                        break
                
                await dot.apply_dot(fighter)

            # Enemy team
        
        for enemy in enemy_team:
            await asyncio.sleep(0)
            
            # Dot
            for dot in enemy.dot :
                await asyncio.sleep(0)

                # If one of the effect is over
                if(dot.duration <= 0):
                    enemy.dot.remove(dot)

                    if(len(enemy.dot) == 0):
                        break

                # If the effect is not over, apply the effect

                await dot.apply_dot(enemy)

        # Turn maker
        # For PvE the player starts always first

        for fighter in player_team:
            await asyncio.sleep(0)
            
            if(len(fighter.dot) > 0):
                if(fighter.stat.current_hp > 0):
                    # Display fighter's turn

                    await Pve_display_fighter(client, ctx, fighter)
            
            else:
                pass

            # Then ask action
        
        # Sam for enemy team

        # End of turn

        turn += 1
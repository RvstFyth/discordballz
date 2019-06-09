'''
Manages the fight system.

Last update: 08/06/19
'''

# Dependancies

import asyncio
from random import randint

# Object

from cogs.objects.character.character import Character
from cogs.objects.character.characters_list import char_1

# Utils

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.commands.fight.displayer.display_teams import Pve_display_team
from cogs.utils.functions.readability.embed import Basic_embed
from cogs.utils.functions.readability.displayer.character_displayer import Display_character
from cogs.utils.functions.commands.fight.player.player_team import Get_player_team
from cogs.utils.functions.commands.fight.displayer.display_fighter import Pve_display_fighter
from cogs.utils.functions.commands.fight.wait_for.wait_for_move import Wait_for_move
from cogs.utils.functions.commands.fight.functions.stat_manager import Reset_stat

# Phases

from cogs.utils.functions.commands.fight.phases.trigger_phase import Triggers_phase
from cogs.utils.functions.commands.fight.phases.selection_phase import Selection_phase
from cogs.utils.functions.commands.fight.phases.battle_phase import Battle_phase

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

    _ = await Translate(client, ctx)
    
    player_team = await Get_player_team(client, player)  # Represent the player team (Character Objects)
    enemy_team = enemy

    # Init the player team

    fighter_leader = player_team[3]
    fighter_a, fighter_b, fighter_c = player_team[0], player_team[1], player_team[2]

    player_team = [fighter_a, fighter_b, fighter_c]

    player_team_count = 0
    player_team_average_hp = 0

    # Init the enemy team

    enemy_team_count = 0
    enemy_team_average_hp = 0

        # Calculation of player team average hps

    for character in player_team:
        await asyncio.sleep(0)

        player_team_average_hp += character.current_hp

        player_team_count += 1
    
    player_team_average_hp /= player_team_count

        # Calculation of enemy team average hps
    
    for enemy in enemy_team:
        await asyncio.sleep(0)

        enemy_team_average_hp += enemy.current_hp

        enemy_team_count += 1
    
    enemy_team_average_hp /= enemy_team_count

    # All char
    # Join the player team and enemy team to determinate the number of characters

    all_fighter = player_team + enemy_team

    # Init Teams

    for fighter in player_team :
        await asyncio.sleep(0)

        await fighter.init(client, ctx)
    
    for enemy in enemy_team :
        await asyncio.sleep(0)

        await enemy.init(client, ctx)

    # Main loop
    # Turn

    turn = 1  # Begin at 1

    while player_team_average_hp > 0 and enemy_team_average_hp > 0:
        await asyncio.sleep(0)

        # Init

        player_move = []
        enemy_move = []
        
        player_team_average_hp = 0
        enemy_team_average_hp = 0
        player_team_count = 0
        enemy_team_count = 0

        await asyncio.sleep(2)

        ##### NEW TURN ##### 

        await Pve_display_team(client, ctx, player, player_team, enemy_team)

        await ctx.send(_('---------- 📣 Round {} ! ----------').format(turn))
        await asyncio.sleep(2)
        
        # Trigger the effects
        
        await ctx.send(_('🌀 - Triggers Phase'))
        await asyncio.sleep(1)

        await Triggers_phase(client, ctx, player, player_team, enemy_team, 0)
        await Triggers_phase(client, ctx, player, enemy_team, enemy_team, 1)

        # Calculation of player team average hps

        for character in player_team:
            await asyncio.sleep(0)

            player_team_average_hp += character.current_hp

            player_team_count += 1
        
        player_team_average_hp = int(player_team_average_hp / player_team_count)

            # Calculation of enemy team average hps
        
        for enemy in enemy_team:
            await asyncio.sleep(0)

            enemy_team_average_hp += enemy.current_hp

            enemy_team_count += 1
        
        enemy_team_average_hp = int(enemy_team_average_hp / enemy_team_count)

                # If winner 

        if(player_team_average_hp <= 0 and enemy_team_average_hp > 0):
            await ctx.send(_('Enemy team won !'))
            break
        
        elif(enemy_team_average_hp <= 0 and player_team_average_hp > 0):
            await ctx.send(_('Player team won !'))
            break
        
        elif(enemy_team_average_hp <= 0 and player_team_average_hp <= 0):
            await ctx.send('Draw !')
            break
        
        else:
            pass
        
        # Turn maker
        # For PvE the player starts always first
        
        await ctx.send(_('💠 - Selection Phase'))
        await asyncio.sleep(1)

        # Display both team
        await Pve_display_team(client, ctx, player, player_team, enemy_team)
        
        player_move = await Selection_phase(client, ctx, player, player_team, enemy_team, all_fighter)

        if(player_move == 'flee'):
            await ctx.send(_('<@{}> You flee the fight.').format(player.id))
            break
        
        # End Player_team turn
        # Apply the move

        await ctx.send(_('⚔ - Battle Phase'))
        await asyncio.sleep(1)

        await Battle_phase(client, ctx, player, player_move, player_team, enemy_team, all_fighter)

        # End of turn

        turn += 1

        # Reset stats

        for character in player_team:
            await asyncio.sleep(0)
            
            await Reset_stat(client, ctx, character)
        
        for enemy in enemy_team:
            await asyncio.sleep(0)

            await Reset_stat(client, ctx, enemy)
    
        # End of turn

    # End of Pve_Fight

    return
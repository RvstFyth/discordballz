'''
Manages the fight battle phase.

Last update: 18/06/19
'''

# Dependancies

import asyncio
from random import randint

# Utils

from cogs.utils.functions.readability.embed import Basic_embed
from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.commands.fight.displayer.display_fighter import Pve_display_fighter
from cogs.utils.functions.commands.fight.functions.damage_calculator import Damage_calculator
from cogs.utils.functions.commands.fight.displayer.display_move import Display_move

async def Battle_phase(client, ctx, player, player_move, player_team, enemy_team, all_fighter):
    '''
    `coroutine`

    Manages the battle phase.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `player` : must be `discord.Member` object.

    `player_move`: must be list object of player_move [[move, target]]

    `player_team` : must be list of `Character` objects.

    `enemy_team` : must be list of `Character` objects.

    `all_fighter` : must be list of `Character` objects.

    Return: discord.Message (battle informations)
    '''
    # Init

    _ = await Translate(client, ctx)
    fighter_move_id = 0
    npc_move_id = 0
    player_team_moves = ''
    npc_team_moves = ''
    npc_order = 0
    order = 0

    npc_team_alive = False
    player_team_alive = False
    for fighter in player_team:
        await asyncio.sleep(0)

        if(fighter.current_hp > 0 and fighter.flag != 3):  # fighter is alive
            player_team_alive = True

            fighter_move_list = player_move[fighter_move_id]  # Player_move = [[move, target], [move, target]], now fighter_move_list = [move,target]

            if fighter_move_list[1] == None:  # If there is no target
                fighter_choice, fighter_target = fighter_move_list[0], None
                player_team_moves += _('{} - {}**{}** {} to **{}** :\n').format(order+1, fighter.icon, fighter.name, fighter.type_icon, _('Himself'))

            else:
                fighter_choice, fighter_target = fighter_move_list[0], fighter_move_list[1]  # -1 because we have counted the list from 1 not from 0
                player_team_moves += _('{} - {}**{}** {} to {}**{}** {} :\n').format(order+1, fighter.icon, fighter.name, fighter.type_icon, fighter_target.icon, fighter_target.name, fighter_target.type_icon)

            if(fighter_choice == 1):
                # Sequence
                # Get the defenders
                fighter.flag = 0  # Changes the flag to 'attack'
                damages_done = await Damage_calculator(fighter, fighter_target, is_sequence = True)

                await fighter_target.inflict_damage(client, ctx, fighter, damages_done, player_team, enemy_team)

                player_team_moves += await Display_move(client, ctx, 'Sequence', '👊', damages_done, fighter, fighter_target)

            elif(fighter_choice == 2):
                # Ki charge
                fighter.flag = 1
                move = _('Ki charge')
                move_icon = ':fire:'
                missing_ki = fighter.max_ki - fighter.current_ki
                missing_ki = (10*missing_ki)/100  # 10% of missing ki

                ki_gain = randint(1, 5) + fighter.rarity_value + missing_ki

                ki_gain = int(ki_gain)
                fighter.current_ki += ki_gain

                if(fighter.current_ki > fighter.max_ki):
                    fighter.current_ki = fighter.max_ki

                player_team_moves += await Display_move(client, ctx, move, move_icon, 0, fighter, fighter, ki_gain = ki_gain)
            
            elif(fighter_choice == 3):
                # def
                # pass the fighter flag to 2
                fighter.flag = 2

                move = _('Defend')
                move_icon = '🏰'

                player_team_moves += await Display_move(client, ctx, move, move_icon, 0, fighter, fighter)
            
            else:
                # Ability
                    # Init
                
                fighter.flag = 0
                
                ability = fighter.ability_list[fighter_choice-4]  # -4 because we ignore the first 3 abilities (sequence, ki, flee) and we start counting at 0
                ability = ability()
                cost = ability.cost
                fighter.current_ki -= cost

                # We get the ability

                ability_ = await player_team[order].Use_ability(client, ctx, fighter, fighter_target, player_team, enemy_team, player_team_moves, fighter_choice-4)

                # Init ability

                await ability_.init(client, ctx, fighter)

                # Trigger effect

                player_team_moves = await ability_.trigger(client, ctx, fighter, fighter_target, player_team, enemy_team, player_team_moves, fighter_choice-4)

            # Increase fighter move to assign the move to the next fighter
            fighter_move_id += 1
            order += 1

    # Player team actions
    order = 1

    if(player_team_alive):
        player_team_display = Basic_embed(client, thumb = player.avatar_url)
        player_team_display.add_field(name = _('{}\'s team :').format(player.name), value = player_team_moves, inline = False)
        
        await ctx.send(embed = player_team_display)
    
    # Same for enemy team
    
    for npc in enemy_team:
        await asyncio.sleep(0)

        if(npc.current_hp > 0 and npc.flag != 3):  # If the NPC isn't dead or stunned
            # Get the npc move 
            npc_team_alive = True
            npc_move = await npc.artificial_intelligence(client, ctx, npc, enemy_team, player_team)
            npc_target = npc_move[1]
    
            if(npc_move[0] == 1):  # If the npc has chosen to use sequence
                # SEQUENCE MOVE

                npc_target = npc_move[1]   

                # Get the list of defenders
                defenders = []
                for character_a in player_team:
                    await asyncio.sleep(0)

                    if(character_a.flag == 2):  # If posture = defense
                        defenders.append(character_a)
                    
                    else:
                        pass
                
                if(len(defenders) == 0):  # If there is no defenders
                    pass
                
                else:
                    npc_target = defenders[randint(0, len(defenders)-1)]  # Pick a random defender as the target
                
                npc.flag = 0  # The npc is now in attack posture

                damages_done = await Damage_calculator(npc, npc_target, is_sequence = True) 

                await npc_target.inflict_damage(client, ctx, npc, damages_done, enemy_team, player_team)  # reverse player team and enemy team as the npc is part of the enemy team
                
                # move
                if npc_target == None:  # If there is no Target
                    npc_team_moves += _('{} - {}**{}** {} to **{}** : \n').format(npc_order+1, npc.icon, npc.name, npc.type_icon, _('Himself'))
                    
                else:
                    npc_team_moves += _('{} - {}**{}** {} to {}**{}** {} : \n').format(npc_order+1, npc.icon, npc.name, npc.type_icon, npc_target.icon, npc_target.name, npc_target.type_icon)

                npc_team_moves += await Display_move(client, ctx, 'Sequence', '👊', damages_done, npc, npc_target)
            
            elif(npc_move[0] == 2):  # If the npc decides to charge ki
                npc.flag = 1

                npc_move = _('Ki charge')
                npc_move_icon = ':fire:'

                missing_ki = npc.max_ki - npc.current_ki
                missing_ki = (10*missing_ki)/100  # 10 % of missing ki

                ki_gain = randint(1, 5) + npc.rarity_value + missing_ki

                ki_gain = int(ki_gain)

                npc.current_ki += ki_gain

                if(npc.current_ki > npc.max_ki):
                    npc.current_ki = npc.max_ki
                
                # move
                if npc_target == None:  # If there is no Target
                    npc_team_moves += _('{} - {}**{}** {} to **{}** : \n').format(npc_order+1, npc.icon, npc.name, npc.type_icon, _('Himself'))

                else:
                    npc_team_moves += _('{} - {}**{}** {} to {}**{}** {} : \n').format(npc_order+1, npc.icon, npc.name, npc.type_icon, npc_target.icon, npc_target.name, npc_target.type_icon)

                npc_team_moves += await Display_move(client, ctx, npc_move, npc_move_icon, 0, npc, npc, ki_gain = ki_gain)
            
            elif(npc_move[0] == 3):  # set a new defender
                npc.flag = 2

                npc_move = _('Defend')
                npc_move_icon = '🏰'

                # move
                if npc_target == None:  # If there is no Target
                    npc_team_moves += _('{} - {}**{}** {} to **{}** : \n').format(npc_order+1, npc.icon, npc.name, npc.type_icon, _('Himself'))
                
                else:
                    npc_team_moves += _('{} - {}**{}** {} to {}**{}** {} : \n').format(npc_order+1, npc.icon, npc.name, npc.type_icon, npc_target.icon, npc_target.name, npc_target.type_icon)
                
                npc_team_moves += await Display_move(client, ctx, npc_move, npc_move_icon, 0, npc, npc)
            
            else:  # If it's an ability
                ability = npc.ability_list[npc_move[0]-3]
                ability = ability()
                cost = ability.cost
                npc.current_ki -= cost
                npc_target = npc_move[1]

                # Get the list of defenders
                defenders = []
                for character_b in player_team:
                    await asyncio.sleep(0)

                    if(character_b.flag == 2):  # If posture = defense
                        defenders.append(character_b)
                    
                    else:
                        pass
                
                if(len(defenders) == 0):  # If there is no defenders
                    pass
                
                else:
                    npc_target = defenders[randint(0, len(defenders)-1)]  # Pick a random defender as the target
                
                # Now get the ability

                ability_ = await enemy_team[npc_order].Use_ability(client, ctx, npc, npc_target, enemy_team, player_team, npc_team_moves, npc_move[0]-3)

                # Init

                await ability_.init(client, ctx, npc)

                # Trigger

                # move
                if npc_move[1] == None:  # If there is no Target
                    npc_team_moves += _('{} - {}**{}** {} to **{}** : \n').format(npc_order+1, npc.icon, npc.name, npc.type_icon, _('Himself'))
                
                else:
                    npc_team_moves += _('{} - {}**{}** {} to {}**{}** {} : \n').format(npc_order+1, npc.icon, npc.name, npc.type_icon, npc_target.icon, npc_target.name, npc_target.type_icon)
                
                npc_team_moves = await ability_.trigger(client, ctx, npc, npc_target, enemy_team, player_team, npc_team_moves, npc_move[0]-3)
    
        npc_order += 1

    if(npc_team_alive):
        npc_display = Basic_embed(client)
        npc_display.add_field(name = _('Enemy team :'), value = npc_team_moves, inline = False)

        await ctx.send(embed = npc_display)

    # End Enemery_team turn

    return
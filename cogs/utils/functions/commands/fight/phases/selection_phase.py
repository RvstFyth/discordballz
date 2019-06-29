'''
Manages the fight selection phase.

Last update: 29/06/19
'''

# Dependancies

import asyncio

# Utils

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.commands.fight.functions.team_selection import Get_targetable
from cogs.utils.functions.commands.fight.displayer.display_fighter import Pve_display_fighter

# Waiters
from cogs.utils.functions.commands.fight.wait_for.wait_for_move import Wait_for_move
from cogs.utils.functions.commands.fight.wait_for.wait_for_first_turn import Wait_for_move_first_turn
from cogs.utils.functions.commands.fight.displayer.display_targets import Display_targets
from cogs.utils.functions.commands.fight.wait_for.wait_for_target import Wait_for_target

async def Selection_phase(client, ctx, player, player_team, enemy_team, all_fighter, turn):
    '''
    `coroutine`

    Allows the player to make his choices.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `player`: must be `discord.Member` object.

    `player_team` : must be list of `Character` objects.

    `enemy_team` : must be list of `Character` objects.

    `all_fighter` : must be list of `Character` objects.

    Return: list ([[move, target]])
    '''
    # Init

    _ = await Translate(client, ctx)

    player_move = []
    order = 1

    for fighter in player_team:
        await asyncio.sleep(0)
        
        if(fighter.current_hp > 0 and fighter.flag != 3):  # If fighter is alive and not stunned
            # Display fighter's turn

            await Pve_display_fighter(client, ctx, fighter, order)
            await asyncio.sleep(2)

            # Set fighter kit

            if(turn > 1):
                fighter_kit = _('`1. Sequence 👊` | `2. Ki charge 🔥` | `3. Defend 🏰`\n\n__Abilities__ :\n\n')
                
            else:
                fighter_kit = _('`1. Skip the turn ⏩` | `3. Defend 🏰`\n')
            
            if(turn > 1):
                fighter_ability_count = len(fighter.ability_list)

                if(fighter_ability_count > 0):
                    if(len(fighter.ability_list) >= 1):
                        ability_count = 4

                        for ability in fighter.ability_list:
                            await asyncio.sleep(0)

                            ability = ability()

                            fighter_kit += '`{}. {}`{} *({})*\n'.format(ability_count, ability.name, ability.icon, ability.cost)

                            # End turn
                            ability_count += 1
                    
                    else:
                        pass
                
            fighter_kit += _('\nTo **flee** the fight, type `\'flee\'`, to **take a look at** a specific unit, type `\'check {num}\'`')
            
            # Shows possible actions
            action_display = _('<@{}> Please select an action among the following for {}**{}**{} - {} / {} :fire:.\n{} ').format(player.id, fighter.icon, fighter.name, fighter.type_icon, fighter.current_ki, fighter.max_ki, fighter_kit)
            # Then ask action
        
            decision_made = False

            while not decision_made:
                await asyncio.sleep(0)

                await ctx.send(action_display)

                if(turn > 1):
                    correct_move, move = await Wait_for_move(client, player, fighter, all_fighter)  # Move : [action, target]
                    # We get the move

                    if(correct_move):
                        # init
                        teams_display = ''

                        # check if the move isn't a text
                        if(type(move) == str):  # if its a text
                            if(move.upper() == 'FLEE'):
                                return('flee')
                        
                        if(type(move) == list):  # if list
                            if(move[0].upper() == 'CHECK'):
                                await ctx.send(_('<@{}> Here are some infos about {}**{}**').format(player.id, move[1].icon, move[1].name))
                                await Pve_display_fighter(client, ctx, move[1], move[2])
                                await asyncio.sleep(2)
                                decision_made = False

                        # Check if the ability is not in cooldown
                        elif(move > 3 and move <= len(fighter.ability_list)+3):  # If the move is an ability
                            chosen_ability = fighter.ability_list[move-4]  # -4 because we remove the sequence, ki, and flee option and the list begins at 0
                            chosen_ability = chosen_ability()
                            
                            cooldown = chosen_ability.cooldown
                            need_target = chosen_ability.need_target

                            if(cooldown <= 0):  # If the ability is not on cooldown
                                if(fighter.current_ki >= chosen_ability.cost):  # If the fighter has enough ki to launch
                                    await chosen_ability.init(client, ctx, fighter)

                                    if not need_target:  # If the ability does not need a target
                                        player_move.append([move, None])  # None because it has not target

                                        decision_made = True  # The decision has been made, we can go out of the loop
                                    
                                    else:  # The ability needs a target, we ask for one

                                        targetable_list_ally, targetable_list_enemy = await Get_targetable(chosen_ability, player_team, enemy_team)  # get the targetable units
                                        
                                        # Displays the targets
                                        character_count = 1

                                        # Ally
                                        if(len(targetable_list_ally) > 0):  # if not empty
                                            
                                            teams_display = _('\n__Targets__ :\n🔵 - Your team :\n')
                                            
                                            character_count, teams_display = await Display_targets(teams_display, character_count, targetable_list_ally)
                                        
                                        # Enemy
                                        if(len(targetable_list_enemy) > 0):
                                            teams_display += '\n🔴 - Enemy team :\n' 
                                                
                                            character_count, teams_display = await Display_targets(teams_display, character_count, targetable_list_enemy)

                                        target_display = _('<@{}> Please select a target among the following for `{}`{} :\n{}').format(player.id, chosen_ability.name, chosen_ability.icon, teams_display)
                                        await ctx.send(target_display)

                                        targetable_list = targetable_list_ally + targetable_list_enemy  # fusion the list 

                                        # then pass the list to wait for
                                        correct_target, target = await Wait_for_target(client, player, fighter, targetable_list)

                                        if correct_target:
                                            # Check if the ability can be used on an anlly
                                            player_move.append([move, target])
                                            decision_made = True
                                        
                                        else:
                                            decision_made = False
                                
                                else:  # The fighter has not enough ki
                                    await ctx.send(_('<@{}> 🔥 ⚠ Not enough ki : {} / {}').format(player.id, fighter.current_ki, chosen_ability.cost))
                                    await asyncio.sleep(2)

                                    decision_made = False
                                    pass
                            
                            else:  # Ability on cooldown
                                await ctx.send(_('<@{}> ⏳ ⚠ Ability on cooldown : {} turns.').format(player.id, chosen_ability.cooldown))
                                await asyncio.sleep(2)

                                decision_made = False
                                pass

                        else:  # If its not an ability, its ok
                            if(move == 1):
                                # get the targets
                                targetable_list_ally, targetable_list_enemy = await Get_targetable('sequence', player_team, enemy_team)  # get the targetable units
                                        
                                # Displays the targets
                                character_count = 1

                                # Ally
                                if(len(targetable_list_ally) > 0):  # if not empty
                                    
                                    teams_display = _('\n__Targets__ :\n🔵 - Your team :\n')
                                    
                                    character_count, teams_display = await Display_targets(teams_display, character_count, targetable_list_ally)
                                
                                # Enemy
                                if(len(targetable_list_enemy) > 0):
                                    teams_display += '\n🔴 - Enemy team :\n' 
                                        
                                    character_count, teams_display = await Display_targets(teams_display, character_count, targetable_list_enemy)

                                target_display = _('<@{}> Please select a target among the following for `Sequence 👊` :\n{}').format(player.id, teams_display)
                                await ctx.send(target_display)

                                targetable_list = targetable_list_ally + targetable_list_enemy  # fusion the list 

                                correct_target, target = await Wait_for_target(client, player, fighter, targetable_list)  # get the new targets

                                if correct_target:
                                    player_move.append([move, target])
                                    decision_made = True
                                
                                else:  # If target is incorrect
                                    decision_made = False

                            elif(move == 2 or move == 3):
                                if(move == 2):  # ki 
                                    move = [2, None]
                                    player_move.append(move)
                                    decision_made = True

                                if(move == 3):  # def
                                    move = [3, None]
                                    player_move.append(move)
                                    decision_made = True

                    else:  # If move is not correct we re-ask
                        if(move == 'flee'):  # In that case it's an error raised by Asyncio.TimeOutError
                            return('flee')
                        
                        else:
                            pass 
                
                else:  # if turn 1
                    correct_move, move = await Wait_for_move_first_turn(client, player, fighter, all_fighter)

                    if correct_move:

                        # check if the move isn't a text
                        if(type(move) == str):  # if its a text
                            if(move.upper() == 'FLEE'):
                                return('flee')
                        
                        elif(type(move) == list):  # if list
                            if(move[0].upper() == 'CHECK'):
                                await ctx.send(_('<@{}> Here are some infos about {}**{}**').format(player.id, move[1].icon, move[1].name))
                                await Pve_display_fighter(client, ctx, move[1], move[2])
                                await asyncio.sleep(2)
                                decision_made = False
                        
                        else:
                            if(move == 1):
                                player_move.append(['skip', None])
                                decision_made = True
                            
                            if(move == 3):
                                player_move.append([3, None])
                                decision_made = True
        else:
            pass

        order += 1
    
    return(player_move)
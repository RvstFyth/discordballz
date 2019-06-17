'''
Manages the fight selection phase.

Last update: 17/06/19
'''

# Dependancies

import asyncio

# Utils

from cogs.utils.functions.translation.gettext_config import Translate

from cogs.utils.functions.commands.fight.displayer.display_fighter import Pve_display_fighter

# Waiters
from cogs.utils.functions.commands.fight.wait_for.wait_for_move import Wait_for_move
from cogs.utils.functions.commands.fight.wait_for.wait_for_target import Wait_for_target

async def Selection_phase(client, ctx, player, player_team, enemy_team, all_fighter):
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

            # Set fighter kit

            fighter_kit = _('`1. Sequence 👊` | `2. Ki charge 🔥` | `3. Flee 🏃`\n')
            fighter_ability_count = len(fighter.ability_list)

            if(fighter_ability_count > 0):
                if(len(fighter.ability_list) >= 1):
                    ability_count = 4

                    for ability in fighter.ability_list:
                        await asyncio.sleep(0)

                        ability = ability()

                        fighter_kit += '`{}. {}`{} *({})* | '.format(ability_count, ability.name, ability.icon, ability.cost)

                        # End turn
                        ability_count += 1
                
                else:
                    pass
            
            # Displays the targets

            teams_display = _('\n__Targets__ :\n🔵 - Your team : ')

            character_count = 1
            
            # Player team

            for fighter_member in player_team:
                await asyncio.sleep(0)

                if(fighter_member.current_hp <= 0):
                    teams_display += '{}.💀**{}** {} | '.format(character_count, fighter_member.name, fighter_member.type_icon)
                else:
                    teams_display += '{}. {}**{}** {} | '.format(character_count, fighter_member.icon, fighter_member.name, fighter_member.type_icon)
                character_count += 1
            
            teams_display += '\n🔴 - Enemey team : '
            
            # Enemy team

            for enemy_member in enemy_team:
                await asyncio.sleep(0)

                if(enemy_member.current_hp <= 0):
                    teams_display += '{}.💀**{}** {} | '.format(character_count, enemy_member.name, enemy_member.type_icon)
                else:
                    teams_display += '{}. {}**{}** {} | '.format(character_count, enemy_member.icon, enemy_member.name, enemy_member.type_icon)

                character_count += 1

            # Show the possible actions :

            action_display = _('<@{}> Please select an action among the following for **{}**{}.\n{}').format(player.id, fighter.name, fighter.type_icon, fighter_kit)

            # Then ask action
        
            decision_made = False

            while not decision_made:
                await asyncio.sleep(0)

                await ctx.send(action_display)

                correct_move, move = await Wait_for_move(client, player, fighter, all_fighter)  # Move : [action, target]
                # We get the move

                if(correct_move):
                    # Check if the ability is not in cooldown
                    if(move > 3 and move <= len(fighter.ability_list)+3):  # If the move is an ability
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
                                    target_display = _('<@{}> Please select a target among the following for `{}`{} :\n{}').format(player.id, chosen_ability.name, chosen_ability.icon, teams_display)
                                    await ctx.send(target_display)

                                    correct_target, target = await Wait_for_target(client, player, fighter, all_fighter)

                                    if correct_target:
                                        # Check if the ability can be used on an anlly
                                        if chosen_ability.can_target_ally:  # If it can, its ok
                                            player_move.append([move, target])
                                            decision_made = True

                                        elif(chosen_ability.can_target_ally == False and target <= len(player_team)):  # Else we re-ask
                                            decision_made = False
                                            await ctx.send(_('<@{}> You cannot target an ally with this ability.').format(player.id))
                                        
                                        else:  # If the target is correct
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
                            target_display = _('<@{}> Please select a target among the following for `Sequence 👊` :\n{}').format(player.id, teams_display)
                            await ctx.send(target_display)
                            correct_target, target = await Wait_for_target(client, player, fighter, all_fighter)

                            if correct_target:
                                if(target > len(player_team)):
                                    player_move.append([move, target])
                                    decision_made = True

                                else:  # If target is ally
                                    await ctx.send(_('<@{}> You cannot target an ally with this ability.').format(player.id))
                                    decision_made = False
                            
                            else:  # If target is incorrect
                                decision_made = False

                        elif(move == 2 or move == 3):
                            if(move == 2):
                                move = [2, None]
                                player_move.append(move)
                                decision_made = True

                            if(move == 3):
                                return('flee')

                else:  # If move is not correct we re-ask
                    if(move == 'flee'):  # In that case it's an error raised by Asyncio.TimeOutError
                        return('flee')
                    
                    else:
                        pass 

        else:
            pass

        order += 1
    
    return(player_move)
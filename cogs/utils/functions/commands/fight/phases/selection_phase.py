'''
Manages the fight selection phase.

Last update: 29/05/19
'''

# Dependancies

import asyncio

# Utils

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.commands.fight.wait_for.wait_for_move import Wait_for_move
from cogs.utils.functions.commands.fight.displayer.display_fighter import Pve_display_fighter

async def Selection_phase(client, ctx, player, player_team, enemy_team, all_fighter):
    '''
    `coroutine`

    Allows the player to make his choices.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `player`: must be `discord.Member` object.

    `player_team` : must be list of `Fighter` objects.

    `enemy_team` : must be list of `Fighter` objects.

    `all_fighter` : must be list of `Fighter` objects.

    Return: list ([[move, target]])
    '''
    # Init

    _ = await Translate(client, ctx)

    player_move = []

    for fighter in player_team:
        await asyncio.sleep(0)
        
        if(fighter.stat.current_hp > 0):
            # Display fighter's turn

            await Pve_display_fighter(client, ctx, fighter)

            # Set fighter kit

            fighter_kit = _('`1. Sequence` | `2. Ki charge` | `3. Flee` | ')
            fighter_ability_count = fighter.stat.ability_count 

            if(fighter_ability_count > 0):
                if(fighter_ability_count == 1):
                    fighter_kit += '`4. {}` | '.format(fighter.stat.first_ability_name)
                
                elif(fighter_ability_count == 2):
                    fighter_kit += '`4. {}` | '.format(fighter.stat.first_ability_name)
                    fighter_kit += '`5. {}` | '.format(fighter.stat.second_ability_name)
                
                elif(fighter_ability_count == 3):
                    fighter_kit += '`4. {}` | '.format(fighter.stat.first_ability_name)
                    fighter_kit += '`5. {}` | '.format(fighter.stat.second_ability_name)
                    fighter_kit += '`6. {}` | '.format(fighter.stat.third_ability_name)
                
                elif(fighter_ability_count == 4):
                    fighter_kit += '`4. {}` | '.format(fighter.stat.first_ability_name)
                    fighter_kit += '`5. {}` | '.format(fighter.stat.second_ability_name)
                    fighter_kit += '`6. {}` | '.format(fighter.stat.third_ability_name)
                    fighter_kit += '`7. {}` | '.format(fighter.stat.fourth_ability_name)
                
                else:
                    pass
            
            # Displays the targets

            fighter_kit += _('\n\n__Targets__ :\nYour team : ')

            character_count = 1
            
            # Player team

            for fighter_member in player_team:
                await asyncio.sleep(0)

                fighter_kit += '{}. **{}** {} | '.format(character_count, fighter_member.stat.name, fighter_member.stat.type)
                character_count += 1
            
            fighter_kit += '\nEnemey team : '
            
            # Enemy team

            for enemy_member in enemy_team:
                await asyncio.sleep(0)

                fighter_kit += '{}. **{}** {} | '.format(character_count, enemy_member.stat.name, enemy_member.stat.type)
                character_count += 1

            # Show the possible actions :

            action_display = _('<@{}> Please select an action and a target among the following for **{}** {}.\n(type their number right above : like `[action number]`  `[target number]`) :\n\n{}').format(player.id, fighter.stat.name, fighter.stat.type, fighter_kit)

            # Then ask action
        
            decision_made = False

            while not decision_made:
                await ctx.send(action_display)

                correct_move, move = await Wait_for_move(client, player, fighter, all_fighter)  # Move : [action, target]

                # We get the move

                if(correct_move):
                    # Check if the ability is not in cooldown
                    if(move[0] > 3):  # If the move is an ability
                        if(move[0] == 4):  # If its the first ability
                            cooldown = fighter.stat.first_ability_cooldown  # Get the ability current cooldown

                            if(cooldown <= 0):  # If its not on cooldown, we add it to the action to perform
                                player_move.append(move)

                                decision_made = True
                                
                            else:  # If the ability is on cd
                                decision_made = False
                                await ctx.send(_('<@{}> 🚫 ⚠ Ability on cooldown : {} turns.').format(player.id, cooldown))
                                await asyncio.sleep(2)
                                pass
                        
                        elif(move[0] == 5):  # If its the first ability
                            cooldown = fighter.stat.second_ability_cooldown  # Get the ability current cooldown

                            if(cooldown <= 0):  # If its not on cooldown, we add it to the action to perform
                                player_move.append(move)

                                decision_made = True
                                
                            else:  # If the ability is on cd
                                decision_made = False
                                await ctx.send(_('<@{}> 🚫 ⚠ Ability on cooldown : {} turns.').format(player.id, cooldown))
                                await asyncio.sleep(2)
                                pass
                        
                        elif(move[0] == 6):  # If its the first ability
                            cooldown = fighter.stat.third_ability_cooldown  # Get the ability current cooldown

                            if(cooldown <= 0):  # If its not on cooldown, we add it to the action to perform
                                player_move.append(move)

                                decision_made = True
                                
                            else:  # If the ability is on cd
                                decision_made = False
                                await ctx.send(_('<@{}> 🚫 ⚠ Ability on cooldown : {} turns.').format(player.id, cooldown))
                                await asyncio.sleep(2)
                                pass

                        elif(move[0] == 7):  # If its the first ability
                            cooldown = fighter.stat.fourth_ability_cooldown  # Get the ability current cooldown

                            if(cooldown <= 0):  # If its not on cooldown, we add it to the action to perform
                                player_move.append(move)

                                decision_made = True
                                
                            else:  # If the ability is on cd
                                decision_made = False
                                await ctx.send(_('<@{}> 🚫 ⚠ Ability on cooldown : {} turns.').format(player.id, cooldown))
                                await asyncio.sleep(2)
                                pass

                    else:  # If its not an ability, its ok
                        decision_made = True
                        if(len(move) == 1):
                            move = [2, 0]
                            
                        player_move.append(move)

                else:  # If move is not correct we re-ask
                    pass 
            
            # If the player wants to flee :

            if(move[0] == 3):
                return('flee')

        else:
            pass
    
    return(player_move)
'''
Manages the fight battle phase.

Last update: 29/05/19
'''

# Dependancies

import asyncio
from random import randint

# Utils

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.commands.fight.displayer.display_fighter import Pve_display_fighter

async def Battle_phase(client, ctx, player_move, player_team, enemy_team, all_fighter):
    '''
    `coroutine`

    Manages the battle phase.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `player_move`: must be list object of player_move [[move, target]]

    `player_team` : must be list of `Fighter` objects.

    `enemy_team` : must be list of `Fighter` objects.

    `all_fighter` : must be list of `Fighter` objects.

    Return: discord.Message (battle informations)
    '''
    # Init

    _ = await Translate(client, ctx)
    fighter_move_id = 0

    for fighter in player_team:
        await asyncio.sleep(0)

        fighter_move_list = player_move[fighter_move_id]  # Player_move = [[move, target], [move, target]], now fighter_move_list = [move,target]

        fighter_choice, fighter_target = fighter_move_list[0], all_fighter[fighter_move_list[1] - 1]  # -1 because we have counted the list from 1 not from 0

        # 7 possible choices

        await ctx.send(_('**{}** {}\'s action performed on **{}** {} :').format(fighter.stat.name, fighter.stat.type, fighter_target.stat.name, fighter.stat.type))

        if(fighter_choice == 1):
            # Sequence
            if(fighter_move_list[1] <= len(player_team)):
                # If the player targeted a member of his team with sequence we do nothing
                await ctx.send(_('**{}** {} tried to attack a member of his own team !').format(fighter.stat.name, fighter.stat.type))
                pass
            
            else:  # Otherwise we hit
                # Get the defenders
                defenders = []
                for enemy in enemy_team:
                    await asyncio.sleep(0)
                    
                    if(enemy.posture == 2):
                        defenders.append(enemy)
                    
                    else:
                        pass

                if(len(defenders) == 0):
                    pass
                
                else:
                    fighter_target = defenders[randint(0, len(defenders)-1)]  # Select a random defender as the new target

                fighter_target.stat.current_hp -= fighter.stat.damage_max
                await Pve_display_fighter(client, ctx, fighter_target)
        
        if(fighter_choice == 2):
            # Ki charge
            pass
        
        if(fighter_choice == 3):
            # Flee
            pass
        
        if(fighter_choice == 4):
            # Ability 1
            await player_team[0].stat.First_ability(client, ctx, fighter_target, player_team, enemy_team)
        
        if(fighter_choice == 5):
            # Ability 2
            pass
        
        if(fighter_choice == 6):
            # Ability 3
            pass
        
        if(fighter_choice == 7):
            # Ability 4
            pass

        # Increase fighter move to assign the move to the next fighter
        fighter_move_id += 1

    # Same for enemy team

    # End Enemery_team turn
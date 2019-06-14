'''
Manages the fight battle phase.

Last update: 13/06/19
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
    player_team_moves = ''
    enemy_team_moves = ''
    order = 0

    for fighter in player_team:
        await asyncio.sleep(0)

        fighter_move_list = player_move[fighter_move_id]  # Player_move = [[move, target], [move, target]], now fighter_move_list = [move,target]

        if fighter_move_list[1] == None:  # If there is no target
            fighter_choice, fighter_target = fighter_move_list[0], None
            player_team_moves += _('{} - **{}** {} to **{}** :\n').format(order+1, fighter.name, fighter.type_icon, _('Himself'))

        else:
            fighter_choice, fighter_target = fighter_move_list[0], all_fighter[fighter_move_list[1] - 1]  # -1 because we have counted the list from 1 not from 0
            player_team_moves += _('{} - **{}** {} to **{}** {} :\n').format(order+1, fighter.name, fighter.type_icon, fighter_target.name, fighter_target.type_icon)

        if(fighter_choice == 1):
            # Sequence
            # Get the defenders
            defenders = []
            for enemy in enemy_team:
                await asyncio.sleep(0)
                
                if(enemy.flag == 2):
                    defenders.append(enemy)
                
                else:
                    pass

            if(len(defenders) == 0):
                pass
            
            else:
                fighter_target = defenders[randint(0, len(defenders)-1)]  # Select a random defender as the new target

            fighter.flag = 0
            damages_done = await Damage_calculator(fighter, fighter_target, is_sequence = True)
            fighter_target.current_hp -= damages_done

            player_team_moves += await Display_move(client, ctx, 'Sequence', '👊', damages_done, fighter, fighter_target)

            if(fighter_target.current_hp <= 0):
                fighter_target.current_hp = 0
                await fighter_target.On_being_killed(fighter_target, player_team, enemy_team)
                await fighter.On_killing(fighter, player_team, enemy_team)
    
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
            # Flee
            pass
        
        else:
            # Ability
                # Init
            
            ability = fighter.ability_list[fighter_choice-4]  # -4 because we ignore the first 3 abilities (sequence, ki, flee) and we start counting at 0
            cost = ability.cost
            fighter.current_ki -= cost

            # We get the ability

            ability_ = await player_team[order].Use_ability(client, ctx, fighter, fighter_target, player_team, enemy_team, player_team_moves, fighter_choice-4)

            # Init ability

            await ability_.init(client, ctx, fighter)

            # Trigger effect

            player_team_moves = await ability_.trigger(client, ctx, fighter, fighter_target, player_team, enemy_team, player_team_moves, fighter_choice-4)

            # Put the stuff under into a function
            '''# Check healths
            # If they're ded
            if(fighter.current_hp <= 0):
                await fighter.On_being_killed(fighter, player_team, enemy_team)  # Trigger the On_death effect
            
            elif(fighter_target.current_hp <= 0):
                await fighter_target.On_being_killed(fighter_target, player_team, enemy_team)

            # If they're alive
            if(fighter.current_hp > 0):'''


        # Increase fighter move to assign the move to the next fighter
        fighter_move_id += 1
        order += 1

    # Player team actions
    order = 1

    player_team_display = Basic_embed(client, thumb = player.avatar_url)
    player_team_display.add_field(name = _('{}\'s team :').format(player.name), value = player_team_moves, inline = False)
    
    await ctx.send(embed = player_team_display)
    
    # Same for enemy team

    # End Enemery_team turn

    return
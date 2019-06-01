'''
Manages the trigger phase of the fight.

Last update: 01/06/19
'''

# Dependancies

import asyncio

# Utils

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.readability.embed import Basic_embed

async def Triggers_phase(client, ctx, player_team, enemy_team):
    '''
    `coroutine`

    Trigger the fighters effects.

    `player_team` : must be list of `Fighter` objects.

    `enemy_team` : must be list of `Fighter` objects.

    Return: void
    '''

    # Init

    _ = await Translate(client, ctx)

    # Enemy team

    enemy_team_display = ''
    enemy_effects = False
    enemy_team_triggers = ''
    enemy_count = 1

        # Dot
    enemy_dot = False
    enemy_dot_display = _('\n__Dot__ : ') # List the enemy dots
    enemy_dot_stack_display = _('\n__Stack__ : ')
    enemy_dot_damage_display = _('\n__Damages__ : ')
    enemy_dot_duration_display = _('\n__Remaining__ : ')

    enemy_dot_total_stack = 0
    enemy_dot_total_duration = 0
    enemy_dot_total_damage = 0

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
        enemy_effects, enemy_dot = False, False  # If the enemy has active effects pass to true
        
        # Dot
        for dot in enemy.dot :
            await asyncio.sleep(0)

            # If one of the effect is over
            if(dot.duration <= 0):
                enemy.dot.remove(dot)

                if(len(enemy.dot) == 0):
                    break

            # If the effect is not over, apply the effect

            print(dot.stack)
            enemy_effects = True
            enemy_dot = True

            await dot.apply_dot(enemy)

            # The enemy has an effect on him, we display
            
            enemy_dot_display += '`{}`{} | '.format(dot.dot_name, dot.dot_icon)
            enemy_dot_total_stack += dot.stack
            enemy_dot_total_damage += dot.tick_damage
            enemy_dot_total_duration += dot.duration

    # End
    # Display
    if enemy_effects:
        if enemy_dot :
            
            # DOT
            enemy_team_triggers += _('\n------------ Damages over time ------------')
            enemy_dot_stack_display += '{:,}'.format(enemy_dot_total_stack)
            enemy_dot_damage_display += '**{:,}**'.format(enemy_dot_total_damage)
            enemy_dot_duration_display += '{:,}'.format(enemy_dot_total_duration)
            
            # Dot name
            enemy_team_triggers += enemy_dot_display
            # Dot stack
            enemy_team_triggers += enemy_dot_stack_display
            # Dot damages
            enemy_team_triggers += enemy_dot_damage_display
            # Dot duration
            enemy_team_triggers += enemy_dot_duration_display

            enemy_team_display += _('🔴 - Enemy Team :\n')+ enemy_team_triggers
        
            # Send
            await ctx.send(enemy_team_display)

        enemy_count += 1
'''
Manages the trigger phase of the fight.

Last update: 31/05/19
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

    enemy_team_display = Basic_embed(client)
    enemy_effects = False
    enemy_team_triggers = ''
    enemy_count = 1

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
        enemy_effects = False  # If the enemy has active effects pass to true

        enemy_team_triggers += _('{} - **{}** {} :\n').format(enemy_count, enemy.stat.name, enemy.stat.type)
        
        # Dot
        for dot in enemy.dot :
            await asyncio.sleep(0)

            # If one of the effect is over
            if(dot.duration <= 0):
                enemy.dot.remove(dot)

                if(len(enemy.dot) == 0):
                    break

            # If the effect is not over, apply the effect

            enemy_effects = True
            await dot.apply_dot(enemy)

            enemy_team_triggers += _('__Dot__ : `{}` {}\n__Stack__ : {:,}\n__Damages__ : **{:,}**\n__Remaining__ : {:,} Turns\n\n').format(dot.dot_name, dot.dot_icon, dot.stack, dot.tick_damage, dot.duration)
            
        # End
        
        if enemy_effects:
            enemy_team_display.add_field(name = 'Enemy team :', value = enemy_team_triggers, inline = False)
            await ctx.send(embed = enemy_team_display)

        enemy_count += 1
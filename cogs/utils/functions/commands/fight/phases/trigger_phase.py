'''
Manages the trigger phase of the fight.

Last update: 29/05/19
'''

# Dependancies

import asyncio

async def Triggers_phase(player_team, enemy_team):
    '''
    `coroutine`

    Trigger the fighters effects.

    `player_team` : must be list of `Fighter` objects.

    `enemy_team` : must be list of `Fighter` objects.

    Return: void
    '''

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
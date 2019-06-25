'''
Return the targetable units

Last update: 25/06/19
'''

# dependancies

import asyncio

async def Get_targetable(ability, allies, enemies):
    '''
    `coroutine`

    `ability` : must be `Ability` object, allows us to know the targeting conditions.

    `alies` : must be a list of `Character` object, represents the allies.

    `enemies` : same as `allies` but for enemies.

    Return a list of targetable units

    Return: lists of objects : [list[Allies], list[Enemies]]
    '''

    # init

    ally_list, enemy_list = [], []

    # ally

    if(ability != 'sequence'):  # if its not sequence (sequence cannot target allies)
        if(ability.can_target_ally):
            for ally in allies:
                await asyncio.sleep(0)

                ally_list.append(ally)
    
    # enemy

    if(ability != 'sequence'):
        if(ability.can_target_enemy):
            for enemy in enemies:
                await asyncio.sleep(0)

                enemy_list.append(enemy)
            
            # now get the enemy defenders
            defender_list = []

            for defender in enemy_list:
                await asyncio.sleep(0)

                if(defender.flag == 2):  # if defending
                    defender_list.append(defender)
                
                else:
                    pass
        
    else:  # if sequence
        for enemy in enemies:
            await asyncio.sleep(0)

            enemy_list.append(enemy)
        
        # now get the enemy defenders
        defender_list = []

        for defender in enemy_list:
            await asyncio.sleep(0)

            if(defender.flag == 2):  # if defending
                defender_list.append(defender)
            
            else:
                pass
        
    # now replace the nemy team if there is defenders

    if(len(defender_list) > 0):  # if not empty
        enemy_list = defender_list
    
    return(ally_list, enemy_list)
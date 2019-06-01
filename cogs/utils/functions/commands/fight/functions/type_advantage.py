'''
Manages the type advantages

Last update: 31/05/19
'''

# Dependancies

import asyncio

async def Is_type_advantaged(fighter, target):
    '''
    `coroutine`

    Tells elif the fighter has the type advantage on its target.

    `fighter` : must be `Character` object.

    `target` : must be `Character` object.

    Return: int (0 : nothing, 1 : advantaged, 2: disadvantaged)
    '''

    # Init

    fighter_type = fighter.type

    target_type = target.type

    # Advantages 

    if fighter_type == 3 and target_type == 4:
        # Phy > Int
        return(1)
    
    elif fighter_type == 4 and target_type == 1:
        # Int > Teq
        return(1)
    
    elif fighter_type == 0 and target_type == 2:
        # Agl > Str
        return(1)
    
    elif fighter_type == 2 and target_type == 3:
        # Str > Phy
        return(1)
    
    elif fighter_type == 1 and target_type == 0:
        # Teq > Agl
        return(1)

    # Disadvantage

    elif fighter_type == 3 and target_type == 2 :
        # Phy < Str
        return(2)
    
    elif fighter_type == 4 and target_type == 3:
        # Int < Phy
        return(2)
    
    elif fighter_type == 1 and target_type == 4:
        # Teq < Int
        return(2)
    
    elif fighter_type == 0 and target_type == 1:
        # Agl < Teq
        return(2)
    
    elif fighter_type == 2 and target_type == 0:
        # Str < Agl
        return(2)

    else:
        return(0)
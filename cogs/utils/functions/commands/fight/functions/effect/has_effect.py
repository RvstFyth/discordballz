'''
Manages the Has_effect functions.

Last update: 03/06/19
'''

# Dependancies

import asyncio

async def Has_buff(character, buff):
    '''
    `coroutine`

    Return True if the passed `Character` instance has the passed `Buff` object.

    `character` : must be `Character` instance.

    `buff` : must be `Buff` object.

    Return: bool
    '''

    # Init

    has_buff = False

    # Looking for the buff

    for char_buff in character.buff:
        await asyncio.sleep(0)

        if(char_buff.id == buff.id):
            has_buff = True
            break
    
    return(has_buff)

async def Has_debuff(character, debuff):
    '''
    `coroutine`

    Return True if the passed `Character` instance has the passed `Debuff` object.

    `character` : must be `Character` instance.

    `debuff` : must be `Debuff` object.

    Return: bool
    '''

    # Init

    has_debuff = False

    # Looking for the debuff

    for char_debuff in character.debuff:
        await asyncio.sleep(0)

        if(char_debuff.id == debuff.id):
            has_debuff = True
            break
    
    return(has_debuff)
        
async def Has_dot(character, dot):
    '''
    `coroutine`

    Return True if the passed `Character` instance has the passed `Dot` object.

    `character` : must be `Character` instance.

    `dot` : must be `Dot` object.

    Return: bool
    '''

    # Init

    has_dot = False

    # Looking for the dot

    for char_dot in character.dot:
        await asyncio.sleep(0)

        if(char_dot.id == dot.id):
            has_dot = True
            break

    return(has_dot)
'''
Manage the effect getters

Last update: 03/06/19
'''

# Dependancies

import asyncio

async def Get_buff(character, buff):
    '''
    `coroutine`

    Get a buff that is present on a character. Better test if the character has
    the buff you are looking for using an `await Has_buff()` before calling this 
    function.

    `character` : must be `Character` object.

    `buff` : must be `Buff` object.

    Return: `Buff` object or `None` if not found.
    '''

    # Init

    buff_object = None

    # Find it

    for char_buff in character.buff:
        await asyncio.sleep(0)

        if(char_buff.id == buff.id):
            buff_object = char_buff
            break

    return(buff_object)

async def Get_debuff(character, debuff):
    '''
    `coroutine`

    Get a debuff that is present on a character. Better test if the character has
    the debuff you are looking for using an `await Has_debuff()` before calling this 
    function.

    `character` : must be `Character` object.

    `debuff` : must be `Debuff` object.

    Return: `Debuff` object or `None` if not found.
    '''

    # Init

    debuff_object = None

    # Find it

    for char_debuff in character.debuff:
        await asyncio.sleep(0)

        if(char_debuff.id == debuff.id):
            debuff_object = char_debuff
            break

    return(debuff_object)

async def Get_dot(character, dot):
    '''
    `coroutine`

    Get a dot that is present on a character. Better test if the character has
    the dot you are looking for using an `await Has_dot()` before calling this 
    function.

    `character` : must be `Character` object.

    `dot` : must be `Dot` object.

    Return: `Dot` object or `None` if not found.
    '''

    # Init

    dot_object = None

    # Find it

    for char_dot in character.dot:
        await asyncio.sleep(0)

        if(char_dot.id == dot.id):
            dot_object = char_dot
            break

    return(dot_object)
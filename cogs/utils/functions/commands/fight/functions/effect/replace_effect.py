'''
Manages how the effects are replaced.

Last update: 03/06/19
'''

# Dependancies

import asyncio

# Utils

from cogs.utils.functions.commands.fight.functions.effect.has_effect import Has_dot

async def Replace_dot(character, dot_replacer):
    '''
    `coroutine`

    This function replace dot with the same id of the passed `dot_replacer`.

    `character` : must be `Character` object.

    `dot_replacer` : must be `Dot` object.

    Return: void
    '''

    # Init

    has_dot = await Has_dot(character, dot_replacer)

    if has_dot:
        for dot in character.dot:
            await asyncio.sleep(0)

            if(dot.id == dot_replacer.id):
                character.dot.remove(dot)
                character.dot.append(dot_replacer)
    
    return
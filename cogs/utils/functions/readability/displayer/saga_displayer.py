'''
Manages the sagas.

Last update: 30/06/19
'''

# dependancies

import asyncio

# utils

from cogs.utils.functions.translation.gettext_config import Translate

async def Get_Saga(client, ctx, character):
    '''
    `coroutine`

    Return the saga name of the character.
    
    `client` : must be `discord.Client`

    `ctx` : must be `discord.ext.commands.Context`

    `character` : must be `Character` instance.

    Return: Saga name
    '''

    # init

    _ = await Translate(client, ctx)

    # list all the sagas

    saga = [_('Saiyan')]
    saga_name = 'Unknown'

    # Update character saga
    
    if character.saga <= len(saga):  # if the saga is registered
        saga_name = saga[character.saga]
    
    else:
        pass

    return(saga_name)
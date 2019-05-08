'''
Manages the player's checks.

Last update: 08/05/19
'''

# Dependancies

import asyncio, time

# Translation

from cogs.utils.functions.translation.gettext_config import Translate

# Database

from cogs.utils.functions.database.select.player.player import Select_player_name

async def Is_registered(ctx):
    '''
    Checks if the player is already registered in the database. If not, it returns `False` and invites him to do so.

    Otherwise, it returns `True`.

    `ctx` : must be `discord.ext.commands.Context` object.

    Return: bool
    '''

    # Init
    # This represents the bot, it works like a discord.Client object, only use it when you can get the original discord.Client object

    client = ctx.bot
    _ = await Translate(client, ctx)
    player = ctx.message.author
    player_name = await Select_player_name(client, player)

    if(player_name == None):
        await ctx.send(_('<@{}> You must be registered to perform this action, to do so, use the `d!start` command.').format(player.id))
        
        return(False)
    
    else:
        return(True)

async def Is_not_registered(ctx):
    '''
    This function works like the `Is_registered` function, but it returns `True` if the player isn't registered and `False` if he is.

    `ctx` : must be `discord.ext.commands.Context` object.

    Return: bool
    '''

    # Init

    client = ctx.bot
    _ = await Translate(client, ctx)
    player = ctx.message.author
    player_name = await Select_player_name(client, player)

    if(player_name == None):
        return(True)
    
    else:
        await ctx.send(_('<@{}> You\'re already registered.').format(player.id))
        
        return(False)
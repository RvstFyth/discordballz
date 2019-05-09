'''
Manages the displaying of the profile.

Last update: 09/05/19
'''

# Dependancies

import discord, asyncio, time

# Translation

from cogs.utils.functions.translation.gettext_config import Translate

# Config

from cogs.utils.functions.readability.embed import Basic_embed

async def Display_profile(client, ctx, player):
    '''
    Displays the passed player profile.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `player` : must be `discord.Member` object.

    Return: void : sends a message in `discord.Embed` form
    '''

    # Init

    _ = await Translate(client, ctx)
    player_ava = player.avatar_url

    # Set up the embed

    profile = Basic_embed(client, _('{}\'s profile').format(player.name), thumb = player_ava)
    
    # Send

    await ctx.send(embed = profile)
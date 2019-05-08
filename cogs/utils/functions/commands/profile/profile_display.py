'''
Manages the displaying of the profile.

Last update: 08/05/19
'''

# Dependancies

import discord, asyncio, time

# Translation

from cogs.utils.functions.translation.gettext_config import Translate

# Config

from cogs.utils.functions.readability.embed import Basic_embed

# Check

from cogs.utils.functions.check.player.player_checks import Is_not_registered

async def Display_profile(client, ctx, player):
    '''
    Displays the passed player profile.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `player` : must be `discord.Member` object.

    Return: void : sends a message in `discord.Embed` form
    '''

    # Init
        # We check if the player is already registered or not, if not, we don't display anything.
    
    registered = await Is_not_registered(ctx)

    if(registered):  # Is_not_registered is reversed, it returns False if the player is registered and True if not
        return

    _ = await Translate(client, ctx)
    player_ava = player.avatar_url

    # Set up the embed

    profile = Basic_embed(client, _('{}\'s profile').format(player.name), thumb = player_ava)
    
    # Send

    await ctx.send(embed = profile)
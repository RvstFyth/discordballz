'''
Manages the displaying of the profile.

Last update: 09/05/19
'''

# Dependancies

import discord, asyncio, time
from cogs.objects.player_ import Player_

# Translation

from cogs.utils.functions.translation.gettext_config import Translate

# Config

from cogs.utils.functions.readability.embed import Basic_embed

# Database

from cogs.utils.functions.database.select.player.player_ressources import Select_player_stones, Select_player_zenis

async def Display_profile(client, ctx, player):
    '''
    Displays the passed player profile.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `player` : must be `discord.Member` object.

    Return: void : sends a message in `discord.Embed` form
    '''

    # Init

    if(player.bot):  # If the player is a bot we don't display anything
        return

    _ = await Translate(client, ctx)
    player_ = Player_(client, player)

        # Init player's info

    player_stones = await player_.stones()
    player_zenis = await player_.zenis()
    player_ava = player_.avatar()

    # Set up the embed

    profile = Basic_embed(client, _('{}\'s profile').format(player.name), thumb = player_ava)

        # Fields
    
    profile.add_field(name = _('Dragon stones :'), value = player_stones, inline = True)
    profile.add_field(name = _('Zenis :'), value = player_zenis, inline = True)
    
    # Send

    await ctx.send(embed = profile)
'''
Manages the displaying of the profile.

Last update: 30/06/19
'''

# Dependancies

import discord, asyncio, time

# Object

from cogs.objects.player import Player

# Translation

from cogs.utils.functions.translation.gettext_config import Translate

# Config

from cogs.utils.functions.readability.embed import Basic_embed
from configuration.graphic_config.icons_config import ICON_DS, ICON_STAR, ICON_ZENIS, ICON_LEVEL

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

    player_ = Player(client, player)
    await player_.init()

        # Init player's info
        
    player_register, player_ava = player_.register_date, player_.avatar
    player_stones, player_zenis = player_.stone, player_.zenis

    # Set up the embed

    profile = Basic_embed(client, _('{}\'s profile').format(player.name), thumb = player_ava)

        # Fields
    
    profile.add_field(name = _('{}Level :').format(ICON_LEVEL), value = '{:,}'.format(0), inline = True)
    profile.add_field(name = _('{}Experience :').format(ICON_STAR), value = '{:,}'.format(0), inline = True)
    profile.add_field(name = _('{}Dragon stones :').format(ICON_DS), value = '{:,}'.format(player_stones), inline = True)
    profile.add_field(name = _('{}Zenis :').format(ICON_ZENIS), value = '{:,}'.format(player_zenis), inline = True)
    profile.add_field(name = _('Play since :'), value = player_register, inline = True)
    profile.add_field(name = _('Language :'), value = player_.language, inline = True)
    profile.add_field(name = _('Location :'), value = player_.location, inline = True)
    
    # Send

    await ctx.send(embed = profile)
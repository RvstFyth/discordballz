'''
Manages the displaying of the profile.

Last update: 09/05/19
'''

# Dependancies

import discord, asyncio, time

# Object

from cogs.objects.player import Player

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

    if(player.bot):  # If the player is a bot we don't display anything
        return

    _ = await Translate(client, ctx)
    player_ = Player(client, player)

        # Init player's info
        
    player_register, player_ava = await player_.register_date(), player_.avatar
    player_stones, player_zenis = await player_.stones(), await player_.zenis()
    player_level, player_xp = await player_.level(), await player_.xp()

    # Set up the embed

    profile = Basic_embed(client, _('{}\'s profile').format(player.name), thumb = player_ava)

        # Fields
    
    profile.add_field(name = _('Level :'), value = '{:,}'.format(player_level), inline = True)
    profile.add_field(name = _('Experience :'), value = '{:,}'.format(player_xp), inline = True)
    profile.add_field(name = _('Dragon stones :'), value = '{:,}'.format(player_stones), inline = True)
    profile.add_field(name = _('Zenis :'), value = '{:,}'.format(player_zenis), inline = True)
    profile.add_field(name = _('Play since :'), value = player_register, inline = True)
    profile.add_field(name = _('Language :'), value = await player_.language(), inline = True)
    profile.add_field(name = _('Location :'), value = await player_.location(), inline = True)
    
    # Send

    await ctx.send(embed = profile)
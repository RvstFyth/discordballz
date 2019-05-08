'''
Manages the player's profile.

Last update: 08/05/19
'''

# Dependancies

import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog

# Check

from cogs.utils.functions.check.player.player_checks import Is_registered

# Config
    # Utils

from cogs.utils.functions.readability.embed import Basic_embed

    # Badges

from configuration.graphic_config.badges_config import BADGE_PIONEER

class Profile(Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.check(Is_registered)
    async def profile(self, ctx):
        '''
        Displays the player's profile.
        '''

        # Init

        player = ctx.message.author
        player_ava = player.avatar_url

        player_level = 0
        player_rank = '#1'

        # Set up the embed

        profile_display = Basic_embed(self.client, thumb = player_ava)
        profile_display.add_field(name = 'Level :', value = player_level, inline = True)
        profile_display.add_field(name = 'Ladder :', value = player_rank, inline = True)

        await ctx.send(embed = profile_display)

def setup(client):
    client.add_cog(Profile(client))
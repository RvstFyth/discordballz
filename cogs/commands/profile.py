'''
Manages the player's profile.

Last update: 09/05/19
'''

# Dependancies

import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog

# Check

from cogs.utils.functions.check.player.player_checks import Is_registered

# Database

from cogs.utils.functions.logs.command_logger import Command_log

# Functions

from cogs.utils.functions.commands.profile.profile_display import Display_profile

class Profile(Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.check(Is_registered)
    async def profile(self, ctx, target: discord.Member = None):
        '''
        Displays the player's profile.
        '''

        # Init

        caller = ctx.message.author

        # If the caller didn't mention someone

        if(target == None):
            player = ctx.message.author

            # Log

            await Command_log(self.client, ctx, caller)
        
        else:
            
            # If he mentionned someone, we replace him by the mentionned person

            player = target

            # Log

            await Command_log(self.client, ctx, caller, target = player)
        
        await Display_profile(self.client, ctx, player)

def setup(client):
    client.add_cog(Profile(client))
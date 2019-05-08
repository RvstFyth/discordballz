'''
Manages the start command and its behaviour.

Last update: 08/05/19
'''

# Dependancies

import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog

# Check

from cogs.utils.functions.check.player.player_checks import Is_not_registered

# Database

from cogs.utils.functions.database.insert.player import Insert_in_player

class Start(Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check(Is_not_registered)
    async def start(self, ctx):
        '''
        Register a member into the database.
        '''

        # Init

        player = ctx.message.author
        date = time.strftime('%d/%m/%y', time.gmtime())

        # Insert informations into the database

        await Insert_in_player(self.client, player, date)

def setup(client):
    client.add_cog(Start(client))
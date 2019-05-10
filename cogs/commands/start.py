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

from cogs.utils.functions.logs.command_logger import Command_log
from cogs.utils.functions.database.insert.player import Insert_in_player, Insert_in_player_ressources, Insert_in_player_experience

class Cmd_Start(Cog):
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

        # Logs

        await Command_log(self.client, ctx, 'start', player)

        # Insert informations into the database

        await Insert_in_player(self.client, player, date)
        await Insert_in_player_ressources(self.client, player)
        await Insert_in_player_experience(self.client, player)

def setup(client):
    client.add_cog(Cmd_Start(client))
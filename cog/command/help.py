"""
Manages the Help command

--

Author : DrLarck

Last update : 29/08/19 (DrLarck)
"""

# dependancies
import asyncio
from discord.ext import commands

# utils
from utility.cog.helper.helper import Helper

# check
from utility.command.checker.basic import Basic_checker

# command
class Cmd_help(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.check(Basic_checker().is_game_ready)
    @commands.command()
    async def help(self, ctx):
        """
        Displays the help.
        """

        # init
        helper = Helper(self.client, ctx)

def setup(client):
    client.add_cog(Cmd_help(client))
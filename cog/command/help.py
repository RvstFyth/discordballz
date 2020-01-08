"""
Manages the Help command

--

Author : DrLarck

Last update : 08/01/2020 (DrLarck)
"""

# dependancies
import asyncio
from discord.ext import commands

# utils
from utility.cog.helper.helper import Helper
from utility.cog.player.player import Player

# check
from utility.command.checker.basic import Basic_checker

# command
class Cmd_help(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.check(Basic_checker().is_game_ready)
    @commands.command()
    async def help(self, ctx, command = None):
        """
        Displays the help.

        - Parameter : 

        `command` (str) : The name of the command which the user wants to see the help.
        """

        # init
        player = Player(ctx, self.client, ctx.message.author)
        helper = Helper(self.client, ctx, player)

        if(command == None):
            await helper.helper_manager()
    
        else:
            help_panel = await helper.get_help_command(command)
            
            if not help_panel is None:
                await helper.display_help(help_panel)
            
            else:
                await ctx.send(f"Sorry, the help pannel for the command `{command}` has not been found.")

def setup(client):
    client.add_cog(Cmd_help(client))
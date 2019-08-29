"""
Allows the player to manage his team

--

Author : DrLarck

Last update : 29/08/19 (DrLarck)
"""

# dependancies
import asyncio
from discord.ext import commands

# utils
from utility.cog.player.player import Player

# check
from utility.command.checker.basic import Basic_checker

# command
class Cmd_fighter(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @commands.group()
    async def fighter(self, ctx):
        """
        The fighter command group
        """

        # display the fighter help here

    #################### SET ####################
    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @fighter.group(invoke_without_command = True)
    async def set(self, cxt):
        """
        Allow the player to set a fighter
        """

        # display the set help here

    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @set.command()
    async def a(self, ctx, global_id : int):
        """
        Allow the player to select the fighter a to set

        `global_id` : int - Represents the character to display
        """

        # init
        player = Player(ctx, self.client, ctx.message.author)
        box_data = await player.box.get_data(global_id)

        # ask the player to pick the id of his character
        await ctx.send(f"<@{player.id}> Please select a fighter among the following by typing its index number :")
        # display the available characters
        await player.box.manager(global_id)
        # ask for choice

def setup(client):
    client.add_cog(Cmd_fighter(client))
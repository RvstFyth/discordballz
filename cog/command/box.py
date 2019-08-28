"""
Manages the box command.

-- 

Author : DrLarck

Last update : 28/08/19 (DrLarck)
"""

# dependancies
import asyncio
from discord.ext import commands

# checker
from utility.command.checker.basic import Basic_checker

# util
from utility.cog.player.player import Player
from utility.cog.box.box import Box

# command
class Cmd_box(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.check(Basic_checker().is_game_ready)
    @commands.command()
    async def box(self, ctx):
        """
        Displays the player's box
        """

        # init
        player = Player(self.client, ctx.message.author)
        box = Box(ctx, self.client, player)

        # display the box
        await box.display_box()

def setup(client):
    client.add_cog(Cmd_box(client))
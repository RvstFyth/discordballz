"""
Manages the box command.

-- 

Author : DrLarck

Last update : 29/08/19 (DrLarck)
"""

# dependancies
import asyncio
from discord.ext import commands

# checker
from utility.command.checker.basic import Basic_checker
from utility.command.checker.box import Box_checker

# util
from utility.cog.player.player import Player
from utility.cog.box.box import Box

# command
class Cmd_box(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @commands.check(Box_checker().has_opened_box)
    @commands.command()
    async def box(self, ctx, character_id : int = None):
        """
        Displays the player's box

        - Parameter :

        `character_id` : Represents the character global id to display.
        """

        # init
        player = Player(ctx, self.client, ctx.message.author)

        # box
        await player.box.manager(character_id = character_id)

def setup(client):
    client.add_cog(Cmd_box(client))
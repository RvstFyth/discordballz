"""
Allow the player to cancel an action

--

Author : DrLarck

Last update : 31/01/20 (DrLarck)
"""

# dependancies
import asyncio
from discord.ext import commands

# util
from utility.cog.player.player import Player

# checker
from utility.command.checker.basic import Basic_checker
from utility.command.checker.fight import Fight_checker

# command
class Cmd_cancel(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @commands.group(invoke_without_command = False)
    async def cancel(self, ctx):
        """
        Allow the player to cancel an action
        """

        return
    
    @cancel.command()
    async def fight(self, ctx):
        """
        Allow the player to reset its `in_fight` status
        """

        # init
        player = Player(ctx, self.client, ctx.message.author)
        checker = Fight_checker()

        # check if the player is in a fight
        if player.id in checker.in_fight:
            checker.in_fight.remove(player.id)

            await ctx.send("You are no longer in a fight.")
        
        else:
            await ctx.send("You're not in a fight.")

def setup(client):
    client.add_cog(Cmd_cancel(client))
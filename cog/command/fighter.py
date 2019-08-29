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
from utility.command._fighter import Fighter
from utility.cog.character.getter import Character_getter
from utility.command._fighter import Fighter

# check
from utility.command.checker.basic import Basic_checker

# command
class Cmd_fighter(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.getter = Character_getter()

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
    async def a(self, ctx, character_id):
        """
        Set the fighter slot a
        """

        # init
        player = Player(ctx, self.client, ctx.message.author)
        fighter = Fighter(ctx, self.client, player)

        await fighter.fighter_command("a", character_id)
    
    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @set.command()
    async def b(self, ctx, character_id):
        """
        Set the fighter slot b
        """

        # init
        player = Player(ctx, self.client, ctx.message.author)
        fighter = Fighter(ctx, self.client, player)

        await fighter.fighter_command("b", character_id)
    
    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @set.command()
    async def c(self, ctx, character_id):
        """
        Set the fighter slot c
        """

        # init
        player = Player(ctx, self.client, ctx.message.author)
        fighter = Fighter(ctx, self.client, player)

        await fighter.fighter_command("c", character_id)

def setup(client):
    client.add_cog(Cmd_fighter(client))
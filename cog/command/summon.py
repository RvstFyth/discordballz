"""
Summon command

--

Author : DrLarck

Last update : 22/08/19 (DrLarck)
"""

# dependancies
import asyncio
from discord.ext import commands

# utils
from utility.cog.player.player import Player
from utility.graphic.embed import Custom_embed
    # checker
from utility.command.checker.basic import Basic_checker
    # summon
from utility.command._summon import Summoner
    # displayer
from utility.cog.displayer.character import Character_displayer
from utility.cog.helper.helper import Helper

class Cmd_summon(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.check(Basic_checker().is_game_ready)
    @commands.group(
        aliases = ["sum"],
        invoke_without_command = True
    )
    async def summon(self, ctx):
        """
        Command group :

        - basic {multi} default {single}
        """
        
        # init
        helper = Helper(self.client, ctx)
        summon_help = await helper.summon()

        # send the help
        await helper.display_help(summon_help)

        return
    
    @commands.check(Basic_checker().is_game_ready)
    @summon.command()
    async def basic(self, ctx):
        """
        Summon a character from the basic banner.
        """

        # init
        player = Player(ctx.message.author)
        summoner = Summoner(self.client)
        displayer = Character_displayer(self.client, ctx, player)

        # draw 
        drawn_character = await summoner.summon(player)
        await drawn_character.init()

        # display
        displayer.character = drawn_character
        await displayer.display(summon_format = True)
        
        return

def setup(client):
    client.add_cog(Cmd_summon(client))
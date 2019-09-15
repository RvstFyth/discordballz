"""
Manages the show command.

--

Author : DrLarck

Last update : 15/09/19 (DrLarck)
"""

# dependancies
import asyncio
from discord.ext import commands

# checker
from utility.command.checker.basic import Basic_checker

# util
from utility.cog.player.player import Player
from utility.cog.character.getter import Character_getter

from utility.cog.displayer.character import Character_displayer

# command
class Cmd_show(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.check(Basic_checker().is_game_ready)
    @commands.command()
    async def show(self, ctx, character_id, level = None):
        """
        Allow the player to see a character's stats and abilities by passing its global id.

        If a unique id is passed, displays the unique character.
        """

        # init
        player = Player(ctx, self.client, ctx.message.author)
        character_getter = Character_getter()
        displayer = Character_displayer(self.client, ctx, player)

        if(level != None):
            if(level.isdigit()):
                level = int(level)

                if(level > 150):
                    level = 150
            
            else:
                level = None

        # global id
        if(character_id.isdigit()):
            character_id = int(character_id)
            character = await character_getter.get_character(character_id)

            if(character != None):
                displayer.character = character

                await displayer.display(
                    basic_format = True,
                    level = level
                )
            
            else:
                await ctx.send(f"<@{player.id}> Character `#{character_id}` not found.")
        
        # unique id
        else:
            character = await character_getter.get_from_unique(self.client, character_id)

            if(character != None):
                displayer.character = character

                await displayer.display(
                    basic_format = True,
                    level = level
                )

            else:
                await ctx.send(f"<@{player.id}> Character `#{character_id}` not found.")

def setup(client):
    client.add_cog(Cmd_show(client))
"""
Manages the start command

--

Author : DrLarck

Last update : 04/01/19 (DrLarck)
"""

# dependancies
import asyncio
from discord.ext import commands

# util
from utility.database.database_manager import Database
from utility.cog.player.player import Player

# checker
from utility.command.checker.basic import Basic_checker
from utility.command.checker.start import Start_checker

# icon
from configuration.icon import game_icon

# start command
class Cmd_start(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Start_checker().need_register)
    @commands.command()
    async def start(self, ctx):
        """
        Allow the player to start an adventure.
        """

        # init
        db = Database(self.client.db)
        player = Player(ctx, self.client, ctx.message.author)
        
        # insert the player into the tables
        await db.execute(
            f"""
            INSERT INTO player_info(player_id, player_name) VALUES({player.id}, '{player.name}');
            INSERT INTO player_resource(player_id, player_name, player_dragonstone) VALUES({player.id}, '{player.name}', 25);
            INSERT INTO player_combat_info(player_id, player_name) VALUES({player.id}, '{player.name}');
            """
        )

        # welcome message
        welcome = f"<@{player.id}> Hello and welcome to **Discord Ball Z III** - *Open Beta* !\nWe're hoping you to enjoy your adventure !\n\nHere are **25** {game_icon['dragonstone']}, they will help you to **summon** your first heroes that will fight for you !\n\nIf you have any question, do not hesitate to consult the `d!help` command or join the **Official Server** : https://discord.gg/eZf2p7h"
        
        await ctx.send(welcome)
        
def setup(client):
    client.add_cog(Cmd_start(client))
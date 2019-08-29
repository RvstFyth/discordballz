"""
Manages the start command

--

Author : DrLarck

Last update : 28/08/19 (DrLarck)
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
        player = Player(self.client, ctx.message.author)
        
        # insert the player into the tables
        await db.execute(
            f"""
            INSERT INTO player_info(player_id, player_name) VALUES({player.id}, '{player.name}');
            INSERT INTO player_resource(player_id, player_name) VALUES({player.id}, '{player.name}');
            INSERT INTO player_combat_info(player_id, player_name) VALUES({player.id}, '{player.name}');
            """
        )
    
def setup(client):
    client.add_cog(Cmd_start(client))
"""
Manages the start command

--

Author : DrLarck

Last update : 12/01/2020 (DrLarck)
"""

# dependancies
import asyncio
import time
import random
from discord.ext import commands

# util
from utility.database.database_manager import Database
from utility.cog.player.player import Player
from utility.command._summon import Summoner

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
        summoner = Summoner(self.client)

        # insert the player into the tables
        await db.execute(
            """INSERT INTO player_info(player_id, player_name, player_register_date) VALUES ($1, $2, $3)""",
            (player.id, player.name, time.strftime("%d/%m/%y", time.gmtime())))
        await db.execute(
            """INSERT INTO player_resource(player_id, player_name, player_dragonstone) VALUES ($1, $2, 25)""",
            (player.id, player.name,))
        await db.execute("""INSERT INTO player_combat_info(player_id, player_name) VALUES ($1, $2)""",
                         (player.id, player.name,))

        # generate 3 saibaiman
        for i in range(3):
            await db.execute("""
                            INSERT INTO character_unique(character_owner_id, character_owner_name, character_global_id, 
                            character_type, character_rarity)
                            VALUES($1, $2, $3, $4, 0)""",
                             [player.id, player.name, (i + 1), random.randint(0, 4)]
                             )

        await summoner.set_unique_id()

        # get the summoned characters
        summoned = await db.fetch(
            f"""
            SELECT character_unique_id FROM character_unique WHERE character_owner_id = {player.id};
            """
        )

        # assign summoned character
        slot = ["a", "b", "c"]

        for a in range(3):
            await asyncio.sleep(0)

            await db.execute(
                f"""
                UPDATE player_combat_info 
                SET player_fighter_{slot[a]} = '{summoned[a][0]}'
                WHERE player_id = {player.id};
                """
            )

        # welcome message
        welcome = f"<@{player.id}> Hello and welcome to **Discord Ball Z III** - *Open Beta* !\nWe're hoping you to enjoy your adventure !\n\nHere are **25**{game_icon['dragonstone']}, they will help you to **summon** your first heroes that will fight for you !\n\nIf you have any question, do not hesitate to consult the `d!help` command or join the **Official Server** : https://discord.gg/eZf2p7h"

        await ctx.send(welcome)

def setup(client):
    client.add_cog(Cmd_start(client))
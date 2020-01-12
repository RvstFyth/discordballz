"""
Main file of the program. Run the bot.

--

Project started : 06/05/19 - 8:20 PM France

Author : DrLarck

Last update : 12/01/2020 (DrLarck)
"""

# dependancies
import asyncio, logging, discord
from discord.ext import commands

# utils
    # cogs
from utility.cog.cog_loader import Cog_loader
from utility.cog.task.background_manager import Background_manager
    # database
from utility.database.database_manager import Database
from utility.database.operation.database_table import Table_creator
# config
from configuration.bot import Bot_config

# presence
presence_activity = discord.Game(f"d!help | v{Bot_config.version} - {Bot_config.phase}")

# init client
client = commands.AutoShardedBot(command_prefix = Bot_config.prefix, help_command = None, activity = presence_activity)
cog = Cog_loader(client)

# logs
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# _init
# create the database connection pool
database = Database(None)  # pass None as we do not have set up a connection pool yet
client.db = client.loop.run_until_complete(database.init())
background = Background_manager(client)

# loading the cogs
if __name__ == "__main__":
    cog.load_cog()

# run the bot
client.run(Bot_config.token)
"""
Main file of the program. Run the bot.

--

Project started : 06/05/19 - 8:20 PM France

Author : DrLarck

Last update : 20/08/19 (DrLarck)
"""

# dependancies
import asyncio, logging, discord

from discord.ext import commands

# utils
    # cogs
from utility.cog.cog_loader import Cog_loader

    # database
from utility.database.database_manager import Database

# config
from configuration.bot import Bot_config

# init
client = commands.AutoShardedBot(command_prefix = Bot_config.prefix, help_command = None)

cog = Cog_loader(client)

# logs
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# create the database connection pool
database = Database(None)  # pass None as we do not have set up a connection pool yet
client.db = client.loop.run_until_complete(database.init())

# loading the cogs
if __name__ == "__main__":
    cog.load_cog()

# run the bot
client.run(Bot_config.token)
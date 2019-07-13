"""
Main file of the program. Run the bot.

--

Project started : 06/05/19 - 8:20 PM France

Author : DrLarck

Last update : 11/07/19 (DrLarck)
"""

# dependancies
import asyncio, logging

from discord.ext import commands

# utils
    # cogs
from utility.cog.cog_loader import Cog_loader

    # database
from utility.database.database_manager import Database

# config
from configuration.bot import bot_config

# init
logging.basicConfig(level = logging.INFO)

client = commands.AutoShardedBot(command_prefix = bot_config["prefix"], help_command = None)

cog = Cog_loader(client)

# create the database connection pool
database = Database(None)  # pass None as we do not have set up a connection pool yet
client.db = client.loop.run_until_complete(database.init())

# loading the cogs
if __name__ == "__main__":
    cog.load_cog()

# run the bot
client.run(bot_config["token"])
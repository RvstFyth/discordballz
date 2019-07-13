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
from utility.cog.cog_loader import Cog_loader

# config
from configuration.bot import bot_config

# init
logging.basicConfig(level = logging.INFO)

client = commands.AutoShardedBot(command_prefix = bot_config["prefix"], help_command = None)

cog = Cog_loader(client)

# loading the cogs
if __name__ == "__main__":
    cog.load_cog()

# run the bot
client.run(bot_config["token"])
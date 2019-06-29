'''
Main file of the project.

Created : 06/05/19 - 8:20 PM (GMT+1) France

Last update: 29/06/19
'''

# Dependancies

import discord, asyncio, logging, time
from discord.ext import commands

# Config

from configuration.main_config.basic_config import BOT_TOKEN, PREFIX, COGS

# Functions

from cogs.utils.tasks._task_runner import Task_runner

from cogs.utils.functions.database.init.database_connection import Connection_to_database

# Init
logging.basicConfig(level = logging.INFO)
client = commands.AutoShardedBot(command_prefix = PREFIX, help_command = None)

# Tasks
    # connect to database
client.loop.run_until_complete(Connection_to_database(client))  # init the connection to the database

# run tasks
runner = Task_runner(client)
instances = runner.run_tasks()

# Loading cogs

if __name__ == '__main__':
    for cog in COGS:
        try:
            client.load_extension(cog)

        except Exception as error:
            error_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
            print('{} - Error in main : loading cogs : {}'.format(error_time, error))
            pass

# Run the tasks

Task_runner(client)

# Run the bot

client.run(BOT_TOKEN)
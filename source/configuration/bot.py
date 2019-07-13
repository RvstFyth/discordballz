"""
Here is the basic configuration of the bot.

--

Author : DrLarck

Last update : 13/07/19
"""

# dependancies
from os import environ

# config
bot_config = {
    "token" : environ["BOT_TOKEN3"],
    "prefix" : [
        "Db", "db", "D!", "d!"
    ],
    "version" : "3.0.1.0",
    "phase" : "BETA"
}
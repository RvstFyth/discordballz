"""
Here is the basic configuration of the bot.

--

Author : DrLarck

Last update : 20/08/19 (DrLarck)
"""

# dependancies
from os import environ

# config
class Bot_config:
    """
    Manages the bot configuration.

    - Attribute :

    `token` : The bot token.

    `prefix` : The bot prefixes.

    `is_ready` : Default false, tells if the bot is ready to use or not.

    `version` : The bot version

    `phase` : The bot release phase.
    """

    # basic
    token = environ["BOT_TOKEN3"]

    # usage 
    prefix = [
        "Db", "db",
        "D!", "d!"
    ]
    
    is_ready = False

    # info
    version = "3.0.1.0"
    phase = "BETA"
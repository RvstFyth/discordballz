"""
Here is the basic configuration of the bot.

--

Author : DrLarck

Last update : 08/01/2020 (DrLarck)
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

    `droprate` : dict - The droprates of the characters

    - Key :

    n
    r
    sr
    ssr
    ur
    lr
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
    version = "3.0.1.149"
    phase = "BETA"

    # droprate
    droprate = {
        "n" : 100,
        "r" : 60,
        "sr" : 30,
        "ssr" : 10,
        "ur" : 1,
        "lr" : 0.1
    }

    # level per rarity
    rarity_level = {
        "n" : 20,
        "r" : 40,
        "sr" : 60,
        "ssr" : 80,
        "ur" : 120,
        "lr" : 150
    }
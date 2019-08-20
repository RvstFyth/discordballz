"""
Managing the basic checks.

--

Author : DrLarck

Last update : 20/08/19 (DrLarck)
"""

# dependancies
import asyncio

# config
from configuration.bot import Bot_config

# basic checker
class Basic_checker:
    """
    Manages the basic checks.
    """

    # method
    async def is_game_ready(self, ctx):
        """
        `coroutine`

        Tells if the game is ready to use or not.

        --

        Return : bool
        """

        # init
        game_status = Bot_config.is_ready

        return(game_status)
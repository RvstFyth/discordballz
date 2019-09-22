"""
Managing the basic checks.

--

Author : DrLarck

Last update : 22/09/19 (DrLarck)
"""

# dependancies
import asyncio

# config
from configuration.bot import Bot_config

# util
from utility.database.database_manager import Database

# basic checker
class Basic_checker:
    """
    Manages the basic checks.
    """

    database = Database(None)

    # method
    async def is_registered(self, ctx):
        """
        `coroutine`

        Check if the caller is already registered in the databse or not.

        --

        Return : bool
        """

        # init
        handler = ctx.bot.db
        db = Database(handler)

        # get the player
        player = await db.fetchval(
            f"""
            SELECT player_id FROM player_info
            WHERE player_id = {ctx.message.author.id};
            """
        )

        # check if registered
        if(player == None):
            await ctx.send(f"<@{ctx.message.author.id}> ❌ You must be **registered** to perform this action.\nUse `d!start` to do so.")
            return(False)
        
        else:
            return(True)

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
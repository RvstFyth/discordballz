"""
Manages the start command checker

--

Author : DrLarck

Last update : 28/08/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.database.database_manager import Database

# checker 
class Start_checker:
    """
    Manages the start checks.
    """

    async def need_register(self, ctx):
        """
        `coroutine`

        Check if the player is already registered or not.

        --

        Return : bool
        """

        # init
        handler = ctx.bot.db
        db = Database(handler)

        # check if the player is found
        player = await db.fetchval(
            f"""
            SELECT player_id FROM player_info
            WHERE player_id = {ctx.message.author.id};
            """
        )

        # check if registered
        if(player == None):
            return(True)
        
        else:
            await ctx.send(f"<@{ctx.message.author.id}> You are already registered.")
            return(False)
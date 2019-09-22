"""
Box checker

--

Author : DrLarck

Last update : 28/08/19 (DrLarck)
"""

# dependancies
import asyncio

# box checker
class Box_checker:
    """
    Manages the box checks.

    - Attribute :

    `opened_box` : list - Stores the id of the player who have their box currently opened.

    - Method :

    :coro:`has_opened_box(player_id)` : Check if a player has his box opened or not. Return bool.
    """
    
    # attribute
    opened_box = []
    
    # method
    async def has_opened_box(self, ctx):
        """
        `coroutine`

        Check if the player has opened a box or not.

        - Parameter :

        `ctx` : int - Represents the `commands.Context`

        --

        Return : bool
        """

        # init
        player_id = ctx.message.author.id 

        if player_id in self.opened_box:
            await ctx.send(f"<@{player_id}> ❌ Please close your previous box page to open a new one.")
            return(False)
        
        else:
            return(True)
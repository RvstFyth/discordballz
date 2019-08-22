"""
Manages the colors.

--

Author : DrLarck

Last update : 22/08/19 (DrLarck)
"""

# dependancies
import asyncio

# config
from configuration.color import game_color

# color manager
class Color_displayer:
    """
    Manages the colors

    - Method :
    """

    # method
    async def get_rarity_color(self, rarity_id):
        """
        `coroutine`

        Get and return the rarity color.

        --

        Return : color code
        """

        # init
        color = 0xffffff

        # get the color
        if(rarity_id == 0):
            color = game_color["n"]
        
        elif(rarity_id == 1):
            color = game_color["r"]
        
        elif(rarity_id == 1):
            color = game_color["sr"]
        
        elif(rarity_id == 1):
            color = game_color["ssr"]
        
        elif(rarity_id == 1):
            color = game_color["ur"]
        
        elif(rarity_id == 1):
            color = game_color["lr"]

        return(color)
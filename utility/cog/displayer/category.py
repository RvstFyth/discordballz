"""
Manages the category display such as expansion, saga, etc.

--

Author : DrLarck

Last update : 22/08/19 (DrLarck)
"""

# dependancies
import asyncio

# config
from configuration.icon import game_icon

# category displayer
class Category_displayer:
    """
    Displays the categories according to the value returned by the character.
    """

    # method
    async def get_expansion(self, expansion_id):
        """
        `coroutine`

        Get the expansion name and icon.

        --
        
        Return : expansion name, expansion icon
        """

        # init
        name = ""
        icon = ""
        
        # get the expansion
        if(expansion_id == 0):
            name = "Basic"
            icon = game_icon["expansion"]["basic"]
            
        return(name, icon)
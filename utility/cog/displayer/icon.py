"""
Manages the displaying of the icons such as the type, rarity, expansion, etc.

--

Author : DrLarck

Last update : 22/08/19 (DrLarck)
"""

# dependancies
import asyncio

# config
from configuration.icon import game_icon

# icon manager
class Icon_displayer:
    """
    Manages the displaying of most of the game icons.

    - Parameter :

    - Attribute :

    - Method :

    :coro:`get_rarity_icon(rarity : int)` : Convert the rarity into the discord.Emoji icon

    :coro:`get_type_icon(type : int)` : Convert the type icon the discord.Emoji icon
    """

    # method
    async def get_rarity_icon(self, rarity : int):
        """
        `couroutine`

        Convert the icon id into the discord.Emoji

        --

        Return : discord.Emoji
        """

        # init
        rarity_icon = ""

        # Normal
        if(rarity == 0):
            rarity_icon = game_icon["n"]

            return(rarity_icon)
        
        # Rare
        if(rarity == 1):
            rarity_icon = game_icon["r"]

            return(rarity_icon)
        
        # Super rare
        if(rarity == 2):
            rarity_icon = game_icon["sr"]

            return(rarity_icon)
        
        # Super super rare
        if(rarity == 3):
            rarity_icon = game_icon["ssr"]

            return(rarity_icon)
        
        # Ultra rare
        if(rarity == 4):
            rarity_icon = game_icon["ur"]

            return(rarity_icon)
        
        # Legendary
        if(rarity == 5):
            rarity_icon = game_icon["lr"]

            return(rarity_icon)
        
        # if not found return none
        return(None)
    
    async def get_type_icon(self, _type):
        """
        `coroutine`

        Convert the type into the discord.Emoji icon

        --

        Return : discord.Emoji
        """

        # init

        type_icon = ""

        # Agl
        if(_type == 0):
            type_icon = game_icon["agl"]

            return(type_icon)
        
        # Teq
        if(_type == 1):
            type_icon = game_icon["teq"]

            return(type_icon)
        
        # Str
        if(_type == 2):
            type_icon = game_icon["str"]

            return(type_icon)
        
        # Phy
        if(_type == 3):
            type_icon = game_icon["phy"]

            return(type_icon)
        
        # Int
        if(_type == 4):
            type_icon = game_icon["int"]

            return(type_icon)
        
        # if not found return none
        return(None)
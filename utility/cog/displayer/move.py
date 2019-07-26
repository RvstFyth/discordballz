"""
Manages the way the move are displayed.

--

Author : DrLarck

Last update : 25/07/19 (DrLarck)
"""

# dependancies
import asyncio

# icon
from configuration.icon import game_icon

# utils
from utility.graphic.embed import Custom_embed

# move displayer
class Move_displayer:
    """
    Manages the way the moves are displayed

    - Parameter :

    - Attribute :

    - Method :
    """

    # attribute
    def __init__(self):
        self.a = 0
    
    # method
    async def offensive_move(self, move):
        """
        `coroutine`

        Displays an offensive move.

        - Parameter :

        `move` : Represents a dict of the move that contains :
        - "name" : The move name (str)
        - "icon" : The move icon (emoji)
        - "damage" : The move damage (int)
        - "critical" : Is critical (bool)
        - "dodge" : Is dodged (bool)
        - "physical" : Are the damage physical damage (bool)
        - "ki" : Are the damage ki damage (bool)

        --

        Return : str (format the string for offensive display)
        """
        
        # init
        offensive_display = ""

        offensive_display += f"__Move__ : `{move['name']}`{move['icon']}\n"

        # type of damage
        if(move["dodge"]):
            offensive_display += f"__Damage__ : **DODGED ! 💨**\n"
        
        elif(move["physical"]):
            offensive_display += f"__Damage__ : -**{move['damage']:,}** :punch: "
        
        elif(move["ki"]):
            offensive_display += f"__Damage__ : -**{move['damage']:,}** {game_icon['ki_ability']} "
        
        # check if crit
        if(move["dodge"] == False):
            # a dodge cannot be crit
            if(move["critical"]):
                offensive_display += "**(CRITICAL ! :boom:)**\n"
            
            else:
                offensive_display += "\n"

        return(offensive_display)
    
    async def ki_move(self, move):
        """
        `coroutine`

        Manages the displaying of a ki move.
        
        damage key represents the ki gain.

        - Parameter : 

        `move` : Represents the move infos as a `dict` 
        - "name" : The move name (str)
        - "icon" : The move icon (emoji)
        - "damage" : The ki gained (int)
        - "critical" : Is critical (bool)
        - "dodge" : Is dodged (bool)
        - "physical" : Are the damage physical damage (bool)
        - "ki" : Are the damage ki damage (bool)

        -- 

        Return : str formatted to display the ki move
        """

        # init
        ki_display = ""

        ki_display += f"__Move__ : `{move['name']}`{move['icon']}\n"
        ki_display += f"__Ki gain__ : +**{move['damage']}** :fire: \n"
        
        return(ki_display)
    
    async def defense_move(self):
        """
        `coroutine`

        Manages the displaying of the defending move.

        --

        Return : str formatted to display defending move
        """

        # init
        defend_display = ""

        defend_display += f"__Move__ : Defending :shield:"

        return(defend_display)
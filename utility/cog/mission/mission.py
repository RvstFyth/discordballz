"""
Mission object

--

Author : DrLarck

Last update : 02/02/20 (DrLarck)
"""

# dependancies
import asyncio

# mission
class Mission():
    """
    Represent a mission

    - Attribute :

    `reward` (`dict`) : [dragonstone, zenis, player_xp, team_xp] Represents the reward the player can gain at the end of the mission

    `opponent` (`list`) : List of `Character()` in the opponent team

    - Method 

    :coro:`init()` : `None` - Init the mission

    :coro:`set_opponent()` : `list` - Set the opponent team
    """

    # attribute
    def __init__(self):
        self.reward = {
            "dragonstone" : 0,
            "zenis" : 0,
            "player_xp" : 0,
            "team_xp" : 0
        }

        self.opponent = []
    
    # method
    async def init(self):
        """
        `coroutine`

        Init the mission

        -- 

        Return : `None`
        """

        await self.set_opponent()

        return
    
    async def set_opponent(self):
        """
        `coroutine`

        Set the opponent team

        --

        Return : `list`
        """

        return(self.opponent)
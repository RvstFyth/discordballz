"""
Manages the utils for the train command.

--

Authod : DrLarck

Last update : 19/08/19 (DrLarck)
"""

# dependancies
import asyncio

# train utils
class Train:
    """
    Manages the utils for the train command.

    - Parameter :

    `caller_team` : Represents the caller team.
    """

    # attribute
    def __init__(self, caller_team):
        self.caller_team = caller_team
    
    # method
    async def generate_opponent_team(self):
        """
        `coroutine`

        Generates a "balanced" team to oppose the caller's team.

        --

        Return : list of characters representing the generated team.
        """
    pass
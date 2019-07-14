"""
The :class:`Fight()` manages a fight, from the beginning to the end and returns the winner.

--

Author : DrLarck

Last update : 13/07/19
"""

# dependancies
import asyncio

# utility
from source.utility.cog.fight_system.phase_trigger import Trigger_phase
from source.utility.cog.fight_system.phase_selection import Selection_phase
from source.utility.cog.fight_system.phase_battle import Battle_phase

# fight manager
class Fight:
    """
    Manages a fight and returns the winner.

    - Parameter :

    - Attribute : 

    - Method :
    """

    # attribute
    def __init__(self):
        # phase
        self.trigger_phase = Trigger_phase()
        self.selection_phase = Selection_phase()
        self.battle_phae = Battle_phase()
    
    # method
    async def run_fight(self):
        """
        `coroutine`
        
        This method run the fight and manages the when the phases are called.
        --

        Return : Winner index (0 or 1, 2 in case of a draw)
        """


        return
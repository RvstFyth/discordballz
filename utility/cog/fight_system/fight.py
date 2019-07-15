"""
The :class:`Fight()` manages a fight, from the beginning to the end and returns the winner.

--

Author : DrLarck

Last update : 14/07/19
"""

# dependancies
import asyncio

# utility
from utility.cog.fight_system.phase_trigger import Trigger_phase
from utility.cog.fight_system.phase_selection import Selection_phase
from utility.cog.fight_system.phase_battle import Battle_phase

# translation
from utility.translation.translator import Translator

# fight manager
class Fight:
    """
    Manages a fight and returns the winner.

    - Parameter :

    - Attribute : 

    - Method :
    """

    # attribute
    def __init__(self, client, caller):
        self.client = client
        self.player = caller

        # phase
        self.trigger_phase = Trigger_phase()
        self.selection_phase = Selection_phase()
        self.battle_phae = Battle_phase()
    
    # method
    async def run_fight(self, team):
        """
        `coroutine`
        
        This method run the fight and manages the when the phases are called.

        - Parameter : 

        `team` : Represents a list of `team`s. The teams are `list` of :class:`Character()`.

        --

        Return : Winner index (0 or 1, 2 in case of a draw)
        """

        # init
        translation = Translator(self.client.db, self.player)

        team_a_average_hp = 0
        team_b_average_hp = 0

        # determines the number of characters in each team
        team_a_length = len(team[0])
        team_b_length = len(team[1])

        # get the average team hps
            # for team_a
        for character_a in team[0]:
            await asyncio.sleep(0)

            team_a_average_hp += character_a.current_health

            # for team_b
        for character_b in team[1]:
            await asyncio.sleep(0)

            team_b_average_hp += character_b.current_health
        
        # get the average amount of hps
        team_a_average_hp = int(team_a_average_hp / team_a_length)
        team_b_average_hp = int(team_b_average_hp / team_b_length)

        # main loop
        turn = 1  # begins at 1

        while(team_a_average_hp > 0 and team_b_average_hp > 0):  # if one of the teams is defeated, stops the loop
            await asyncio.sleep(0)

        return
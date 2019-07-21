"""
Manages the displaying of teams.

--

Author : DrLarck

Last update : 20/07/19
"""

# dependancies 
import asyncio

# team displayer
class Team_displayer:
    """
    Manages the displaying of teams.

    - Parameter :

    - Attribute :

    - Method :
    """

    # attribute
    def __init__(self, team_a, team_b):
        self.team_a = team_a
        self.team_b = team_b
    
    # method
    async def get_targetable(self, move, ability = None):
        """
        `coroutine` 

        Return list of targetable units based on the player move.

        - Parameter :

        `move` : Represents the move :
        - "sequence"
        - "ability"

        `ability` : Default `None`, represent the used ability.

        --

        Return : list[team_a], list[team_b] of targetable units.
        """

        # init
        team_a = []
        team_b = []

        if(move.lower() == "sequence"):
            for char_b in self.team_b:
                await asyncio.sleep(0)

                # check if the character is alive
                if(char_b.health.current > 0):  
                    team_b.append(char_b)
            
            # now filter with the defender
            defender = []

            for _char_b in team_b:
                await asyncio.sleep(0)

                if(_char_b.posture.defending == True):
                    defender.append(_char_b)
            
            # now replace the list by the targetable units
            if(len(defender) > 0):
                team_b = defender
        
        else:  # not sequence
            if(ability.can_target_ally):
                for ally in self.team_a:
                    await asyncio.sleep(0)

                    # check if alive
                    if(ally.health.current > 0):
                        team_a.append(ally)
            
            if(ability.can_target_enemy):
                for enemy in self.team_b:
                    await asyncio.sleep(0)

                    # check if alive
                    if(enemy.health.current > 0):
                        team_b.append(enemy)

                # now filter with defender
                defender = []

                for _enemy in team_b:
                    await asyncio.sleep(0)

                    if(_enemy.posture.defending == True):
                        defender.append(_enemy)
                
                # replace the team by the defender
                if(len(defender) > 0):
                    team_b = defender

        return(team_a, team_b)
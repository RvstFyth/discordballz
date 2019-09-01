"""
Manages the displaying of teams.

--

Author : DrLarck

Last update : 19/08/19 (DrLarck)
"""

# dependancies 
import asyncio
from utility.cog.displayer.character import Character_displayer

# team displayer
class Team_displayer:
    """
    Manages the displaying of teams.

    - Parameter :

    `client` : Represents a `discord.Client`

    `ctx` : Represents the `commands.Context`

    `player` : Represents the player that is calling it

    `team_a, b` : Represents a list of `Character()`, allies then enemies.

    - Method :

    :coro:`display_teams()` : Displays both teams infos.

    :coro:`get_targetable(move, ability) : Returns a list of all targetable units. (Team a, then team_b)

    `move` : Name of the move

    `ability` : The ability that is used
    """

    # attribute
    def __init__(self, client, ctx, player, team_a, team_b):
        # basic
        self.client = client
        self.ctx = ctx
        self.player = player
        self.team_a = team_a
        self.team_b = team_b
    
    # method
    async def display_teams(self):
        """
        `coroutine`

        Display both teams.

        --

        Return : None, send messages.
        """

        # init
        displayer = Character_displayer(self.client, self.ctx, self.player)
        index = 1
        
        # display character one by one
        # team a
        await self.ctx.send(f"```🔵 - {self.player.name}'s team```")
        for character_a in self.team_a:
            await asyncio.sleep(0)
            
            if(character_a != None):
                if not character_a.is_minion:  # filter npc characters
                    displayer.character = character_a

                    await displayer.display(
                        team_format = True,
                        index = index
                    )
                    
                    index += 1

                else:
                    pass

        await asyncio.sleep(2)
        
        # team b
        await self.ctx.send(f"```🔴 - Enemy team```")
        for character_b in self.team_b:
            await asyncio.sleep(0)
            
            if(character_b != None):
                if not character_b.is_minion:  # filter npc characters
                    displayer.character = character_b

                    await displayer.display(
                        team_format = True,
                        index = index
                    )

                    index += 1

                else:
                    pass
        
        await asyncio.sleep(2)

        return

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
            if(ability.target_ally):
                for ally in self.team_a:
                    await asyncio.sleep(0)

                    # check if alive
                    if(ally.health.current > 0):
                        team_a.append(ally)
            
            if(ability.target_enemy):
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
"""
Manages the utils for the train command.

--

Authod : DrLarck

Last update : 01/09/19 (DrLarck)
"""

# dependancies
import asyncio
from random import choice, randint

# util
from utility.cog.character.getter import Character_getter

# train utils
class Train:
    """
    Manages the utils for the train command.

    - Parameter :

    `client` : Represents a `discord.Client`. Must handle a connection pool to the database.

    - Method :

    :coro:`is_in_team(team, character)` : Checks if a character is in the passed team of characters.

    :coro:`generate_opponent_team(player)` : Generates an opponent team based on the player's team infos
    """

    # attribute
    def __init__(self, client):
        self.client = client
        self.getter = Character_getter()
        self.possible_opponent = [
            1, 2, 3, 4, 5, 6
        ]

    
    # method
    async def is_in_team(self, team, character):
        """
        `coroutine`

        Checks if the passed character is in the team.

        --

        Return : bool
        """

        # init
        is_in = True 
        team_id = []

        # init team_id
        for char in team:
            await asyncio.sleep(0)

            team_id.append(char.info.id)
        
        # now check if the character is in the team
        if character.info.id in team_id:
            is_in = True
        
        else:
            is_in = False

        return(is_in)

    async def generate_opponent_team(self, player):
        """
        `coroutine`

        Generates a "balanced" team to oppose the caller's team.

        - Parameter :

        `player` : Represents a `Player`.
        --

        Return : list of characters representing the generated team. Or None if error (not enough character in player team)
        """

        # init
        opponent_team = []
        player_average = await player.team.get_info()  
        opponent = None

        # check if the team is able to fight
        if(player_average["level"] > 0):
            # add a character to init according to the player's team rarity
            opponent_team.append(await self.getter.get_character(choice(self.possible_opponent)))

            if(player_average["level"] >= 21):  # add another character
                # while the character is in the team, choice a random one
                in_team = True
                cap, count = 10, 0
                while in_team:
                    await asyncio.sleep(0)

                    opponent = await self.getter.get_character(choice(self.possible_opponent))
                    in_team = await self.is_in_team(opponent_team, opponent)

                    # if we reach the max try
                    # break
                    if(count >= cap):
                        break
                    
                    # end loop
                    count += 1

                # if an opponent has been chosen
                if(opponent != None):
                    opponent_team.append(opponent)
                
                else:  # pick a random one
                    opponent_team.append(await self.getter.get_character(choice(self.possible_opponent)))
            
            if(player_average["level"] >= 80):  # add a last one
                # while the character is in the team, choice a random one
                in_team = True
                cap, count = 10, 0
                while in_team:
                    await asyncio.sleep(0)

                    opponent = await self.getter.get_character(choice(self.possible_opponent))
                    in_team = await self.is_in_team(opponent_team, opponent)

                    # if we reach the max try
                    # break
                    if(count >= cap):
                        break
                    
                    # end loop
                    count += 1

                # if an opponent has been chosen
                if(opponent != None):
                    opponent_team.append(opponent)
                
                else:  # pick a random one
                    opponent_team.append(await self.getter.get_character(choice(self.possible_opponent)))
        
        else:
            return

        # all good
        # setup the team
        for character in opponent_team:
            await asyncio.sleep(0)

            character.level = int(randint((0.9 * player_average["level"]), (1.1 * player_average["level"])))  # pick a random level between 90 % of the player's team
            character.rarity.value = player_average["rarity"]                                                 # average level and 110 %
        
        return(opponent_team)
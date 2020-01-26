"""
Manages the player_choice for the fight.

--

Author : DrLarck

Last update : 16/08/19 (DrLarck)
"""

# dependance
import asyncio

# class wait for player choice
class Player_choice:
    """
    Manages the player_choice for the fight.

    - Parameter :

    `client` : Represents a `discord.Client`

    `player` : Represents the player to look for

    - Method :

    :coro:`wait_for_choice(possible_choice, team)` : Waits for the player's choice

    :coro:`wait_for_target(possible_target)` : Waits for the player to choose a target
    """

    # attribute
    def __init__(self, client, player, cast_to_lowercase=False):
        self.client = client
        self.player = player
        self.timeout = 120
        self.cast_to_lowercase = cast_to_lowercase

    # method
    async def wait_for_choice(self, possible_choice, team):
        """
        `coroutine`

        Wait for the player choice. If the player choice is contained in `possible_choice` return the choice made.

        - Parameter : 

        `possible_choice` : Represents all the possible choice. `list` of `str` choices.

        `team` : Represents a list of character present in the combat.

        --

        Return : `str`: Choice
        """

        # init
            # predicate
        def input_check(message):
            """
            Check if the `message.content` is in `possible_choice`.

            - Parameter :

            `message` : Represents the `player` input as `discord.Message`.

            Return : Bool
            """

            # init
            content = message.content
            if self.cast_to_lowercase:
                content = content.lower()

            content = content.split()
            choice = None

            if(message.author.id == self.player.id):
                if content[0] in possible_choice:
                    if(content[0].isdigit()):
                        return(True)
                    
                    else:  # if the choice is a string
                        choice = content[0]

                        if(choice.lower() == "flee"):
                            return(True)

                        if(len(content) > 1):

                            if(choice.lower() == "check"):
                                if(content[1].isdigit()):
                                    to_spec = int(content[1])

                                    if(to_spec > 0 and to_spec-1 <= len(team)-1):
                                        return(True)
                                    
                                    else:  # if the character to spec is not found
                                        return(False)
                                
                                else:  # character to inspect is not specified
                                    return(False)
                            
                            else:  # len > 1 but not check
                                return(False)
                        
                        else:  # if the message.content doesn't contain more than 1 elem
                            return(False)
                
                else:  # if the choice isn't in the possible choice list
                    return(False)
            
            else:  # if the author is not correct
                return(False)

        # get the player choice
        try:
            choice = await self.client.wait_for(
                "message",
                timeout = self.timeout,
                check = input_check
            )
        
        except asyncio.TimeoutError:
            return("flee")
        
        except Exception as error:
            print(f"(PLAYER CHOICE : WAIT FOR) Error : {error}.")
            return("flee")
        
        else:  # seems that everything is ok
            choice = choice.content
            choice = choice.split()

            if choice[0] in possible_choice:
                if(len(choice) == 1):  # if the choice contains only 1 elem
                    if(choice[0].isdigit()):
                        return(choice[0])  # return the action
                
                    else:  # choice not digit
                        if(choice[0].lower == "flee"):  # flee the fight
                            return("flee")
                
                elif(len(choice) > 1):  # if more than one elem
                    if(choice[0].isdigit()):
                        return(choice[0])  # return the action
                        
                    if(choice[0].lower() == "check"):
                        if(choice[1].isdigit()):  # if the target is specified
                            if(int(choice[1])-1 <= len(team)):  # if the target is found
                                choice = [choice[0], choice[1]]
                                return(choice)
                            
                            else:
                                return("flee")
                        
                        else:
                            return("flee")
                    
                    else:
                        return("flee")
                
                else:
                    return("flee")

            else:
                return("flee")
        
        return("flee")
    
    async def wait_for_target(self, possible_target):
        """
        `coroutine`

        Allows the player to select a target among all the targetable units.

        --

        Return : `Character()` instance representing the chosen target.
        """

        # init
            # predicate
        def target_check(message):
            """
            Check if the passed target is correct.
            """
            if(message.author.id == self.player.id):
                target = message.content
                target = target.split()

                if(len(target) == 1):
                    if(target[0].isdigit()):
                        # the target format is correct
                        target = int(target[0])

                        # check if the target exists
                        if(target > 0 and target <= len(possible_target)): 
                            return(True)
                        
                        else:  # target doesnt exist
                            return(False)
                    
                    else:  # the target format is incorrect
                        return(False)
                
                else:  # format incorrect, len too big
                    return(False)
            
            else:  # not the right author
                return(False)
        
        # get the target
        try:
            target = await self.client.wait_for(
                "message",
                timeout = self.timeout,
                check = target_check
            )
        
        except asyncio.TimeoutError:
            return("flee")
        
        except Exception as error:
            print(f"(PLAYER TARGET : WAIT FOR) Error : {error}.")
            return("flee")
        
        else:
            target = target.content
            target = target.split()

            if(len(target) == 1):
                target = int(target[0])
                index = target - 1
                return(possible_target[index])
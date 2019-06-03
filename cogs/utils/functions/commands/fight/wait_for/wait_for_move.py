'''
Get the player's move.

Last update: 02/06/19
'''

# Dependancies

import asyncio
from time import strftime, gmtime

async def Wait_for_move(client, player, fighter, all_fighter):
    '''
    `coroutine`

    Wait for the player's choice.

    `client` : must be `discord.Client` object.

    `player` : must be `discord.Member` object.

    `fighter` : must be `Character` object.

    Return : bool (True if the choice has been registered successfully or False otherwise)
    '''

    # Init

    fighter_ability_count = fighter.ability_count
    success = False

    def Correct_move(message):
        if(message.author == player):
            choice = message.content
            choice = choice.split()

            if(len(choice) == 1):  # If there is only flee or ki charge
                if(choice[0].isdigit()):
                    choice[0] = int(choice[0])

                    if(choice[0] == 2 or choice[0] == 3):
                        return(True)
                    
                    else:  # Not flee or not ki charge
                        return(False)
                
                else:  # Non digit
                    return(False)
        
            elif(len(choice) == 2):
                if(choice[0].isdigit() and choice[1].isdigit()):
                    choice[0] = int(choice[0])
                    choice[1] = int(choice[1])

                    if(choice[0] > 0 and choice[0] <= fighter_ability_count+3 and choice[1] > 0 and choice[1] <= len(all_fighter)):  # +3 because of the 1. Sequence, 2. Charge and 3. Flee
                        return(True)  # All is ok
                    
                    else:  # choice superior to maximum solutions
                        return(False)
            
                else:  # not digits
                    return(False)
            
            else: # message lenght
                return(False)
        
        else:  # message author
            return(False)
    
    # Now we get the answer

    try:
        choice = await client.wait_for('message', timeout = 300, check = Correct_move)
    
    except asyncio.TimeoutError:
        success = False
        return(success, 'flee')
    
    except Exception as error:
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} Error in cogs.utils.functions.commands.fight.wait_for.wait_for_move.Wait_for.move() : l.54 : {}'.format(error_time, error))
        success = False
        pass
    
    else:
        success = True
    
    # If everything is good we return the choice

    if(success):
        choice = choice.content
        choice = choice.split()

        if(len(choice) == 1):
            choice[0] = int(choice[0])
            return(success, choice)
        
        elif(len(choice) == 2):
            choice[0] = int(choice[0])
            choice[1] = int(choice[1])
            return(success, choice)
    
    else:
        return(False)
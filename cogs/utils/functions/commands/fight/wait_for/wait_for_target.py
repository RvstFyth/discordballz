'''
Manages the wait for target.

Last update: 12/06/19
'''

# Dependancies

import asyncio
from time import strftime, gmtime

async def Wait_for_target(client, player, fighter, all_fighter):
    '''
    `coroutine`

    Ask the player for a correct target.

    `client` : must be `discord.Client` object.

    `player` : must be `discord.Member` object.

    `fighter` : must be `Character` object.

    Return: bool, int (success, target) return success and None if afk
    '''

    # Init

    success = False

    def Correct_target(message):
        if(message.author == player):
            target = message.content
            target = target.split()

            if(len(target) == 1):
                if(target[0].isdigit()):
                    target[0] = int(target[0])

                    if(target[0] > 0 and target[0] <= len(all_fighter)):  # If the target exists
                        return(True)
                    
                    else:  # If the target doesn't exists
                        return(False)
                
                else:  # If target is not digit
                    return(False)
            
            else:  # If there is more than one target
                return(False)
        
        else:  # If the message author is not correct
            return(False)
                    
    # Ask for the target 

    try:
        target = await client.wait_for('message', timeout = 300, check = Correct_target)

    except asyncio.TimeoutError:
        success = False
        return(success, None)
    
    except Exception as error:
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} Error in cogs.utils.functions.commands.fight.wait_for.Wait_for_target() : {}'.format(error_time, error))
        success = False
        pass
    
    else:
        success = True
    
    # Everything is good

    if success:
        target = target.content
        target = target.split()

        if(len(target) == 1):
            target[0] = int(target[0])
            return(success, target[0])
        
        else:
            pass
    
    else:
        return(False)
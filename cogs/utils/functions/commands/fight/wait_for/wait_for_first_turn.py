'''
Manages the input for the first turn

Last update: 29/06/19
'''

# dependancies

import asyncio

async def Wait_for_move_first_turn(client, player, fighter, all_fighter):
    '''
    `coroutine`

    Wait for the move during the first turn only.

    Return: bool, int
    '''

    # init
    succes = False

    def Correct_move(message):
        if(message.author.id == player.id):
            choice = message.content
            choice = choice.split()

            if(len(choice) == 1):
                if(choice[0].isdigit()):
                    choice[0] = int(choice[0])

                    if(choice[0] == 1 or choice[0] == 3):
                        return(True)
                    
                    else:  # if not 1 or 3
                        return(False)
                
                else:  # Non digit
                    if(choice[0].upper() == 'FLEE'):  # if flee
                        return(True)
                    
                    else:  # if not flee or see
                        return(False)
            
            elif(len(choice) == 2):
                if(choice[0].upper() == 'CHECK'):  # if player want to check a character
                    if(choice[1].isdigit()):  # if he defined the target
                        choice[1] = int(choice[1])

                        if(choice[1] <= len(all_fighter)):  # if the target is ok
                            return(True)
                        
                        else:  # if target not ok
                            return(False)
                    
                    else:  # if not target
                        return(False)
                
                else:  # if not check
                    return(False)
        
            else:
                return(False)
            
        else:  # if not player
            return(False)
    
    try:
        choice = await client.wait_for('message', timeout = 300, check = Correct_move)
    
    except asyncio.TimeoutError:
        succes = False
        return(succes, 'flee')
    
    else:
        success = True
    
    if success:
        choice = choice.content
        choice = choice.split()

        if(len(choice) == 1):
            if(choice[0].isdigit()):
                choice[0] = int(choice[0])
                return(success, choice[0])
            
            else:
                if(choice[0].upper() == 'FLEE'):
                    return(success, 'flee')
        
        elif(len(choice) == 2):
            if(choice[0].upper() == 'CHECK'):  # if check target
                if(choice[1].isdigit()):  # if correct
                    choice[1] = int(choice[1])

                    if(choice[1] <= len(all_fighter)):
                        choice[1] = int(choice[1])  
                        choice = ['CHECK', all_fighter[choice[1]-1], choice[1]]  # return ['CHECK', target.object, order]
                        return(success, choice)
        
        else:
            return(False)
    
    else:
        return(False)
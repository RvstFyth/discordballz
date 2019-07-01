'''
Manages the client.wait_for for the box.

Last update: 01/07/19
'''

# dependancies

import asyncio

async def Box_wait_for_reaction(client, message, player, reactions, current_page):
    '''
    `coroutine`

    Wait for reaction to be added to the message. If the reaction added is in reactions do something.

    `client` : must be `discord.Client` instance

    `message` : must be `discord.Message`

    `player` : must be `discord.Member` object representing the author

    `reaction` : must be `list` of `str(reaction)`

    `current_page` : must be `int` and represent the current page that is displayed for the box

    Return: int (next page to display), return false in case of error
    '''

    # init
    next_page = 0
    
    # check

    def Check_correct_reaction(reaction, reacted):
        '''
        Check if the reaction is correct.
        '''

        if(reaction.message.id == message.id):
            if(reacted.id == player.id):
                if(str(reaction.emoji) in reactions):
                    return(True)
                
                else:  # if the reaction isn't in the reactions list
                    return(False)
            
            else:  # if the player didn't reacted
                return(False)
        
        else:  # if the reaction isn't the box message
            return(False)
        
    try:  # catch the reactions
        reaction, user = await client.wait_for('reaction_add', timeout = 120, check = Check_correct_reaction)
    
    except asyncio.TimeoutError:  # if not reacted in time
        return('False')
    
    else:  # if it's ok
        if(str(reaction.emoji) == '⬅'):  # if the user wants to see the previous page
            next_page = current_page-1
        
        elif(str(reaction.emoji) == '➡'):  # wants to see the next page
            next_page = current_page+1
        
        elif(str(reaction.emoji) == '❌'):  # wants to close the thing
            next_page = 0  # 0 stop the loop and close all

        return(next_page)
    
    # basic return, in case of error
    return('False')
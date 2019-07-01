'''
Manages the box reactions.

Last update: 01/07/19
'''

# dependancies

import asyncio

async def Box_add_reaction(message, current_page, total_pages):
    '''
    `coroutine`

    Add the reactions onto the box message.

    `message` : must be `discord.Message`

    `current_page` : must be `int` and represent the current page of the box
    
    `total_pages` : must be `int` and represent the total number of pages

    Return: list[str(reaction)] the only possible reactions
    '''

    # init 

    left_arrow, right_arrow, close = '⬅', '➡', '❌'
    reactions = [close, left_arrow, right_arrow]

    # set up

    if(current_page == total_pages):  # if the user cannot open the next page
        reactions.remove(right_arrow)  # remove the right arrow reaction
    
    if(current_page == 1):  # if the user cannot open the previous page
        reactions.remove(left_arrow)
    
    # now add the reactions 

    for reaction in reactions:
        await asyncio.sleep(0)

        await message.add_reaction(emoji = reaction)
    
    return(reactions)
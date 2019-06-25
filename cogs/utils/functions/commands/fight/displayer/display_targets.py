'''
Displays the available targets

Last update: 25/06/19
'''

# dependancies

import asyncio

async def Display_targets(display, count, team_list):
    '''
    `coroutine`

    Display the available targets.

    `display` : must be type `str` and represent the message to display

    `count` : must be type `int` and represent the character count.

    `team_list` : must be the list of `Character` object to display in `display`

    Return: int, str (count, display)
    '''

    for character in team_list:
        await asyncio.sleep(0)

        if(character.current_hp <= 0):  # if dead
            display += '{}.💀**{}** {} | '.format(count, character.name, character.type_icon)
        
        else:  # alive
            display += '{}. {}**{}** {} | '.format(count, character.icon, character.name, character.type_icon)
        
        count += 1
    
    return(count, display)
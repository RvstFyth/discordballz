'''
Manages the displaying of the player_slots

Last update: 05/07/19
'''

# dependancies

import asyncio

# utils
from cogs.utils.functions.translation.gettext_config import Translate

from cogs.utils.functions.commands.slot.display_player_slots import Display_player_slots
from cogs.utils.functions.commands.box.box_reaction import Box_add_reaction
from cogs.utils.functions.commands.box.box_wait_for import Box_wait_for_reaction

async def Player_slot_manager(client, ctx, player, page):
    '''
    `coroutine`

    Update the player slot page.
    '''

    # init
    _ = await Translate(client, ctx)
    data = None

    while page > 0:
        await asyncio.sleep(0)

        slots, total_page, data = await Display_player_slots(client, ctx, ctx.message.author, page = page)

        reactions = await Box_add_reaction(slots, page, total_page)

        next_page = await Box_wait_for_reaction(client, slots, player, reactions, page)

        # check if error
        if(next_page == 'False'):  # if there an error occured
            await ctx.send(_('<@{}> An error occurred, closing the slots.').format(player.id))
            await slots.delete()  # closing the box message
            break  # stop everything
        
        else:  # if it's ok
            if(next_page == 0):  # close
                await slots.delete()  # delete the box if the user wanted to 
                break
            
            else:  # if the user didn't want to close
                await slots.delete()  # delete the message to replace it
                page = next_page  # define the new page to display
    
    return
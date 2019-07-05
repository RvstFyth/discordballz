'''
Manages the displaying of the unique id box.

Last update: 05/07/19
'''

# dependancies

import asyncio

# utils
from cogs.utils.functions.translation.gettext_config import Translate

from cogs.utils.functions.commands.box.id_box.id_box_displayer import Display_id_box
from cogs.utils.functions.commands.box.box_reaction import Box_add_reaction
from cogs.utils.functions.commands.box.box_wait_for import Box_wait_for_reaction

async def Box_id_manager(client, ctx, player, character_id, page):
    '''
    `coroutine`

    Update the page of the current oppened box id.
    '''

    # init
    _ = await Translate(client, ctx)
    data = None

    while page > 0:
        await asyncio.sleep(0)

        box, total_page, data = await Display_id_box(client, ctx, character_id, data = data, page = page)

        reactions = await Box_add_reaction(box, page, total_page)

        next_page = await Box_wait_for_reaction(client, box, player, reactions, page)

        # check if error
        if(next_page == 'False'):  # if there an error occured
            await ctx.send(_('<@{}> An error occurred, closing the box.').format(player.id))
            await box.delete()  # closing the box message
            break  # stop everything
        
        else:  # if it's ok
            if(next_page == 0):  # close
                await box.delete()  # delete the box if the user wanted to 
                break
            
            else:  # if the user didn't want to close
                await box.delete()  # delete the message to replace it
                page = next_page  # define the new page to display

        pass

    # end
    return
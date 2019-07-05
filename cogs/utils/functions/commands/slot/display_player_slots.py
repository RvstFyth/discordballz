'''
Manages the displaying of the player's slots.

Last update: 05/07/19
'''

# dependancies

import asyncio

# utils
from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.readability.embed import Basic_embed
from cogs.objects.character.characters_list.all_char import Get_char

# object

from cogs.objects.database import Database

async def Display_player_slots(client, ctx, player, data = None, page = 1):
    '''
    `coroutine`

    Display the player's slots.
    '''

    #init

    _ = await Translate(client, ctx)

    db = Database(client)
    await db.init()
    
    player = ctx.message.author
    slot_lines = ''  # each line of this string represents a slot
    total_pages = 0  # represent the total number of pages the player has access to
    max_to_display = 5  # represent the max number of character to display per page
    start_at = 0  # start the display at pos 0
    end_at = 4 # end after 10 character fetched
    page_to_display = page  # represent the page to display, default 1

    # manege which characters to display
    if(page_to_display > 1):
        start_at += (end_at+1)*(page_to_display-1)  # determines the first character to display, each page must display the char above the last char of the previous page
        end_at += max_to_display*(page_to_display-1)  # determines the max character to display, it displays +10 character more than the previous page

    # queries

    fetch_slot = 'SELECT player_slot FROM player_slot WHERE player_id = {};'.format(player.id)

    # fetching

    if not data == None:  # if the data is provided we use it
        player_slots = data

    else:  # if not we fetch again
        player_slots = await db.fetchval(fetch_slot)  # get the total number of distinct characters the player has
        player_slots = player_slots.split()
    
    if(player_slots[0].upper() == "NONE"):
        await ctx.send(_("<@{}> You did not set a character slot yet. To do so, use `slot add [unique id]`.").format(player.id))
        return

    total_pages = 1 + int(len(player_slots)/max_to_display)  # determines the total number of pages

    if(page_to_display > total_pages):
        await ctx.send(_('<@{}> This page doesn\'t exist.').format(player.id))
        return
    
    # last set up
    if(len(player_slots) < end_at):  # if there is less characters in the box than the max it can show up
        end_at = len(player_slots)
    
    # If everything is ok we start the displaying
    
    waiting_message = await ctx.send(_('<@{}> Displaying ...').format(player.id))

    # init
    slot_id = 1
    for row in range(start_at, end_at):
        await asyncio.sleep(0)
        
        unique_id = player_slots[row]  # each pos represent a unique id

        # get the character informations
        fetch_char_info = "SELECT character_global_id, character_level, character_rarity, character_type FROM character_unique WHERE character_unique_id = '{}';".format(unique_id)
        character_info = await db.fetch(fetch_char_info)

        global_id, level, rarity, char_type = character_info[0][0], character_info[0][1], character_info[0][2], character_info[0][3]

        # Get the character and init
        character = await Get_char(global_id)

        # set up the attributes
        character.level, character.rarity_value, character.type_value = level, rarity, char_type
        await character.init(client, ctx)

        # Add a line to the display
        slot_lines += _('`#{}`- {}__{}__ : lv.*{}* | {} | {}\n').format(slot_id, character.icon, character.name, character.level, character.type_icon, character.rarity_icon)
        slot_id += 1
    
    await db.close()
    # setup the embed
    display_box = Basic_embed(client, thumb = player.avatar_url)

    display_box.add_field(name = _('{}\'s box | Page {:,} / {:,} :').format(player.name, page_to_display, total_pages), value = slot_lines, inline = False)
    
    await waiting_message.delete()
    displayer = await ctx.send(embed = display_box)

    return(displayer, total_pages, data)
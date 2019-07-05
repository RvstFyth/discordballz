'''
Manages the display of the unique id box

Last update: 05/07/19
'''

# dependancies

import asyncio

# object

from cogs.objects.database import Database

# utils

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.objects.character.characters_list.all_char import Get_char
from cogs.utils.functions.readability.embed import Basic_embed

async def Display_id_box(client, ctx, character_id, data = None, page: int = 1):
    '''
    Displays the player's box based on the page passed.

    `client` : must be `discord.Client` instance.

    `ctx` : must be `discord.ext.commands.Context`

    `character_id` : must be `int` and represent the character global id.

    `data`[Optional] : represent the data we're walking through to display the characters in the box.

    `page`[Optional] : must be `int` default : 1

    Return: [discord.Message, int] ([box_embed, total_pages])
    '''

    #init

    _ = await Translate(client, ctx)

    db = Database(client)
    await db.init()
    
    player = ctx.message.author
    box_lines = ''  # each line of this string represents a character
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

    fetch_characters = 'SELECT character_unique_id, character_type, character_level FROM character_unique WHERE character_owner_id = {} ORDER BY character_level DESC;'.format(player.id)  # normalement SELECT DISTINCT

    # fetching

    if not data == None:  # if the data is provided we use it
        player_characters = data

    else:  # if not we fetch again
        player_characters = await db.fetch(fetch_characters)  # get the total number of distinct characters the player has

    total_pages = 1 + int(len(player_characters)/max_to_display)  # determines the total number of pages

    if(page_to_display > total_pages):
        await ctx.send(_('<@{}> This page doesn\'t exist.').format(player.id))
        return
    
    # last set up
    if(len(player_characters) < end_at):  # if there is less characters in the box than the max it can show up
        end_at = len(player_characters)
    
    # If everything is ok we start the displaying
    
    waiting_message = await ctx.send(_('<@{}> Displaying ...').format(player.id))
    
    for row in range(start_at, end_at):
        await asyncio.sleep(0)
        
        unique_id = player_characters[row][0]  # at pos [x][0] there is the unique id
        type_value = int(player_characters[row][1])
        level = int(player_characters[row][2])

        # Get the character and init
        character = await Get_char(character_id)
        character.type_value = type_value
        character.level = level
        await character.init(client, ctx)

        # Add a line to the display
        box_lines += _('`{}`- {}__{}__ : lv.*{:,}* | {} | {}\n').format(unique_id, character.icon, character.name, character.level, character.type_icon, character.rarity_icon)
    
    await db.close()
    # setup the embed
    display_box = Basic_embed(client, thumb = player.avatar_url)

    display_box.add_field(name = _('{}\'s box | Page {:,} / {:,} :').format(player.name, page_to_display, total_pages), value = box_lines, inline = False)
    
    await waiting_message.delete()
    displayer = await ctx.send(embed = display_box)

    return(displayer, total_pages, data)
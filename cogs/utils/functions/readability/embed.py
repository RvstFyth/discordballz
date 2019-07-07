'''
Manages the basic embed of the bot.

Last update: 06/07/19
'''

# Dependancies

import discord, time

# Config

from configuration.main_config.basic_config import V_MAJ,V_MED,V_MIN,V_BUILD,V_PHASE
from configuration.graphic_config.color_config import DEFAULT_THEME

def Basic_embed(client, title = None, thumb = None, footer = None, colour = None):
    '''
    Generates a custom embed.

    Return: `discord.Embed`
    '''

    # Init

    basic_embed = discord.Embed()
    footer_ = '{} v{}.{}.{}.{} {} | © 2019 - DrLarck & DrMegas'.format(client.user.name, V_MAJ, V_MED, V_MIN, V_BUILD, V_PHASE)

    if(colour != None):
        colour_ = colour
    
    else:
        colour_ = DEFAULT_THEME

    if(title != None):
        title_ = title
        basic_embed = discord.Embed(title = title_, colour = colour_)
    
    else:
        basic_embed = discord.Embed(colour = colour_)
    
    if(footer != None):
        footer_ = footer
    
    if(thumb != None):
        thumb_ = thumb
        basic_embed.set_thumbnail(url = thumb_)
    
    basic_embed.set_author(name = client.user.name, icon_url = client.user.avatar_url)
    basic_embed.set_footer(text = footer_)

    return(basic_embed)
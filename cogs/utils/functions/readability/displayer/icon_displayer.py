'''
Manages the way of how the icons are displayed.

Last update: 28/05/19
'''

# Dependancies

import asyncio

# Conf

from configuration.graphic_config.icons_config import *

async def Get_rarity_icon(rarity: int):
    '''
    `coroutine`

    Returns the icon of the passed rarity.

    `rarity` : must be type `int`

    Return: discord.Emoji (str)
    '''

    # Init 

    rarity_icon = ''

    # Normal

    if(rarity == 0):
        rarity_icon = ICON_N

        return(rarity_icon)
    
    # Rare

    if(rarity == 1):
        rarity_icon = ICON_R

        return(rarity_icon)
    
    # Super Rare

    if(rarity == 2):
        rarity_icon = ICON_SR

        return(rarity_icon)
    
    # Super super rare

    if(rarity == 3):
        rarity_icon = ICON_SSR

        return(rarity_icon)
    
    # Ultra rare

    if(rarity == 4):
        rarity_icon = ICON_UR

        return(rarity_icon)
    
    # Legendary

    if(rarity == 5):
        rarity_icon = ICON_LR

        return(rarity_icon)

async def Get_type_icon(type_ref: int):
    '''
    `coroutine`

    Return the type icon of the passed type.

    `type` : must be type `int`

    Return: discord.Emoji (str)
    '''

    # Init

    type_icon = ''

    # AGL

    if(type_ref == 0):
        type_icon = ICON_AGL

        return(type_icon)
    
    # TEQ

    if(type_ref == 1):
        type_icon = ICON_TEQ

        return(type_icon)
    
    # STR

    if(type_ref == 2):
        type_icon = ICON_STR

        return(type_icon)
    
    # PHY

    if(type_ref == 3):
        type_icon = ICON_PHY

        return(type_icon)
    
    # INT

    if(type_ref == 4):
        type_icon = ICON_INT

        return(type_icon)
'''
Manages the character displayer.

Last update: 30/06/19
'''

# Dependancies

import asyncio

# Utils

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.readability.embed import Basic_embed

# config

from configuration.graphic_config.color_config import N_COLOR, R_COLOR, SR_COLOR, SSR_COLOR, UR_COLOR, LR_COLOR

async def Display_character(client, ctx, character):
    '''
    `coroutine`

    Displays the player's fighter into embeded messages.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `character` : must be `Character` instance.

    Return: void (send messages)
    '''

    # Init

    _ = await Translate(client, ctx)
    
    character.level = 1
    await character.init(client, ctx)

    # Set embed
        # Values
    
    informations = _('__Name__ : **{}**\n__Saga__ : **{}**\n__Rarity__ : {}\n__Type__ : {}\n__Health__ : **{:,}** :hearts:')
    informations = informations.format(character.name, character.saga, character.rarity_icon, character.type_icon, character.max_hp)

    combat = _('__Physical damage__ : **{:,}** - **{:,}** :crossed_swords:\n__Ki power__ : **{:,}** - **{:,}** :rosette:\n__Armor__ : **{:,}** :shield:\n__Spirit__ : **{:,}** :rosette:')
    combat = combat.format(character.physical_damage_min, character.physical_damage_max, character.ki_damage_min, character.ki_damage_max, character.physical_defense, character.ki_defense)
    
    # color managment

    color = None

    if(character.rarity_value == 0):  # if N
        color = N_COLOR
    
    elif(character.rarity_value == 1):  # if R
        color = R_COLOR

    elif(character.rarity_value == 2):  # if SR
        color = SR_COLOR
    
    elif(character.rarity_value == 3):  # if SSR
        color = SSR_COLOR
    
    elif(character.rarity_value == 4):  # if UR
        color = UR_COLOR
    
    elif(character.rarity_value == 5):  # if LR
        color = LR_COLOR
    
    else:
        pass

    displayer = Basic_embed(client, colour = color, thumb = character.thumb)
    
    # Fields

    displayer.add_field(name = _('Informations :'), value = informations, inline = False)
    displayer.add_field(name = _('Combat :'), value = combat, inline = False)
    displayer.set_image(url = character.image)

    await ctx.send(embed = displayer)
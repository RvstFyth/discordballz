'''
Manages the character displayer.

Last update: 25/05/19
'''

# Dependancies

import asyncio

# Utils

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.readability.embed import Basic_embed

async def Display_character(client, ctx, character):
    '''
    `coroutine`

    Displays the player's fighter into embeded messages.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `character` : must be `Character` object.

    Return: void (send messages)
    '''

    # Init

    _ = await Translate(client, ctx)

    # Set embed
        # Values
    
    informations = _('__Name__ : **{}**\n__Type__ : {}\n__Level__ : **{:,}**\n__Health__ : {:,} / {:,} :hearts:\n__Ki__ : {:,} / {:,} :fire:')
    informations = informations.format(character.name, character.type_icon, 1, character.current_hp, character.max_hp, character.current_ki, character.max_ki)

    combat = _('__Damage range__ : {:,} - {:,} :crossed_swords:\n__Defense__ : {:,} :shield:')
    combat = combat.format(character.damage_min, character.damage_max, character.defense)

    displayer = Basic_embed(client)
    
    # Fields

    displayer.add_field(name = _('Informations :'), value = informations, inline = False)
    displayer.add_field(name = _('Combat :'), value = combat, inline = False)
    displayer.set_image(url = character.image)

    await ctx.send(embed = displayer)
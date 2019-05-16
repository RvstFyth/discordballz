'''
Manages the display of the player's team.

Last update: 16/05/19
'''

# Dependancies

import asyncio

# Objects

from cogs.objects.character import Character
from cogs.objects.player import Player

# Utils

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.readability.embed import Basic_embed

async def Display_player_fighter(client, ctx, player):
    '''
    `coroutine`

    Displays the player's fighter into embeded messages.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `player` : must be `discord.Member` object.

    Return: void (send messages)
    '''

    # Init

    player_ = Player(client, player)
    _ = await Translate(client, ctx)

    # Init Character object.

    character_ = Character(client, player, unique_id = await player_.fighter())

    # Set embed
        # Values
    
    name = _('__Name__ : {}').format(await character_.name())
    

    player_embed = Basic_embed(client, thumb = player_.avatar)
    player_embed.add_field(name = _('Informations :'), value = '{}'.format(name), inline = False)    
    player_embed.set_image(url = await character_.image())

    await ctx.send(embed = player_embed)
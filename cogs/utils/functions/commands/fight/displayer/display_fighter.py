'''
Manages the informations displayed about a fighter.

Last update: 10/06/19
'''

# Dependancies

import asyncio

# Utils

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.readability.embed import Basic_embed
from cogs.utils.functions.readability.displayer.icon_displayer import Get_type_icon

async def Pve_display_fighter(client, ctx, fighter, order_number:int):
    '''
    `coroutine`

    Displays the fighter's informations such as his current and max HPs.

    His stats, his buff/ debuff/ dot etc.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `fighter` : must be `Character` object.

    Return: discord.Message (embed)
    '''

    # Init

    _ = await Translate(client, ctx)

    display = Basic_embed(client, thumb = ctx.message.author.avatar_url)

    informations = _('__Name__ : **{}** {}\n__Health__ : {:,} / {:,}:hearts:\n__Ki__ : {:,} / {:,}:fire:\n__Physical damage__ : {:,} - {:,}:crossed_swords:\n__Ki damage__: {:,} - {:,}:rosette:\n__Armor__ : {:,} :shield:\n__Spirit__ : {:,} :rosette:').format(fighter.name, fighter.type_icon, fighter.current_hp, fighter.max_hp, fighter.current_ki, fighter.max_ki, fighter.physical_damage_min, fighter.physical_damage_max, fighter.ki_damage_max, fighter.ki_damage_min, fighter.physical_defense, fighter.ki_defense)
    
    if(len(fighter.buff) > 0):  # If the fighter has at least one buff, displays its icon and the durations
        for buff in fighter.buff:
            await asyncio.sleep(0)

            informations += _('\n__Buff__ :')
            informations += '{}x{} *({})* |'.format(buff.icon, buff.stack, buff.duration)
    
    if(len(fighter.debuff) > 0):
        for debuff in fighter.debuff:
            await asyncio.sleep(0)

            informations += _('\n__Debuff__ :')
            informations += '{}x{} *({})* |'.format(debuff.icon, debuff.stack, debuff.duration)
    
    if(len(fighter.dot) > 0):
        for dot in fighter.dot:
            await asyncio.sleep(0)

            informations += _('\n__Dot__ :')
            informations += '{}x{} *({})* |'.format(dot.icon, dot.stack, dot.duration)
    
    # Setting up the embed

    display.add_field(name = _('#{} - {}{}\'s turn :').format(order_number, fighter.icon, fighter.name), value = informations, inline = False)

    await ctx.send(embed = display)
'''
Manages the informations displayed about a fighter.

Last update: 28/05/19
'''

# Dependancies

import asyncio

# Utils

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.readability.embed import Basic_embed
from cogs.utils.functions.readability.displayer.icon_displayer import Get_type_icon

async def Pve_display_fighter(client, ctx, fighter):
    '''
    `coroutine`

    Displays the fighter's informations such as his current and max HPs.

    His stats, his buff/ debuff/ dot etc.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `fighter` : must be `Fighter` object.

    Return: discord.Message (embed)
    '''

    # Init

    _ = await Translate(client, ctx)

    display = Basic_embed(client)

    informations = _('__Name__ : **{}** {}\n__Health__ : {:,} / {:,} :hearts:\n__Damage range__ : {:,} - {:,} :crossed_swords:\n__Defense__ : {:,} :shield:\n').format(fighter.stat.name, fighter.stat.type, fighter.stat.current_hp, fighter.stat.max_hp, fighter.stat.damage_min, fighter.stat.damage_max, fighter.stat.defense)
    
    if(len(fighter.buff) > 0):  # If the fighter has at least one buff, displays its icon and the durations
        for buff in fighter.buff:
            await asyncio.sleep(0)

            informations += _('\n__Buff__ :')
            informations += '{}x{} *({})* |'.format(buff.buff_icon, buff.stack, buff.duration)
    
    if(len(fighter.debuff) > 0):
        for debuff in fighter.debuff:
            await asyncio.sleep(0)

            informations += _('\n__Debuff__ :')
            informations += '{}x{} *({})* |'.format(debuff.debuff_icon, debuff.stack, debuff.duration)
    
    if(len(fighter.dot) > 0):
        for dot in fighter.dot:
            await asyncio.sleep(0)

            informations += _('\n__Dot__ :')
            informations += '{}x{} *({})* |'.format(dot.dot_icon, dot.stack, dot.duration)
    
    # Setting up the embed

    display.add_field(name = _('{}\'s turn :').format(fighter.stat.name), value = informations, inline = False)

    await ctx.send(embed = display)
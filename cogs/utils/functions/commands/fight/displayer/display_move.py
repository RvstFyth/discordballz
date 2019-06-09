'''
Manages the displaying of the move

Last update: 01/06/19
'''

# Dependancies

import asyncio

# Utils

from cogs.utils.functions.translation.gettext_config import Translate

async def Display_move(client, ctx, move_name, move_icon, damage_done, fighter, target,  ki_gain = 0):
    '''
    `coroutine`

    Return the move displaying.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `move_name` : must be type `str` and represent the name of the move.

    `move_icon` : must be type `str` and represent a `discord.Emoji`.

    `damage_done` : must be type `int` and represent the damage the move has done.

    `ki_gain` : must be type `int` and represent the ki the fighter has gain thanks to the move, default : 0

    `fighter` : must be `Character` object.

    `target` : must be `Character` object.

    Return: str
    '''

    # Init

    _ = await Translate(client, ctx)

    move = _('__Move__ : `{}`{}\n__Damages__ : **{:,}**\n__Target__ : **{}** {}\n__Ki gain__ : {:,}\n__Ki remaining__ : {:,} / {:,}\n\n').format(move_name, move_icon, damage_done, target.name, target.type_icon, fighter.ki_regen+ki_gain, fighter.current_ki, fighter.max_ki)

    return(move)
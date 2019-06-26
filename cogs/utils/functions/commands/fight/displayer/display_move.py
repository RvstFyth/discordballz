'''
Manages the displaying of the move

Last update: 26/06/19
'''

# Dependancies

import asyncio

# Utils

from cogs.utils.functions.translation.gettext_config import Translate

async def Display_move(client, ctx, move_name, move_icon, damage_done, caster, target,  ki_gain = 0, is_ki = False, crit = 0):
    '''
    `coroutine`

    Return the move displaying.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `move_name` : must be type `str` and represent the name of the move.

    `move_icon` : must be type `str` and represent a `discord.Emoji`.

    `damage_done` : must be type `int` and represent the damage the move has done.

    `ki_gain` : must be type `int` and represent the ki the caster has gain thanks to the move, default : 0

    `caster` : must be `Character` object.

    `target` : must be `Character` object.

    Return: str
    '''

    # Init

    _ = await Translate(client, ctx)

    if(crit == 1):  # means crit
        crit = True
    
    else:
        crit = False

    if is_ki:
        if crit:
            move = _('__Move__ : `{}`{}\n__Damages__ : **-{:,}**:rosette: **CRITICAL** :boom:\n__Ki gain__ : {:,}\n__Ki remaining__ : {:,} / {:,}\n\n').format(move_name, move_icon, damage_done, ki_gain, caster.current_ki, caster.max_ki)
        
        else:
            move = _('__Move__ : `{}`{}\n__Damages__ : **-{:,}**:rosette:\n__Ki gain__ : {:,}\n__Ki remaining__ : {:,} / {:,}\n\n').format(move_name, move_icon, damage_done, ki_gain, caster.current_ki, caster.max_ki)
    else:
        if crit:
            move = _('__Move__ : `{}`{}\n__Damages__ : **-{:,}** **CRITICAL** :boom:\n__Ki gain__ : {:,}\n__Ki remaining__ : {:,} / {:,}\n\n').format(move_name, move_icon, damage_done, ki_gain, caster.current_ki, caster.max_ki)
        
        else:
            move = _('__Move__ : `{}`{}\n__Damages__ : **-{:,}**\n__Ki gain__ : {:,}\n__Ki remaining__ : {:,} / {:,}\n\n').format(move_name, move_icon, damage_done, ki_gain, caster.current_ki, caster.max_ki)

    return(move)
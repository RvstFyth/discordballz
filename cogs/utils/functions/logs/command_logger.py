'''
Manages the commands logs in the database.

Last update: 09/05/19
'''

# Dependancies

import asyncio
from time import strftime, gmtime

# Database

from cogs.utils.functions.database.insert.logs import Insert_in_logs_command

async def Command_log(client, ctx, caller, target = None):
    '''
    Insert into the database the informations about an used command.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `target` : if passed, must be `discord.Member` object.

    Return: void
    '''

    # Init

    caller = ctx.message.author
    command = ctx.command.name
    day = strftime('%d/%m/%y', gmtime())
    hour = strftime('%H:%M', gmtime())

    # Log
    # If the user mentionned someone

    if(target != None):
        await Insert_in_logs_command(client, caller, day, hour, command, target = target)
    
    else:
        await Insert_in_logs_command(client, caller, day, hour, command)
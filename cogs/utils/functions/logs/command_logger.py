'''
Manages the commands logs in the database.

Last update: 08/05/19
'''

# Dependancies

import asyncio
from time import strftime, gmtime

# Database

from cogs.utils.functions.database.insert.logs import Insert_in_logs_command

async def Command_log(client, ctx, command, caller, mention = None):
    '''
    Insert into the database the informations about an used command.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `command` : must be `str`.

    `mention` : if passed, must be `discord.Member` object.

    Return: void
    '''

    # Init

    caller = ctx.message.author
    command = command.lower()
    day = strftime('%d/%m/%y', gmtime())
    hour = strftime('%H:%M', gmtime())

    # Log
    # If the user mentionned someone

    if(mention != None):
        await Insert_in_logs_command(client, caller, day, hour, command, mention = mention)
    
    else:
        await Insert_in_logs_command(client, caller, day, hour, command)
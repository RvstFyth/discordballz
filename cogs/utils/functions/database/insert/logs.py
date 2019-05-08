'''
Manages the functions that insert informations in the logs tables.

Last update: 08/05/19
'''

# Dependancies

import asyncpg, time

async def Insert_in_logs_command(client, caller, day, hour, command, target = None):
    '''
    Insert a new log into the logs_commands table.

    `client` : must be `discord.Client` object.

    `caller` : must be `discord.Member` object that represents the `context.message.author`.

    `day`, `hour` and `command` : must be `str`.

    *[Optional: target]* : if passed, must be `discord.Member` object.

    Return: void
    '''

    # Init

    conn = await client.db.acquire()
    day = time.strftime('%d/%m/%y', time.gmtime())
    hour = time.strftime('%H:%M', time.gmtime())
    
    # Commands logs
    # If the caller has mentionned an other user :

    if(target != None):
        query = 'INSERT INTO logs_commands(day, hour, caller_id, caller_name, command_name, target_name, target_id) VALUES($1, $2, $3, $4, $5, $6, $7);'

        try:
            await conn.execute(query, day, hour, caller.id, caller.name, command, target.name, target.id)
        
        except Exception as error:
            error_time = time.strftime('%d/%m/%y', time.gmtime())
            print('{} - Error in cogs.utils.functions.database.insert.logs.Insert_in_logs_command() : l.39 : {}'.format(error_time, error))
            pass
        
        finally:
            await client.db.release(conn)
            return
    
    else:
        query = 'INSERT INTO logs_commands(day, hour, caller_id, caller_name, command_name) VALUES($1, $2, $3, $4, $5);'

        try:
            await conn.execute(query, day, hour, caller.id, caller.name, command)
        
        except Exception as error:
            error_time = time.strftime('%d/%m/%y', time.gmtime())
            print('{} - Error in cogs.utils.functions.database.insert.logs.Insert_in_logs_command() : l.57 : {}'.format(error_time, error))
            pass
        
        finally:
            await client.db.release(conn)
            return
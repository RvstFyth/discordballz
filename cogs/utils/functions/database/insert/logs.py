'''
Manages the functions that insert informations in the logs tables.

Last update: 07/05/19
'''

# Dependancies

import asyncpg, time

async def Insert_logs_summon(client, player):
    '''
    Insert informations about a summon into the logs tables.

    Return: void
    '''

    # Init

    conn = await client.db.acquire()
    command = 'summon'
    day = time.strftime('%d/%m/%y', time.gmtime())
    hour = time.strftime('%H:%M', time.gmtime())
    
    # Commands logs

    query = 'INSERT INTO logs_commands(day, time, command_name, caller_name, caller_id) VALUES($1, $2, $3, $4, $5);'

    try:
        await conn.execute(query, day, hour, command, player.name, player.id)
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y', time.gmtime())
        print('{} - Error in cogs.utils.functions.database.insert.logs.Insert_logs_summon() : l.30 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
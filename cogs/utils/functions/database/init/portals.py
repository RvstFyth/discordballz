'''
Manages the portals creation tables.

Last update: 12/05/19
'''

# Dependancies

import asyncpg, time
from time import strftime, gmtime

async def Create_regular_portal_table(client):
    '''
    Creates the regular_portal table.

    `client` : must be `discord.Client` object.

    Return: void
    '''

    # Init

    conn = await client.db.acquire()

    query = '''CREATE TABLE IF NOT EXISTS regular_portal(
        reference SERIAL PRIMARY KEY,
        portal_id BIGINT DEFAULT 0,
        name TEXT DEFAULT 'NONE',
        cost BIGINT DEFAULT 0,
        image TEXT DEFAULT 'NONE',
        legendary TEXT DEFAULT '0 0',
        scouter TEXT DEFAULT '0 0',
        out_scouter TEXT DEFAULT '0 0'
    );'''

    query_constraint = 'CREATE UNIQUE INDEX IF NOT EXISTS reference ON regular_portal(reference, portal_id);'

    try:
        await conn.execute(query)
        await conn.execute(query_constraint)
    
    except Exception as error:
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} Error in cogs.utils.functions.database.init.portals.Create_regular_portal_table() : l.39 - 40 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
'''
Manages the portals creation tables.

Last update: 27/05/19
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

    query = '''
    CREATE SEQUENCE IF NOT EXISTS regular_portal_reference_seq;
    CREATE TABLE IF NOT EXISTS regular_portal(
        reference BIGINT PRIMARY KEY DEFAULT nextval('regular_portal_reference_seq') NOT NULL,
        portal_id BIGINT DEFAULT 0,
        name TEXT DEFAULT 'NONE',
        cost BIGINT DEFAULT 0,
        image TEXT DEFAULT 'NONE',
        legendary TEXT DEFAULT 'NONE',
        scouter TEXT DEFAULT 'NONE',
        out_scouter TEXT DEFAULT 'NONE'
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
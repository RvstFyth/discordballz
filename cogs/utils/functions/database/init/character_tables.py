'''
Manages the character tables creation.

Last update: 12/05/19
'''

# Dependancies

import asyncpg, time
from time import strftime, gmtime

async def Create_unique_character_table(client):
    '''
    Create the unique character table.

    `client` : must be `discord.Client` object.

    Return: void
    '''

    # Init

    conn = await client.db.acquire()

    query = '''CREATE TABLE IF NOT EXISTS unique_characters(
        reference SERIAL PRIMARY KEY,
        unique_id TEXT DEFAULT 'NONE',
        global_id BIGINT,
        player_id BIGINT
        );'''
    
    query_contraint = 'CREATE UNIQUE INDEX IF NOT EXISTS reference ON unique_characters(reference);'

    try:
        await conn.execute(query)
        await conn.execute(query_contraint)
    
    except Exception as error:
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} Error in cogs.utils.functions.database.init.character_tables.Create_unique_character_table() : l.35 - 36 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)

async def Create_characters_table(client):
    '''
    Creates the tables that will contains all the characters informations.

    `client` : must be `discord.Client` object.

    Return: void
    '''

    # Init

    conn = await client.db.acquire()

    query = '''CREATE TABLE IF NOT EXISTS characters(
        reference SERIAL PRIMARY KEY,
        global_id BIGINT DEFAULT 0,
        name TEXT DEFAULT 'NONE',
        image_url TEXT DEFAULT 'NONE',
        base_rarity TEXT DEFAULT 'NONE',
        type TEXT DEFAULT 'NONE'
    );'''

    query_constraint = 'CREATE UNIQUE INDEX IF NOT EXISTS global_id ON characters(global_id, reference);'

    try:
        await conn.execute(query)
        await conn.execute(query_constraint)
    
    except Exception as error:
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} Error in cogs.utils.functions.database.init.character_tables.Create_characters_table() : l.71 - 72 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
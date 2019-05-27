'''
Manages the creation of the player's tables.

Last update: 27/05/19
'''

# Dependancies

import asyncpg, time

async def Create_player_tables(client):
    '''
    Create the different player's tables.

    Return: void
    '''

    # Init

    conn = await client.db.acquire()

    # Player table

    query = '''
    CREATE SEQUENCE IF NOT EXISTS player_register_order_seq;
    CREATE TABLE IF NOT EXISTS player(
        register_order BIGINT PRIMARY KEY DEFAULT nextval('player_register_order_seq') NOT NULL,
        player_id BIGINT,
        player_name TEXT,
        register_date TEXT DEFAULT 'NONE',
        language TEXT DEFAULT 'EN',
        location TEXT DEFAULT 'Unknown'
    );'''

    query_constraint = 'CREATE UNIQUE INDEX IF NOT EXISTS id ON player(player_id);'

    try:
        await conn.execute(query)
        await conn.execute(query_constraint)
        query, query_constraint = '', ''
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
        print('{} Error in cogs.utils.functions.database.init.player_tables.Create_player_tables() : l.34-36 : {}'.format(error_time, error))
        pass
    
    # Player ressources table

    query = '''
    CREATE SEQUENCE IF NOT EXISTS player_ressources_register_order_seq;
    CREATE TABLE IF NOT EXISTS player_ressources(
        register_order BIGINT PRIMARY KEY DEFAULT nextval('player_ressources_register_order_seq') NOT NULL,
        player_id BIGINT,
        player_name TEXT,
        player_stones BIGINT DEFAULT 0,
        player_zenis BIGINT DEFAULT 0,
        player_tower_tickets BIGINT DEFAULT 0
    );'''

    query_constraint = 'CREATE UNIQUE INDEX IF NOT EXISTS id ON player_ressources(player_id);'

    try:
        await conn.execute(query)
        await conn.execute(query_constraint)
        query, query_constraint = '', ''
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
        print('{} Error in cogs.utils.functions.database.init.player_tables.Create_player_tables() : l.57-59 : {}'.format(error_time, error))
        pass
    
    # Player experience table

    query = '''
    CREATE SEQUENCE IF NOT EXISTS player_experience_register_order_seq;
    CREATE TABLE IF NOT EXISTS player_experience(
        register_order BIGINT PRIMARY KEY DEFAULT nextval('player_experience_register_order_seq') NOT NULL,
        player_id BIGINT,
        player_name TEXT,
        player_level BIGINT DEFAULT 1,
        player_xp BIGINT DEFAULT 0,
        player_fighter TEXT DEFAULT 'NONE'
    );'''

    query_constraint = 'CREATE UNIQUE INDEX IF NOT EXISTS id ON player_experience(player_id);'

    try:
        await conn.execute(query)
        await conn.execute(query_constraint)
        query, query_constraint = '', ''
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
        print('{} Error in cogs.utils.functions.database.init.player_tables.Create_player_tables() : l.79-81 : {}'.format(error_time, error))
        pass

    # Player combat table

    query = '''
    CREATE SEQUENCE IF NOT EXISTS player_combat_register_order_seq;
    CREATE TABLE IF NOT EXISTS player_combat(
        register_order BIGINT PRIMARY KEY DEFAULT nextval('player_combat_register_order_seq') NOT NULL,
        player_id BIGINT,
        fighter_a TEXT DEFAULT 'NONE',
        fighter_b TEXT DEFAULT 'NONE',
        fighter_c TEXT DEFAULT 'NONE',
        team_leader TEXT DEFAULT 'NONE'
    );
    '''

    query_constraint = 'CREATE UNIQUE INDEX IF NOT EXISTS player_id ON player_combat(player_id);'

    try:
        await conn.execute(query)
        await conn.execute(query_constraint)
        query, query_constraint = '', ''
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
        print('{} Error in cogs.utils.functions.database.init.player_tables.Create_player_tables() : l.116-118 : {}'.format(error_time, error))
        pass
    
    await client.db.release(conn)
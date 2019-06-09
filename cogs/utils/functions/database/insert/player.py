'''
These functions manages the insert statments into the player's tables.

Last update: 08/05/19
'''

# Dependancies

import asyncpg, time

async def Insert_in_player(client, player, date):
    '''
    `client` : must be `discord.Client` object or `discord.ext.commands.AutoShardedBot` one.

    `player` : must be `discord.Member` object.

    `date` : must be `str` object. Moreover, it should have this format `DD/MM/YY`.

    Return: void
    '''

    # Init

    conn = await client.db.acquire()

    # We insert the player's basic information to the database

    query = 'INSERT INTO player(player_id, player_name, register_date) VALUES($1, $2, $3);'

    try:
        await conn.execute(query, player.id, player.name, date)
    
    # Represents the unique constraint violation error, we don't do anything

    except asyncpg.UniqueViolationError as error:
        pass
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
        print('{} Error in cogs.utils.functions.database.insert.player.Insert_in_player() : l.31 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)

async def Insert_in_player_ressources(client, player):
    '''
    Insert the player's informations in the player_ressources table.

    `client` : must be `discord.Client` or `discord.ext.commands.AutoShardedBot` object.

    `player` : must be `discord.Member` object.

    Return: void
    '''

    # Init

    conn = await client.db.acquire()

    query = 'INSERT INTO player_ressources(player_id, player_name) VALUES($1, $2);'

    try:
        await conn.execute(query, player.id, player.name)
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
        print('{} Error in cogs.utils.functions.database.insert.player.Insert_in_player_ressources() : l.64 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)

async def Insert_in_player_experience(client, player):
    '''
    Insert the player's informations in the player_experience table.

    `client` : must be `discord.Client` object.

    `player` : must be `discord.Member` object.

    Return: void
    '''

    # Init

    conn = await client.db.acquire()

    query = 'INSERT INTO player_experience(player_id, player_name) VALUES($1, $2);'

    try:
        await conn.execute(query, player.id, player.name)
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
        print('{} Error in cogs.utils.functions.database.insert.player.Insert_in_player_experience() : l.92 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)

async def Insert_in_player_combat(client, player):
    '''
    `coroutine`

    Insert player's info into player_combat table.

    `client` : must be `discord.Client` object.

    `player` : must be `discord.Member` object.

    Return: void
    '''

    # Init

    conn = await client.db.acquire()

    query = '''
    INSERT INTO player_combat(player_id)
    VALUES($1);
    '''

    try:
        await conn.execute(query, player.id)
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
        print('{} - Error in cogs.utils.functions.database.insert.player.Insert_in_player_combat() : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
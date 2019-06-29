'''
Allow you to manage the connection to a database.

Last update: 29/05/19
'''

# Dependancies

import asyncio, asyncpg, time

# Config

from configuration.main_config.database_config import DB_HOST,DB_NAME, DB_PASSWORD, DB_USER

async def Connection_to_database(client):
    '''
    Create `client.db` to allow you to connect to the database.

    `client.db.acquire()` : Will allow you to create a connection to the database.

    `client.db.release(connection)` : Will drop the connection to the database.

    Return: New client instance.
    '''

    # Init
    
    client.db = await asyncpg.create_pool(user = DB_USER, host = DB_HOST, database = DB_NAME, password = DB_PASSWORD)

    return
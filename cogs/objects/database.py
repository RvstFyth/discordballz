'''
Simple database manager.

Last update: 09/06/19
'''

# Dependancies

import asyncio, asyncpg
from time import strftime, gmtime

class Database:
    '''
    Simple database manager.

    `client` : must be `discord.Client` object.

    Attributes :
    - client : represent `discord.Client.db`
    - conn : represent a connection to the database.

    Methods :
    - coro init : Connection to the database
    - coro close : Close the connection to the database
    - coro execute : Execute a statment
    - coro fetchval : Fetch a value (default return None)
    - coro fetch : Fetch a row (default return None)
    '''

    def __init__(self, client):
        # Basic
        self.client = client.db
        self.conn = None
    
    # Method

    async def init(self):
        '''
        `coroutine`

        Connection to the database.
        '''

        self.conn = await self.client.acquire()

        return
    
    async def close(self):
        '''
        `coroutine`

        Close the connection to the database.
        '''

        await self.client.release(self.conn)

        return
    
    # Statments

    async def execute(self, query):
        '''
        `coroutine`

        Execute a statment. 

        `query` : must be `PostgreSQL` statment.

        Return: void
        '''

        try:
            await self.conn.execute(query)
        
        except Exception as error:
            error_time = strftime('%d/%m/%y - %H:%M', gmtime())
            print('{} - (EXECUTE) Error with the query : \'{}\' ({})'.format(error_time, query, error))
            pass
        
        return

    async def fetchval(self, query):
        '''
        `coroutine`

        Fetch a value.

        `query` : must be `PostgreSQL` statment.

        Return: value or None
        '''
        
        # Init

        value = None

        try:
            value = await self.conn.fetchval(query)
        
        except Exception as error:
            error_time = strftime('%d/%m/%y - %H:%M', gmtime())
            print('{} - (FETCH VAL) Error with the query : \'{}\' ({})'.format(error_time, query, error))
            pass
        
        return(value)
    
    async def fetch(self, query):
        '''
        `coroutine`

        Fetch a row.

        `query` : must be `PostgreSQL` statment.

        Return: row or None
        '''
        
        # Init

        row = None

        try:
            row = await self.conn.fetch(query)
        
        except Exception as error:
            error_time = strftime('%d/%m/%y - %H:%M', gmtime())
            print('{} - (FETCH ROW) Error with the query : \'{}\' ({})'.format(error_time, query, error))
            pass
        
        return(row)
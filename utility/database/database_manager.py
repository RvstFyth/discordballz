"""
A simple asynchronous PostgreSQL database manager.

--

Author : DrLarck

Last update : 08/01/2020 (DrLarck)
"""

# dependancies

import asyncio, asyncpg

from os import environ

# database manager
class Database:
    """
    A simple asynchronous PostgreSQL database manager.

    The `connect()` and `close()` method are automatically managed.

    - Parameter :

    `handler` : Represent the pool connection handler.

    - Attribute :

    `pool` : Represent the connection pool.

    - Method :

    Connection :

    :coro:`init()` : Return the connection pool to the database.

    :coro:`connect()` : Connect the database to allow you execute queries.

    :coro:`close()` : Release the connection to the database.

    :coro:`stop()` : Stop the connection to the database by releasing the connection pool.
    
    :coro:`execute(query)` : Execute the query.

    :coro:`fetchval(query)` : Fetch a value.

    :coro:`fetch(query)` : Fetch rows.
    """

    # attribute
    def __init__(self, handler):
        self.pool = handler
        self.connection = None

        # database configuration
        self.config = {
            "user" : environ["DBZ_DB_USER"],
            "password" : environ["DBZ_DB_PASSWORD"],
            "host" : environ["DBZ_DB_HOST"],
            "database" : environ["DBZ_DB_NAME"],
            "port" : "5432"
        }
    
    # method
        # connection managment
    async def init(self):
        """
        `coroutine`

        Create the connection pool to the database.

        --

        Return : Connection pool.
        """

        pool = await asyncpg.create_pool(
            host = self.config["host"],
            port = self.config["port"],
            database = self.config["database"],
            user = self.config["user"],
            password = self.config["password"]
        )

        return(pool)
    
    async def connect(self):
        """
        `coroutine`

        Connect the database.

        --

        Return : None
        """

        self.connection = await self.pool.acquire()

        return
    
    async def close(self):
        """
        `coroutine`

        Release the connection to the database.

        --

        Return : None
        """

        await self.pool.release(self.connection)

        return
    
    async def stop(self):
        """
        `coroutine`

        Stop the connection to the database by releasing the connection pool.

        --

        Return : None
        """

        await self.pool.close()

        return
    
        # queries managment
    async def execute(self, query, parameters=None):
        """
        `coroutine`
        
        Execute the passed `query` as parameter.

        - Parameter :

        `query` : Represent a `PostgreSQL` query.

        --

        Return : None
        """

        # init
        if parameters is None:
            parameters = []
        await self.connect()

        try:
            await self.connection.execute(query, parameters)
        
        except asyncpg.UniqueViolationError:  # ignore the unique constraint violation
            pass
        
        except Exception as error:
            print(f"(DATABASE : EXECUTE) - Error while executing the query : {query} : {error}.")
            pass
        
        finally:
            await self.close()

        return
    
    async def fetchval(self, query):
        """
        `coroutine`

        Fetch a value from the database.

        - Parameter :

        `query` : Represent a `PostgreSQL` query.

        --

        Return : fetched value or None if not found
        """

        # init
        await self.connect()
        value = None

        try:
            value = await self.connection.fetchval(query)
        
        except Exception as error:
            print(f"(DATABASE : FETCH VAL) - Error while executing the query : {query} : {error}.")
            pass
        
        finally:
            await self.close()
        
        return(value)
    
    async def fetch(self, query):
        """
        `coroutine`

        Fetch rows by executing the query.

        - Parameter : 

        `query` : Represent a `PostgreSQL` query.

        --

        Return : list of rows or None if not found
        """

        # init
        await self.connect()
        rows = None

        try:
            rows = await self.connection.fetch(query)
        
        except Exception as error:
            print(f"(DATABASE : FETCH) - Error while executing the query : {query} : {error}.")
            pass
        
        finally:
            await self.close()
        
        return(rows)
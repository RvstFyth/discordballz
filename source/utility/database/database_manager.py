"""
A simple asynchronous PostgreSQL database manager.

--

Author : DrLarck

Last update : 13/07/19
"""

# dependancies

import asyncio, asyncpg

from os import environ

# database manager
class Database:
    """
    A simple asynchronous PostgreSQL database manager.

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
            "database" : "dev_dbz3",
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
    
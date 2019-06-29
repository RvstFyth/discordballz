'''
Create the database tables

Last update: 29/06/19
'''

# dependancies

import asyncio
from discord.ext import commands, tasks

# object

from cogs.objects.database import Database

class Create_tables(commands.Cog):
    '''
    Create the database tables.
    '''

    def __init__(self, client):
        self.client = client
        self.db = Database(self.client)
        self.create_tables.start()
    
    # method

    @tasks.loop(count = 1)
    async def create_tables(self):
        '''
        `coroutine`

        Task : create the tables.
        '''

        # init
        await self.db.init()

        # Player info query
        player_info = '''
        CREATE SEQUENCE IF NOT EXISTS player_info_reference_seq;
        CREATE TABLE IF NOT EXISTS player_info(
            reference BIGINT PRIMARY KEY DEFAULT nextval('player_info_reference_seq') NOT NULL,
            player_id BIGINT,
            player_name TEXT,
            player_register_date TEXT,
            player_lang TEXT,
            player_location TEXT DEFAULT 'UNKNOWN'
        );

        CREATE UNIQUE INDEX IF NOT EXISTS player_info_id ON player_info(player_id);
        '''

        # execute the query
        await self.db.execute(player_info)

        # Player combat info
        player_combat_info = '''
        CREATE TABLE IF NOT EXISTS player_combat_info(
            player_id BIGINT,
            player_name TEXT,
            player_leader TEXT,
            player_fighter_a TEXT,
            player_fighter_b TEXT,
            player_fighter_c TEXT
        );

        CREATE UNIQUE INDEX IF NOT EXISTS player_combat_info_id ON player_combat_info(player_id);
        '''

        await self.db.execute(player_combat_info)

        # Character unique
        char_unique = '''
        CREATE SEQUENCE IF NOT EXISTS character_unique_reference_seq;
        CREATE TABLE IF NOT EXISTS character_unique(
            reference BIGINT PRIMARY KEY DEFAULT nextval('character_unique_reference_seq') NOT NULL,
            character_unique_id TEXT DEFAULT 'NONE',
            character_global_id BIGINT,
            character_type INTEGER DEFAULT 0,
            character_rarity INTEGER DEFAULT 0,
            character_level BIGINT DEFAULT 0,
            character_owner_id BIGINT,
            character_owner_name TEXT
        );

        CREATE UNIQUE INDEX IF NOT EXISTS character_unique_reference ON character_unique(reference);
        '''
        
        await self.db.execute(char_unique)

        # close the database
        await self.db.close()
    
    @create_tables.before_loop
    async def before_creation(self):
        '''
        `coroutine`

        Wait for the client to be ready.
        '''

        await self.client.wait_until_ready()

        return
    
    @create_tables.after_loop
    async def after_creation(self):
        '''
        `coroutine`

        Send a message once it's finished and close the task.
        '''

        print('BACKGROUND : Create_tables : DONE')

        self.create_tables.close()

        return
'''
Runs all the tasks.

Last update: 12/05/19
'''

# Dependancies

import time

# Tasks

from cogs.utils.functions.database.init.database_connection import Connection_to_database

# Data

from cogs.utils.functions.database.init.character_tables import Create_unique_character_table, Create_characters_table
from cogs.utils.functions.database.init.logs_tables import Create_logs_tables
from cogs.utils.functions.database.init.player_tables import Create_player_tables
from cogs.utils.functions.database.init.portals import Create_regular_portal_table

def Task_runner(client):
    '''
    The purpose of this function is to run the tasks.

    Return: void
    '''

    # Database
    # Defines the connection to the database

    client.loop.run_until_complete(Connection_to_database(client))

        # Tables creation
    
    client.loop.run_until_complete(Create_regular_portal_table(client))
    client.loop.run_until_complete(Create_characters_table(client))
    client.loop.run_until_complete(Create_logs_tables(client))
    client.loop.run_until_complete(Create_player_tables(client))
    client.loop.run_until_complete(Create_unique_character_table(client))
'''
Runs all the tasks.

Last update: 08/05/19
'''

# Dependancies

import time

# Tasks

from cogs.utils.functions.database.init.database_connection import Connection_to_database

# Data

from cogs.utils.functions.database.init.logs_tables import Create_logs_tables
from cogs.utils.functions.database.init.player_tables import Create_player_tables

def Task_runner(client):
    '''
    The purpose of this function is to run the tasks.

    Return: void
    '''

    # Database
    # Defines the connection to the database

    client.loop.run_until_complete(Connection_to_database(client))

        # Tables creation
    
    client.loop.run_until_complete(Create_logs_tables(client))
    client.loop.run_until_complete(Create_player_tables(client))
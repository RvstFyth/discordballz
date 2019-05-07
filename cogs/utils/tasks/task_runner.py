'''
Runs all the tasks.

Last update: 07/05/19
'''

# Dependancies

import time

# Tasks

from cogs.utils.functions.database.database_connection import Connection_to_database

def Task_runner(client):
    '''
    The purpose of this function is to run the tasks.

    Return: void
    '''

    # Database
    # Defines the connection to the database

    client.loop.run_until_complete(Connection_to_database(client))
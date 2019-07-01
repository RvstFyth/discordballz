'''
Runs all the tasks.

Last update: 30/06/19
'''

# Dependancies

# tasks

from cogs.utils.tasks.database_table_creation import Create_tables
from cogs.utils.tasks.presence import Presence_manager

class Task_runner:
    '''
    Manages the background tasks.
    '''

    def __init__(self, client):
        self.client = client
    
    # method

    def run_tasks(self):
        '''
        Run all the tasks.

        Return: dict with class instances when needed
        '''

        # init
        instance = {}
    
        # tables creation

        Create_tables(self.client)

        # Change presence

        Presence_manager(self.client)

        # return the instances
        return(instance)
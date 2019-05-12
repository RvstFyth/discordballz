'''
Generates ids for characters.

Last update: 12/05/19
'''

# Dependancies

import asyncio, time, string
from string import ascii_letters

async def Unique_id_generator(client, char):
    '''
    Generates a unique id for a character based on the 'aaaa0' system.

    If the id already exists, generate an other one.

    `client` : must be `discord.Client` object.

    `char` : must be type `int`, this is the 'father id' that is asked.

    Return: void
    '''

    # Init

    


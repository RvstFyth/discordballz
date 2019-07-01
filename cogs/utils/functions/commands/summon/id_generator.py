'''
Generates ids for characters.

Last update: 30/06/19
'''

# Dependancies

import asyncio, time, string
from time import strftime, gmtime
from string import ascii_letters

# object

from cogs.objects.database import Database

async def Unique_id_generator(client, reference):
    '''
    Generates a unique id for a character based on the 'aaaa0' system.

    If the id already exists, generate an other one.

    `client` : must be `discord.Client` object.

    `reference` : must be type `int`.

    Return: void
    '''

    # Init

    vd = reference
    l1, l2, l3, l4, n = 0,0,0,0,0
    la, lb, lc, ld = ascii_letters, ascii_letters, ascii_letters, ascii_letters

    # First we store the bigest value in 'n', 'n' can store 7 311 616 values

    n = int((vd/pow(52, 4)))
    vd -= n*pow(52, 4)      # We substract it because the other tiers cannot handle huge amount

    # The fourth letter can store 140 608 values

    l4 = int(vd/pow(52, 3))
    vd -= l4*pow(52, 3)

    # The third one can store 2 704 values

    l3 = int(vd/pow(52, 2))
    vd -= l3*pow(52, 2)

    # The second one can store 52 values

    l2 = int(vd/52)
    vd -= l2*52

    # This one is the unit
    
    l1 = vd 

    code = '{}{}{}{}{}'.format(la[l1],lb[l2],lc[l3],ld[l4],n)

    return(code)

async def Create_unique_id(client):
    '''
    `coroutine`

    Create a unique id for all the character with 'NONE' as unique id based on their
    
    reference number.

    `client` : must be `discord.Client` object.

    Return: void
    '''

    # Init

    db = Database(client)
    await db.init()

    all_unique_char = []  # Fetch

    query = "SELECT * FROM character_unique WHERE character_unique_id = 'NONE';"

    all_unique_char = await db.fetch(query)
    
    # Now we generate a new id for all the char

    for a in range(len(all_unique_char)):
        await asyncio.sleep(0)

        reference = all_unique_char[a][0]
        unique_id = await Unique_id_generator(client, reference)

        # Once we have the unique id we update the unique at 
        # the reference

        query = "UPDATE character_unique SET character_unique_id = '{}' WHERE reference = {};".format(unique_id, reference)

        await db.execute(query)

    # End

    await db.close()

    return
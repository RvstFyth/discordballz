'''
Manages the SQL statment for the regular_portals table.

Last update: 12/05/19
'''

# Dependancies

import asyncpg
from time import strftime, gmtime

async def Select_regular_portal_infos(client, portal):
    '''
    Return a dict containing all the portal informations.

    `client` : must be `discord.Client` object.

    `portal` : must be type `int` and represent the portal_id.

    Return: dict

    Values :
    1. name
    2. cost
    3. image
    4. legendary
    5. scouter
    6. out of scouter
    '''

    # Init

    portal_fetch = None
    portal_infos = {}
    conn = await client.db.acquire()

    query = 'SELECT * FROM regular_portal WHERE portal_id = $1;'

    try:
        portal_fetch = await conn.fetch(query, portal)
    
    except Exception as error:
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} Error in cogs.utils.functions.database.select.portal.regular_portal.Select_regular_portal_infos() : l.33 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
    
    portal_infos['name'] = portal_fetch[0][2]
    portal_infos['cost'] = portal_fetch[0][3]
    portal_infos['image'] = portal_fetch[0][4]
    portal_infos['legendary'] = portal_fetch[0][5]
    portal_infos['scouter'] = portal_fetch[0][6]
    portal_infos['out of scouter'] = portal_fetch[0][7]

    return(portal_infos)

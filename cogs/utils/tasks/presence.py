'''
Manages the presences.

Last update: 30/06/19
'''

# dependancies

import asyncio, discord
from discord.ext import commands, tasks

# config

from configuration.main_config.basic_config import V_MIN, V_MED, V_MAJ, V_BUILD, V_PHASE

class Presence_manager(commands.Cog):
    '''
    Manages the presence, change it and update it.
    '''

    def __init__(self, client):
        self.client = client
        self.change_presence.start()

    def cog_unload(self):
        '''
        On cog unload
        '''

        self.change_presence.close()

        return

    # method
    @tasks.loop(hours = 1)  # call it every hours
    async def change_presence(self):
        '''
        `coroutine`

        Change the discord presence.
        '''

        activity = discord.Game('v{}.{}.{}.{} {}'.format(V_MAJ, V_MED, V_MIN, V_BUILD, V_PHASE))

        await self.client.change_presence(activity = activity)

        pass
    
    @change_presence.before_loop
    async def before_change(self):
        '''
        `coroutine`

        Wait for the client to be ready
        '''

        await self.client.wait_until_ready()

        return
    
    @change_presence.after_loop
    async def after_change(self):
        '''
        `coroutine`

        Confirmation
        '''

        print('BACKGROUND : Presence_manager : DONE')

        return
'''
Manages the `on_ready()` event.

Last update: 07/05/19
'''

# Dependancies

import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog

# Config

from configuration.main_config.basic_config import V_MAJ,V_MED,V_MIN,V_BUILD,V_PHASE

class On_Ready(Cog):
    def __init__(self, client):
        self.client = client
    
    @Cog.listener()
    async def on_ready(self):
        '''
        Displays the following messages when the bot is ready.
        '''
    
        # Init
        ready_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
        server_count = len(self.client.guilds)
        bot_name = self.client.user.name 
        version = f'v{V_MAJ}.{V_MED}.{V_MIN}::{V_BUILD} - {V_PHASE}'

        # Display

        display_message = f'\n\n{ready_time} - {bot_name} : READY !\n\nConnected to {server_count} servers.\n\n{version}\n__________________________'
        
        print(display_message)

def setup(client):
    client.add_cog(On_Ready(client))
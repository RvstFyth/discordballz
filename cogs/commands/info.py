'''
Manages how the informations of a character are displayed.

Last update: 04/06/19
'''

# Dependancies

import asyncio, discord
from discord.ext.commands import Cog, command

# Utils

from cogs.utils.functions.commands.info.display_character_info import Display_character_info

class Cmd_Info(Cog):
    def __init__(self, client):
        self.client = client

    @command()
    async def info(self, ctx, character: int):
        '''
        Displays the informations of a character.
        '''

        await Display_character_info(self.client, ctx, character)
        
def setup(client):
    client.add_cog(Cmd_Info(client))
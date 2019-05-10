'''
Manages the summon feature.

Last update: 07/05/19
'''

# Dependancies

import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog

class Cmd_Summon(Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def summon(self, ctx):
        '''
        Allows the player to summon a character.
        '''

        # Init
        
        player = ctx.message.author

def setup(client):
    client.add_cog(Cmd_Summon(client))
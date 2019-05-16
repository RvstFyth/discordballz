'''
'''

import discord, asyncio
from discord.ext import commands
from discord.ext.commands import Cog

# Utils

from cogs.utils.functions.commands.fight.fight_system import Fight

class Cmd_Fight(Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fight(self, ctx):
        
        await Fight(self.client, ctx, ctx.message.author)
        
def setup(client):
    client.add_cog(Cmd_Fight(client))
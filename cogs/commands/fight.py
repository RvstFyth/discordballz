'''
'''

import discord, asyncio
from discord.ext import commands
from discord.ext.commands import Cog

# Utils

from cogs.utils.functions.commands.fight.fight_system import Pve_Fight

from cogs.objects.character.characters_list.char_1 import Char_1

class Cmd_Fight(Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fight(self, ctx):
        
        enemy = Char_1()
        liste = [enemy]
        
        await Pve_Fight(self.client, ctx, ctx.message.author, liste)
        
def setup(client):
    client.add_cog(Cmd_Fight(client))
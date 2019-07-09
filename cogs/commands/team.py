'''
Manages the team display

Last update : 09/07/19
'''

# dependancies

import discord, asyncio
from discord.ext import commands

# object

from cogs.objects.player.player import Player

class Cmd_Team(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def team(self, ctx):
        player = ctx.message.author
        player = Player(self.client, player)

        await player.fighter.display_team(ctx)

def setup(client):
    client.add_cog(Cmd_Team(client))
'''
Manages the start command and its behaviour.

Last update: 28/06/19
'''

# Dependancies

import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog

# Check

from cogs.utils.functions.check.player.player_checks import Is_not_registered

# Database

from cogs.utils.functions.logs.command_logger import Command_log
from cogs.utils.functions.database.insert.player import Insert_in_player, Insert_in_player_ressources, Insert_in_player_experience, Insert_in_player_combat

class Cmd_Start(Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check(Is_not_registered)
    async def start(self, ctx):
        '''
        Register a member into the database.
        '''

        # Init

        player = ctx.message.author
        date = time.strftime('%d/%m/%y', time.gmtime())

        # Logs

        await Command_log(self.client, ctx, 'start', player)

        # Insert informations into the database

        await Insert_in_player(self.client, player, date)
        await Insert_in_player_ressources(self.client, player)
        await Insert_in_player_experience(self.client, player)
        await Insert_in_player_combat(self.client, player)

        await ctx.send('<@{}> Hello and welcome to the **Discord Ball Z 3.0 BETA** ! 🎉\n\nYou have access to all available characters. The only feature that you can test out for the moment is the **fight** one.\nFight are now **3vX**, so you have to set up your **3 fighters** and a **leader** to perform a fight. To do so, follow these instructions bellow :\n\nTo assign a fighter, do : `d!fighter a/b/c [num]`\nTo assign a leader : `d!fighter leader [num]`\n\nYou have access to all characters, you don\'t need to summon them or something.\n\nFinally, to access a fight, just type `d!fight`, it will generate random opponent team.\n\nDon\'t hesitate to <#585203135845236737>, to see all the character list, just go to <#585202631475986432>.\n\nI hope this new version will please you and have fun !'.format(player.id))

def setup(client):
    client.add_cog(Cmd_Start(client))
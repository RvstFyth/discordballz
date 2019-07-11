'''
Manages the start command and its behaviour.

Last update: 11/07/19
'''

# Dependancies

import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog

# object

from cogs.objects.database import Database

# Check

from cogs.utils.functions.check.player.player_checks import Is_not_registered

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
        date = time.strftime('%d/%m/%y', time.gmtime())  # register date

        db = Database(self.client)

        # Insert informations into the database
            # into player info
        player_info = '''
        INSERT INTO player_info(player_id, player_name, player_register_date)
        VALUES({}, '{}', '{}');
        '''
        player_info = player_info.format(player.id, player.name, date)

            # into player combat info
        player_combat = '''
        INSERT INTO player_combat_info(player_id, player_name)
        VALUES({}, '{}')
        '''
        player_combat = player_combat.format(player.id, player.name)

            # into player ressource
        player_ressource = '''
        INSERT INTO player_resource(player_id, player_name)
        VALUES({}, '{}');
        '''
        player_ressource = player_ressource.format(player.id, player.name)

            # into player slot
        player_slot = f'''
        INSERT INTO player_slot(player_id, player_name)
        VALUES({player.id}, \'{player.name}\')
        '''

        # execute the queries
        await db.execute(player_info)
        await db.execute(player_combat)
        await db.execute(player_ressource)
        await db.execute(player_slot)

        # close the connection
        await ctx.send('<@{}> Hello and welcome to the **Discord Ball Z 3.0 BETA** ! 🎉\n\nYou have access to all available characters. The only feature that you can test out for the moment is the **fight** one.\nFight are now **3vX**, so you have to set up your **3 fighters** and a **leader** to perform a fight. To do so, follow these instructions bellow :\n\nTo assign a fighter, do : `d!fighter a/b/c [num]`\nTo assign a leader : `d!fighter leader [num]`\n\nYou have access to all characters, you don\'t need to summon them or something.\n\nFinally, to access a fight, just type `d!fight`, it will generate random opponent team.\n\nDon\'t hesitate to <#585203135845236737>, to see all the character list, just go to <#585202631475986432>.\n\nI hope this new version will please you and have fun !'.format(player.id))

def setup(client):
    client.add_cog(Cmd_Start(client))
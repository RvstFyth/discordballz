'''
Manages the summon feature.

Last update: 07/05/19
'''

# Dependancies

import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog

# Object

from cogs.objects.character import Character

# Translation

from cogs.utils.functions.translation.gettext_config import Translate

# Embed

from cogs.utils.functions.readability.embed import Basic_embed

# Summon

from cogs.utils.functions.commands.summon.summoner import Summoner

class Cmd_Summon(Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def summon(self, ctx):
        '''
        Allows the player to summon a character.
        '''

        # Init

        _ = await Translate(self.client, ctx)
        player = ctx.message.author

        drawn_char = await Summoner(self.client, 1)
        if(drawn_char == '0 0'):
            print('error')
            return

        character_ = Character(self.client, int(drawn_char))

        # Embed

        summon_embed = Basic_embed(self.client, thumb = player.avatar_url)
        summon_embed.add_field(name = _('{}\'s summon :').format(player.name), value = _('Congratulation **{}** ! You\'ve summoned **{}** !').format(player.name, await character_.name()))
        
        await ctx.send(embed = summon_embed)

def setup(client):
    client.add_cog(Cmd_Summon(client))
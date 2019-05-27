'''
Manages the summon feature.

Last update: 07/05/19
'''

# Dependancies

import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog

# Config

from configuration.main_config.portal_config import REGULAR_PORTAL

# Object

from cogs.objects.character import Character
from cogs.objects.player import Player

from configuration.characters.characters_list.all_char import Get_char

# Translation

from cogs.utils.functions.translation.gettext_config import Translate

# Embed

from cogs.utils.functions.readability.embed import Basic_embed

# Summon

from cogs.utils.functions.commands.summon.summoner import Summoner

# Database

from cogs.utils.functions.database.insert.character import Insert_unique_character
from cogs.utils.functions.database.select.portal.regular_portal import Select_regular_portal_infos
from cogs.utils.functions.commands.summon.id_generator import Create_unique_id

class Cmd_Summon(Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def summon(self, ctx, portal = None):
        '''
        Allows the player to summon a character.
        '''

        # Init

        _ = await Translate(self.client, ctx)
        player = ctx.message.author
        player_ = Player(self.client, player)
        portal = await Select_regular_portal_infos(self.client, REGULAR_PORTAL)

        if(await player_.stones() >= portal['cost']):

            drawn_char = await Summoner(self.client, REGULAR_PORTAL)

            if(drawn_char != 'NONE'):
                # If the player actually drawn an existing character

                await player_.remove_stones(portal['cost'])
                character_ = await Get_char(drawn_char)
                

                # Embed

                summon_embed = Basic_embed(self.client, thumb = player.avatar_url)
                summon_embed.add_field(name = _('{}\'s summon :').format(player.name), value = _('Congratulation **{}** ! You\'ve summoned **{}** !').format(player.name, character_.name))
                summon_embed.set_image(url = character_.image)

                # Unique character

                await Insert_unique_character(self.client, player, drawn_char)
                await Create_unique_id(self.client)

                await ctx.send(embed = summon_embed)
        
        else:
            # If the player doesn't have enough ressources to summon

            await ctx.send(_('<@{}> You don\'t have enough **Dragon stones** to summon in this portal. You need **{}** but you have *{}*.').format(player.id, portal['cost'], await player_.stones()))

def setup(client):
    client.add_cog(Cmd_Summon(client))
'''
Manages the summon feature.

Last update: 01/07/19
'''

# Dependancies

import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog
from random import randint

# Config

from configuration.main_config.banner_config import REGULAR_PORTAL
from configuration.graphic_config.icons_config import ICON_DS

# Object

from cogs.objects.database import Database
from cogs.objects.player import Player
from cogs.objects.banner import Regular_banner

# Translation

from cogs.utils.functions.translation.gettext_config import Translate

# Utils

from cogs.utils.functions.readability.displayer.character_displayer import Display_character

# Database

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

        db = Database(self.client)

        player_ = Player(self.client, player)
        await player_.init()

        portal_ = Regular_banner(self.client)
        await portal_.init()

        if(player_.stone >= portal_.cost):  # if the player has enough stone to summon a character
            drawn_character = await portal_.summon()
            drawn_character.type_value = randint(0, 4)

            # remove al lhe resources from the player's inventory
            await player_.remove_dragonstone(portal_.cost)

            # insert the character into the db

            insert_drawn_character = '''
            INSERT INTO character_unique(character_global_id, character_type, character_rarity, character_owner_id, character_owner_name)
            VALUES({}, {}, {}, {}, '{}');
            '''
            insert_drawn_character = insert_drawn_character.format(drawn_character.id, drawn_character.type_value, drawn_character.rarity_value, player.id, player.name)

            await db.execute(insert_drawn_character)

            # generat unique id

            await Create_unique_id(self.client)

            # display the character
            await Display_character(self.client, ctx, drawn_character)

            return
        
        else:
            await ctx.send(_('<@{}> You do not have enough {}**Dragon stones** to summon *({:,} / {:,})*.').format(player_.id, ICON_DS, player_.stone, portal_.cost))
            return
        
def setup(client):
    client.add_cog(Cmd_Summon(client))
'''
Manages the player characters slots

Last update: 05/07/19
'''

# dependancies

import asyncio
from discord.ext import commands

# object

from cogs.objects.database import Database
from cogs.objects.player.player import Player

# utils
from cogs.utils.functions.translation.gettext_config import Translate

from cogs.utils.functions.commands.slot.player_slot_manager import Player_slot_manager
from cogs.objects.character.characters_list.all_char import Get_char

class Cmd_slot(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.group(invoke_without_command = True)
    async def slot(self, ctx):
        '''
        Display the player's characters slots.

        Called only if the player didn't use any subcommand.
        '''
        
        # init
        player = ctx.message.author

        await Player_slot_manager(self.client, ctx, player, 1)
    
    @slot.command()
    async def add(self, ctx, unique_id: str):
        '''
        Allow the player to add a character into his character slot.
        '''

        player = ctx.message.author
        player = Player(self.client, player)

        await player.slot.add(ctx, unique_id)
        return
    
    @slot.command()
    async def remove(self, ctx, slot_id: int):
        '''
        Allow the player to remove a character by using the slot id.
        '''

        # init

        player = ctx.message.author
        player = Player(self.client, player)

        await player.slot.remove(ctx, slot_id)

        return

def setup(client):
    client.add_cog(Cmd_slot(client))
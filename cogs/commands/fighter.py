'''
Manages the player team.

Last update: 09/07/19
'''

# Dependancies

import discord, asyncio
from discord.ext import commands
from discord.ext.commands import Cog, command, check

# Object

from cogs.objects.character.characters_list.all_char import Get_char
from cogs.objects.database import Database
from cogs.objects.player.player import Player

# Utils

class Cmd_fighter(Cog):
    def __init__(self, client):
        self.client = client
    
    @command()
    async def fighter(self, ctx, slot: str, character):
        '''
        `coroutine`

        Allow a player to assign a fighter to a slot of his team.

        `slot` : must be type `str` : 'leader', 'a', 'b', 'c'

        `character` : ALPHA must be type `str`. If the character matches with an unique id, its good, if it's a digit, we pass the id stored at the id-1
        '''

        # Init

        player = ctx.message.author
        player = Player(self.client, player)
        slot = slot.upper()
        
        if slot == 'A':
            await player.fighter.define_fighter(ctx, "player_fighter_a", character, "Fighter A")

        if slot == 'B':
            await player.fighter.define_fighter(ctx, "player_fighter_b", character, "Fighter B")
        
        if slot == 'C':
            await player.fighter.define_fighter(ctx, "player_fighter_c", character, "Fighter C")
                    
        else:
            pass

def setup(client):
    client.add_cog(Cmd_fighter(client))
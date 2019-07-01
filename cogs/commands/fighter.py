'''
Manages the player team.

Last update: 01/07/19
'''

# Dependancies

import discord, asyncio
from discord.ext import commands
from discord.ext.commands import Cog, command, check

# Object

from cogs.objects.character.characters_list.all_char import Get_char
from cogs.objects.database import Database

# Utils

from cogs.utils.functions.translation.gettext_config import Translate

class Cmd_fighter(Cog):
    def __init__(self, client):
        self.client = client
    
    @command()
    async def fighter(self, ctx, slot: str, character: int):
        '''
        `coroutine`

        Allow a player to assign a fighter to a slot of his team.

        `slot` : must be type `str` : 'leader', 'a', 'b', 'c'

        `character` : ALPHA must be type `int` (Release: str for unique id) and represent a character.
        '''

        # Init

        _ = await Translate(self.client, ctx)

        db = Database(self.client)
        await db.init()

        player = ctx.message.author
        slot = slot.upper()
        
        # Set leader
        if slot == 'LEADER' or slot == 'LEAD':
            if character > 0:  # If the character global id is not 0 or less

                valid_char = await Get_char(character)  # Check if the character exists

                if(valid_char == None):
                    await ctx.send(_('<@{}> Character not found.').format(player.id))
                
                else:
                    query = f'''
                    UPDATE player_combat_info SET player_leader = {character} WHERE player_id = {player.id};
                    '''

                    await db.execute(query)
                    await db.close()

                    await ctx.send(_('<@{}> `Leader` assigned succesfully.').format(player.id))
        
        if slot == 'A':
            if character > 0:

                valid_char = await Get_char(character)

                if(valid_char == None):
                    await ctx.send(_('<@{}> Character not found.').format(player.id))
                
                else:
                    query = f'''
                    UPDATE player_combat_info SET player_fighter_a = {character} WHERE player_id = {player.id};
                    '''

                    await db.execute(query)
                    await db.close()

                    await ctx.send(_('<@{}> `Fighter A` assigned succesfully.').format(player.id))

        if slot == 'B':
            if character > 0:

                valid_char = await Get_char(character)

                if(valid_char == None):
                    await ctx.send(_('<@{}> Character not found.').format(player.id))
                
                else:
                    query = f'''
                    UPDATE player_combat_info SET player_fighter_b = {character} WHERE player_id = {player.id};
                    '''

                    await db.execute(query)
                    await db.close()

                    await ctx.send(_('<@{}> `Fighter B` assigned succesfully.').format(player.id))
        
        if slot == 'C':
            if character > 0:

                valid_char = await Get_char(character)

                if(valid_char == None):
                    await ctx.send(_('<@{}> Character not found.').format(player.id))
                
                else:
                    query = f'''
                    UPDATE player_combat_info SET player_fighter_c = {character} WHERE player_id = {player.id};
                    '''

                    await db.execute(query)
                    await db.close()

                    await ctx.send(_('<@{}> `Fighter C` assigned succesfully.').format(player.id))
                    
        else:
            pass

def setup(client):
    client.add_cog(Cmd_fighter(client))
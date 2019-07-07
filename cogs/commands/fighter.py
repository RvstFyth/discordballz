'''
Manages the player team.

Last update: 07/07/19
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

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.database.character_unique.character_info import Character_from_unique

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

        _ = await Translate(self.client, ctx)

        db = Database(self.client)

        player = ctx.message.author
        player = Player(self.client, player)
        slot = slot.upper()
        
        # Set leader
        if slot == 'LEADER' or slot == 'LEAD':
            if(character.isdigit()):  # if the player wants to set a slot as a character.
                slot_id = int(character)-1  # -1 because we get the slot id from a list
                player_slot = await player.slot.check()

                if(slot_id <= len(player_slot) and slot_id >= 0):  # positiv number and in range of the list
                    character = player_slot[slot_id]  # get the character unique id
                
                else:  # invalid slot
                    await ctx.send(_("<@{}> Wrong slot number. Please define a new character slot using `slot add [unique id]` command.").format(player.id))

                # convert the character
                character_ = await Character_from_unique(self.client, ctx, player, character)

                if not character is None:  # if the character has been found
                    query = f"UPDATE player_combat_info SET player_leader = '{character}' WHERE player_id = {player.id};"  # send the unique id to the database.

                    await db.execute(query)

                    await ctx.send(_("<@{}> The character {}__{}__ lv.{} | {} | {} has been set as **Team Leader**.").format(player.id, character_.icon, character_.name, character_.level, character_.type_icon, character_.rarity_icon))
                
                else:  # not found
                    await ctx.send(_("<@{}> Character not found.").format(player.id))

            else:  # if it's a unique id
                query = f"SELECT character_global_id FROM character_unique WHERE character_owner_id = {player.id} AND character_unique_id = '{character}';"

                global_id = await db.fetchval(query)

                if global_id is None:
                    await ctx.send(_("<@{}> The `unique id` is incorrect.").format(player.id))
                
                else:  # if valid
                    update = f"UPDATE player_combat_info SET player_leader = '{character}' WHERE player_id = {player.id};"

                    await db.execute(update)

                    character_ = await Character_from_unique(self.client, ctx, player, character)

                    await ctx.send(_("<@{}> The character {}__{}__ lv.{} | {} | {} has been set as **Team Leader**.").format(player.id, character_.icon, character_.name, character_.level, character_.type_icon, character_.rarity_icon))
                
                    pass
        
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

                    await ctx.send(_('<@{}> `Fighter C` assigned succesfully.').format(player.id))
                    
        else:
            pass

def setup(client):
    client.add_cog(Cmd_fighter(client))
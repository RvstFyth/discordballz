'''
Manages the player characters slots

Last update: 05/07/19
'''

# dependancies

import asyncio
from discord.ext import commands

# object

from cogs.objects.database import Database

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

        # init
        _ = await Translate(self.client, ctx)
        player = ctx.message.author
        db = Database(self.client)

        # queries
        fetch_character = "SELECT character_global_id FROM character_unique WHERE character_unique_id = '{}' AND character_owner_id = {};".format(unique_id, player.id)
        fetch_player_slot = "SELECT player_slot FROM player_slot WHERE player_id = {};".format(player.id)
        
        # execute the queries

        await db.init()
        character = await db.fetchval(fetch_character)

        if(character != None):  # if the player owns the character
            player_slot = await db.fetchval(fetch_player_slot)
            player_slot = player_slot.split()
            
            # if player slot is "NONE" we reset it
            if player_slot[0] == "NONE":
                player_slot = ""
            
            if not unique_id in player_slot:  # if the character is not already there
                player_slot = " ".join(player_slot)  # convert list to str
                player_slot += " {}".format(unique_id)

                # now update the slot
                update_player_slot = "UPDATE player_slot SET player_slot = '{}' WHERE player_id = {};".format(player_slot, player.id)
                await db.execute(update_player_slot)

                # get the character info
                fetch_character_info = "SELECT character_global_id, character_level, character_type, character_rarity FROM character_unique WHERE character_unique_id = '{}';".format(unique_id)
                char_info = await db.fetch(fetch_character_info)

                global_id, level, char_type, rarity = int(char_info[0][0]), int(char_info[0][1]), int(char_info[0][2]), int(char_info[0][3])

                # define character
                _character = await Get_char(global_id)
                _character.level, _character.type_value, _character.rarity_value = level, char_type, rarity 

                await _character.init(self.client, ctx)

                await ctx.send(_("<@{}> You've successfully added {}__{}__ lv.{} | {} | {} to your slots !").format(player.id, _character.icon, _character.name, _character.level, _character.type_icon, _character.rarity_icon))
                pass

            else:  # character already added
                await ctx.send(_("<@{}> This character is already in your slots.").format(player.id))
                pass
        
        else:
            await ctx.send(_("<@{}> It seems that you do not own this character or the character doesn't exist. Please enter the `unique` id of your character.\nExample : `aaaa0`.\n\nTo find the unique id of your character, use `box [global id]`.").format(player.id))
            pass

        await db.close()
        return
    
    @slot.command()
    async def remove(self, ctx, slot_id: int):
        '''
        Allow the player to remove a character by using the slot id.
        '''

        # init

        _ = await Translate(self.client, ctx)   
        player = ctx.message.author
        db = Database(self.client)

        if(slot_id > 0):
            pass
        
        else:
            await ctx.send(_("<@{}> Please pass a slot id that is higher than 0.").format(player.id))
            return
        
        # queries

        fetch_player_slot = "SELECT player_slot FROM player_slot WHERE player_id = {};".format(player.id)

        # fetching
        await db.init()
        player_slot = await db.fetchval(fetch_player_slot)
        await db.close()

        if(player_slot == 'NONE'):  # if the player has nothing in slot just don't do anything
            await ctx.send(_("<@{}> You have nothing to remove.").format(player.id))
        
        else:
            player_slot = player_slot.split()
            character_unique_id = player_slot[slot_id-1]  # get the unique id
            player_slot.remove(player_slot[slot_id-1])  # -1 because the slot are counted from 1

            if(len(player_slot) > 0):  # if the list is not empty after the remove
                player_slot = " ".join(player_slot)  # convert to str
            
            else:
                player_slot = "NONE"  # reset to None
            
            update_player_slot = "UPDATE player_slot SET player_slot = '{}' WHERE player_id = {};".format(player_slot, player.id)

            await db.init()
            await db.execute(update_player_slot)
            await db.close()

            # get the character info
            fetch_character_info = "SELECT character_global_id, character_level, character_type, character_rarity FROM character_unique WHERE character_unique_id = '{}';".format(character_unique_id)

            await db.init()
            character_info = await db.fetch(fetch_character_info)
            await db.close()

            global_id, level, rarity, char_type = int(character_info[0][0]), int(character_info[0][1]), int(character_info[0][3]), int(character_info[0][2])

            character = await Get_char(global_id)
            character.level, character.rarity_value, character.type_value = level, rarity, char_type
            await character.init(self.client, ctx)

            await ctx.send(_('<@{}> You\'ve successfully removed {}__{}__ lv.{} | {} | {} from your characters slots.').format(player.id, character.icon, character.name, character.level, character.type_icon, character.rarity_icon))
            
            return
        
        return


def setup(client):
    client.add_cog(Cmd_slot(client))
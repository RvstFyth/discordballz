'''
Manages the slot object.

Last update: 07/07/19
'''

# dependancies

import asyncio

# object

from cogs.objects.database import Database

# utils

from cogs.utils.functions.translation.gettext_config import Translate

from cogs.utils.functions.database.character_unique.character_info import Character_from_unique

class Slot:
    '''
    Represent the player's slots pannel.

    `client` : must be `discord.Client` instance.

    `player` : must be `discord.Member` instance.

    Method :
        coro check() : Return list[player_slot], list of str
    '''

    def __init__(self, client, player):
        self.client = client
        self.player = player
    

    # methods

    async def check(self):
        '''
        `coroutine`

        Check that the character slot is still up to date.

        If a character is not owned by the player anymore, remove it from the
        slots.

        Return: list[player_slot]
        '''

        # init
        db = Database(self.client)

        # queries

        fetch_slot = f'SELECT player_slot FROM player_slot WHERE player_id = {self.player.id};'
        
        # execute the queries

        await db.init()
        player_slot = await db.fetchval(fetch_slot)
        await db.close()

        player_slot = player_slot.split()

        # now check if it is up to date
        if player_slot[0] == "NONE":  # if the player slot is set to default = empty
            pass
        
        else:
            for unique_id in player_slot:
                await asyncio.sleep(0)

                fetch_character = f'SELECT character_global_id FROM character_unique WHERE character_owner_id = {self.player.id} AND character_unique_id = \'{unique_id}\';'
                
                await db.init()
                character = await db.fetchval(fetch_character)
                await db.close()

                # check if the player owns the character
                if character is None:  # if the player doesn't own the character, just remove it
                    player_slot.remove(unique_id)
                    pass
                
                else:
                    pass
            
            if not len(player_slot) > 0:  # if the list is empty, return NONE at 0
                update_slot = f"UPDATE player_slot SET player_slot = 'NONE' WHERE player_id = {self.player.id};"

                await db.init()
                await db.execute(update_slot)
                await db.close()

                player_slot = ["NONE"]

        # return the player slot as a list
        return(player_slot)
    
    async def add(self, ctx, unique_id):
        '''
        `coroutine`

        Add a character to player slot if the player owns the character and if 
        the character isn't already declared in the player slots.

        `ctx` : must `discord.ext.commands.Context`

        `unique_id` : must be `str` and represent the unique id of a character.

        Return : discord.Message (confirmation)
        '''

        # init

        db = Database(self.client)
        player_slot = await self.check()
        _ = await Translate(self.client, ctx)

        # queries
        # fetch the global id of the character, get None if not found
        fetch_character = f"SELECT character_global_id FROM character_unique WHERE character_owner_id = {self.player.id} AND character_unique_id = '{unique_id}';"

        # execute
        await db.init()
        global_id = await db.fetchval(fetch_character)
        await db.close()

        if not global_id is None:  # if the character has been found

            if unique_id in player_slot:  # if the character is already defined
                await ctx.send(_("<@{}> This character has a reserved slot already, try with another one.").format(self.player.id))
                return
            
            if player_slot[0] == "NONE":
                player_slot[0] = " "

            player_slot = " ".join(player_slot)  # convert to str
            player_slot += f" {unique_id}"

            # now update the player_slot
            update_slot = f"UPDATE player_slot SET player_slot = '{player_slot}' WHERE player_id = {self.player.id};"

            await db.init()
            await db.execute(update_slot)
            await db.close()

            # get the character

            character = await Character_from_unique(self.client, ctx, self.player, unique_id)

            await ctx.send(_("<@{}> You've successfully added {}__{}__ lv.{} | {} | {} to your character slots !").format(self.player.id, character.icon, character.name, character.level, character.type_icon, character.rarity_icon))
            
            return
        
        else:
            await ctx.send(_("<@{}> You do not own this character or the passed id is wrong. Please use `box [global id]` to verify that you own the character, then pass the `unique id` as `aaaa0` format.").format(self.player.id))
            
        return
    
    async def remove(self, ctx, slot_id: int):
        '''
        `coroutine`

        Remove character from the slot. Then update the database.
        '''

        # init 
        _ = await Translate(self.client, ctx)
        db = Database(self.client)
        player_slot = await self.check()

        if slot_id > 0:  # Ok
            unique_id = player_slot[slot_id-1]
            player_slot.remove(player_slot[slot_id-1])

            # check if the slots are empty now
            if not len(player_slot) > 0:
                player_slot = ["NONE"]

            # update
            new_slot = " ".join(player_slot)

            # quries
            update_slot = f"UPDATE player_slot SET player_slot = '{new_slot}';"

            await db.init()
            await db.execute(update_slot)
            await db.close()

            character = await Character_from_unique(self.client, ctx, self.player, unique_id)

            await ctx.send(_("<@{}> You've successfully removed `{}` - {}__{}__ lv.{} | {} | {} from your character slots !").format(self.player.id, unique_id, character.icon, character.name, character.level, character.type_icon, character.rarity_icon))
        
        else:
            await ctx.send(_("<@{}> You can only delete slots higher than `0`.").format(self.player.id))
        
        return
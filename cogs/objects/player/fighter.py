'''
Manages the fighter selection of the player.

Last update: 09/07/19
'''

# dependancies

import asyncio

# object

from cogs.objects.database import Database

# utils

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.readability.embed import Basic_embed
from cogs.utils.functions.readability.displayer.icon_displayer import Get_rarity_icon
from cogs.utils.functions.database.character_unique.character_info import Character_from_unique

class Fighter:
    '''
    Allow the player to manage his fighters.

    `client` : must be `discord.Client`

    `player` : must be :class:`Player()`

    Attributes :
        - client : represents the used client.
        - player : represents the player.
        - db : represents the database.
    
    Methods:
        - coro 

    '''

    def __init__(self, client, player):
        self.client = client
        self.player = player
        self.db = Database(self.client)

    # methods

    async def define_fighter(self, ctx, fighter_slot, character_id, slot_name):
        '''
        `coroutine`

        Set up the fighter passed as `fighter_slot`. If the `character_id` arg isdigit(), we look for the player.slot.

        `ctx` : must be `discord.ext.commands.Context`

        `fighter_slot` : must be `str` : represent the slot like : "fighter_a"

        `character_id` : `str` or `int` :
            if `int` : check the player.slot, look for the slot, if the slot exists, pick up the unique id stored in it.
            if `str` : check if the player owns it, if he does, define the fighter.
        
        `slot_name` : must be `str` and represent the slot name.
        
        Return: bool (success or failure)
        '''

        # init

        _ = await Translate(self.client, ctx)
        player_team_id = await self.get_team(ctx, True)  # get the team as str
        player_team_instance = await self.get_team(ctx)  # get the team as instance of char()
        player_team_global = []  # reference the global id of the character in the team

        for char in player_team_instance:  # get the global id of the characters
            await asyncio.sleep(0)

            player_team_global.append(char.id)
        
        # define the fighter

        if(character_id.isdigit()):  # if it's a number
            slot_id = int(character_id)-1
            player_slot = await self.player.slot.check()  # get the player slot

            if(player_slot[0] == 'NONE'):  # if the player_slot is empty
                await ctx.send(_(f"<@{self.player.id}> Your character slots are empty. Please define a new slot using `slot add [unique id]` or pass a `unique id` to the `fighter` command."))
                return

            if(slot_id < len(player_slot) and slot_id >= 0):  # positiv number and in range of the list, we already did slot_id - 1
                character = player_slot[slot_id]  # get the character unique id
                
                # check if the character has already been defined in the team
                if character in player_team_id:
                    await ctx.send(_(f"<@{self.player.id}> This character is already in your team."))
                    return
            
            else:  # invalid slot
                await ctx.send(_(f"<@{self.player.id}> Wrong slot number. Please define a new character slot using `slot add [unique id]` command."))
                return

            # convert the character
            character_ = await Character_from_unique(self.client, ctx, self.player, character)

            # the player cannot have the same character instance more than one time
            if character_.id in player_team_global:
                await ctx.send(_(f"<@{self.player.id}> An identical character is already in your team."))
                return

            if not character is None:  # if the character has been found
                query = f"UPDATE player_combat_info SET {fighter_slot} = '{character}' WHERE player_id = {self.player.id};"  # send the unique id to the database.

                await self.db.execute(query)

                await ctx.send(_(f"<@{self.player.id}> The character {character_.icon}__{character_.name}__ lv.{character_.level} | {character_.type_icon} | {character_.rarity_icon} has been set as **`{slot_name}`**."))
            
            else:  # not found
                await ctx.send(_(f"<@{self.player.id}> Character not found."))
                return

        else:  # if it's a unique id
            query = f"SELECT character_global_id FROM character_unique WHERE character_owner_id = {self.player.id} AND character_unique_id = '{character_id}';"

            global_id = await self.db.fetchval(query)

            if global_id is None:  # check if the player owns the char
                await ctx.send(_(f"<@{self.player.id}> The `unique id` is incorrect."))
                return
            
            else:  # if valid

                if character_id in player_team_id:  # check if the unique is in the team
                    await ctx.send(_(f"<@{self.player.id}> This character is already in your team."))
                    return

                print(character_id)
                character_ = await Character_from_unique(self.client, ctx, self.player, character_id)

                # the player cannot have the same character instance more than one time
                if character_.id in player_team_global:
                    await ctx.send(_(f"<@{self.player.id}> An identical character is already in your team."))
                    return

                update = f"UPDATE player_combat_info SET {fighter_slot} = '{character_id}' WHERE player_id = {self.player.id};"

                await self.db.execute(update)

                await ctx.send(_(f"<@{self.player.id}> The character {character_.icon}__{character_.name}__ lv.{character_.level} | {character_.type_icon} | {character_.rarity_icon} has been set as `{slot_name}``."))

        return
    
    async def get_team(self, ctx, str_list = False):
        '''
        `coroutine`

        Get the player's team.

        `str_list`[Optional] : type `bool` default set to `False`. If true, return a list a str object instead of character instance.

        Return: list[Character()], return list of character() instances.
        list : [a, b, c]
        '''

        # init 
        player_team = []
        
        fighter_a, fighter_b, fighter_c = None, None, None

        # fetching

        fighter_a = await self.db.fetchval(f"SELECT player_fighter_a FROM player_combat_info WHERE player_id = {self.player.id};")
        fighter_b = await self.db.fetchval(f"SELECT player_fighter_b FROM player_combat_info WHERE player_id = {self.player.id};")
        fighter_c = await self.db.fetchval(f"SELECT player_fighter_c FROM player_combat_info WHERE player_id = {self.player.id};")

        if str_list:  # return a list of str
            player_team = [fighter_a, fighter_b, fighter_c]

            return(player_team)
        
        else:  # return char instance
            # We append the list only if the fighter is defined
            # the player could define his own team lenght

            if fighter_a != "NONE":
                fighter_a = await Character_from_unique(self.client, ctx, self.player, fighter_a)
                player_team.append(fighter_a)

            if fighter_b != "NONE":
                fighter_b = await Character_from_unique(self.client, ctx, self.player, fighter_b)
                player_team.append(fighter_b)

            if fighter_c != "NONE":
                fighter_c = await Character_from_unique(self.client, ctx, self.player, fighter_c)
                player_team.append(fighter_c)
        
        return(player_team)
    
    async def display_team(self, ctx):
        '''
        `coroutine`

        Display the player's team in the channel.
        '''

        # init 

        _ = await Translate(self.client, ctx)
        team_display = Basic_embed(self.client, title = _(f"{self.player.name}'s team."), thumb = self.player.avatar)
        average_level, average_rarity = 0, 0

        player_team = await self.get_team(ctx)
        
        # set up the display
        # get the average
        for character in player_team:
            await asyncio.sleep(0)

            average_level += character.level
            average_rarity += character.rarity_value
        
        if(len(player_team) > 0):  # cannot divide by 0
            average_level = int(average_level/len(player_team))
            average_rarity = int(average_rarity/len(player_team))
        
        # get the icons
        average_rarity = await Get_rarity_icon(average_rarity)

        fighter_a, fighter_b, fighter_c = "--", "--", "--"

        if(len(player_team) > 0):  # if the team is not empty
            if(len(player_team) >= 1):
                fighter_a = player_team[0]
                fighter_a = _(f"{fighter_a.icon}{fighter_a.name} lv.{fighter_a.level} | {fighter_a.type_icon} | {fighter_a.rarity_icon}")
            
            if(len(player_team) >= 2):
                fighter_b = player_team[1]
                fighter_b = _(f"{fighter_b.icon}{fighter_b.name} lv.{fighter_b.level} | {fighter_b.type_icon} | {fighter_b.rarity_icon}")
            
            if(len(player_team) >= 3):
                fighter_c = player_team[2]
                fighter_c = _(f"{fighter_c.icon}{fighter_c.name} lv.{fighter_c.level} | {fighter_c.type_icon} | {fighter_c.rarity_icon}")
        
        # set up the displaying
        display_info = _(f"Average level : {average_level}\nAverage rarity : {average_rarity}")

        display_character = _(f"👑 - Leader : {fighter_a}\nFighter B : {fighter_b}\nFighter C : {fighter_c}")
        
        # send the embed

        team_display.add_field(name = _("Informations"), value = display_info, inline = False)
        team_display.add_field(name = _("Fighters"), value = display_character, inline = False)

        await ctx.send(embed = team_display)
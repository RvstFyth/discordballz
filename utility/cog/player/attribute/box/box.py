"""
Manages the box behaviour.

--

Author : DrLarck

Last update : 29/08/19 (DrLarck)
"""

# dependancies
import asyncio

# check
from utility.command.checker.box import Box_checker

# util
from utility.database.database_manager import Database
from utility.cog.character.getter import Character_getter
from utility.graphic.embed import Custom_embed

# box manager
class Box:
    """
    Manages the player's box.

    - Parameter :

    `ctx` : Represents the `commands.Context`.

    `client` : Represents a `discord.Client`. The client must handle a database connection pool (i.e Database().init())

    `player` : Represents a `Player` (Player instance or discord.Member)

    - Method :

    :coro:`manager(character_id : None)` : Manages the box display, the page switching etc.

    :coro:`wait_for_reaction(displayer, player, possible_reactions)` : Get the player's reaction for the box.

    :coro:`add_button(displayer, current_page, total_pages)` : Add the buttons according to the box logic.

    :coro:`display_box(page : 1, data : None, character_id : None)` : Display the box. If a character_id is passed, display the unique characters.

    :coro:`display_box(page, data)` : Display the player's box.

    :coro:`get_data(id)` : Get the data used for the unique display.
    """

    # attribute
    def __init__(self, ctx, client, player):
        # basics
        self.client = client
        self.ctx = ctx
        self.player = player
        self.db = Database(self.client.db)
    
    # method
    async def manager(self, character_id = None):
        """
        `coroutine`

        Manages the box by changing the page, closing, etc.

        - Parameter :

        `character_id` : int - Represents the character id to display

        --

        Return : None
        """

        # init
        displayer, total_pages, current_page, data = None, 0, 1, None
        Box_checker.opened_box.append(self.player.id)

        while current_page > 0:  # set the current_page to 0 to stop
            await asyncio.sleep(0)
            
            # display the box
            displayer, total_pages, current_page, data = await self.display_box(current_page, data, character_id = character_id)

            # add buttons
            added_reaction = await self.add_button(displayer, current_page, total_pages)

            # wait for a reaction
            reaction = await self.wait_for_reaction(displayer, self.player, added_reaction)

            await displayer.delete()

            if(reaction == None):  # in this case, the player didn't react in time
                await self.ctx.send(f"<@{self.player.id}> Closing the box.", delete_after = 20)
                current_page = 0
                break
            
            if(reaction == "❌"):
                current_page = 0        
            
            if(reaction == "⏮"):
                current_page = 1
            
            if(reaction == "⏭"):
                current_page = total_pages
            
            if(reaction == "▶"):
                current_page += 1
            
            if(reaction == "◀"):
                current_page -= 1
        
        # remove the player from the checker
        Box_checker.opened_box.remove(self.player.id)
        
        return(data)
    
    async def wait_for_reaction(self, displayer, player, possible_reactions):
        """
        `coroutine`

        Wait for a reaction to be added onto the box message.

        --

        Return : the added reaction as str(`discord.Emoji`).
        """
        
        # init
        added_reaction = None
        def box_predicate(reaction, user):
            check = False
            if(reaction.message.id == displayer.id):
                if(user.id == player.id):
                    if str(reaction.emoji) in possible_reactions:
                        check = True

            return(check)
        
        # get the reaction
        try:
            reaction, user = await self.client.wait_for(
                "reaction_add",
                timeout = 120,
                check = box_predicate
            )
        
        except asyncio.TimeoutError:
            return(added_reaction)
        
        else:
            return(str(reaction.emoji))

        return

    async def add_button(self, box, current_page, total_pages):
        """
        `coroutine`

        Add the button to switch the pages onto the box message.

        - Parameter : 

        `box` : discord.Message - Represents the discord.Message to add the reactions to.

        `current_page` : int - Represents the page that is currently displayed.

        `total_pages` : int - Represents the max number of pages.

        --

        Return : list of added reactions
        """

        # int
        added_reaction = []
        reactions = {
            "close" : "❌",
            "beginning" : "⏮",
            "end" : "⏭",
            "next" : "▶",
            "previous" : "◀"
        }
        
        # add reactions
        await box.add_reaction(reactions["close"])
        added_reaction.append(reactions["close"])

        if(current_page == 1):
            if(total_pages > current_page):
                await box.add_reaction(reactions["next"])
                added_reaction.append(reactions["next"])

                await box.add_reaction(reactions["end"])
                added_reaction.append(reactions["end"])
        
        elif(current_page > 1):
            await box.add_reaction(reactions["beginning"])
            added_reaction.append(reactions["beginning"])

            await box.add_reaction(reactions["previous"])
            added_reaction.append(reactions["previous"])

            if(total_pages > current_page):
                await box.add_reaction(reactions["next"])
                added_reaction.append(reactions["next"])

                await box.add_reaction(reactions["end"])
                added_reaction.append(reactions["end"])
        
        return(added_reaction)

    async def display_box(self, page = 1, data = None, character_id = None):
        """
        `coroutine`

        Displays the player's box

        - Parameter :

        `page` : int default 1 - The page to display.

        `data` : list default None - The data to use.

        `character_id` : int default None - Represent the charcter id to display

        --

        Return : box message, number of pages, current_page, data
        """

        # init
        box_display = ""

            # params
        total_pages = 1
        max_display = 5  # number of characters to display
        start_at = 0     # index of the character to display first
        end_at = 5       # idex of the character to display last  (= max_display + 1)
        getter = Character_getter()

        if(data == None):  # if no data provided, get the player's character
            if(character_id == None):  # if the display is not unique
                data = await self.db.fetch(
                f"""
                SELECT DISTINCT character_global_id FROM character_unique 
                WHERE character_owner_id = {self.player.id}
                ORDER BY character_global_id ASC;
                """
                )
            
            else:
                data = await self.db.fetch(
                    f"""
                    SELECT character_unique_id, character_type, character_rarity, character_level FROM character_unique
                    WHERE character_owner_id = {self.player.id} AND character_global_id = {character_id}
                    ORDER BY character_level DESC;
                    """
                )

        if(page > 1):
            start_at += (end_at) * (page - 1)  # display the character above the last one of the previous page
            end_at += max_display * (page - 1)

            # setup total pages
        total_pages = int(((len(data) - 1) / max_display) + 1)

        if(len(data) < end_at):  # if there is not enough character to display
            end_at = len(data)

        if(page > total_pages):
            await self.ctx.send(f"<@{self.player.id}> Sorry, this page doesn't exist.")
            Box_checker.opened_box.remove(self.player.id)
            return
        
        # start displaying
        waiting_message = await self.ctx.send(f"<@{self.player.id}> Displaying ...")

        for row in range(start_at, end_at):
            await asyncio.sleep(0)

            if(character_id == None):
                # retrieve the character
                character_id = data[row][0]
                character = await getter.get_character(character_id)
                await character.init()

                # get the character quantity
                character_quantity = len(await self.db.fetch(
                    f"""
                    SELECT character_global_id FROM character_unique
                    WHERE character_global_id = {character.info.id} AND character_owner_id = {self.player.id};
                    """
                ))

                # add line to the box
                box_display += f"#`{character.info.id}` - {character.image.icon}__{character.info.name}__ : *x{character_quantity}*\n"

            else:  # character unique
                # retrieve the character
                character = await getter.get_character(character_id)

                # setup the character
                unique_id = data[row][0]
                character.type.value = data[row][1]
                character.rarity.value = data[row][2]
                character.level = data[row][3]
                await character.init()

                # add line to the box
                box_display += f"{row + 1} - `{unique_id}` - {character.image.icon}__{character.info.name}__ {character.type.icon}{character.rarity.icon} - lv.{character.level}\n"
        
        # check if there is something to display
        if(box_display == ""):
            box_display = "DISPLAY ERROR"

        # setup the embed 
        embed = await Custom_embed(self.client).setup_embed()
        embed.set_thumbnail(url = self.player.avatar)
        embed.add_field(
            name = f"{self.player.name}'s box | Page : {page:,} / {total_pages:,}",
            value = box_display,
            inline = False
        )

        # sending
        await waiting_message.delete()
        box = await self.ctx.send(embed = embed)

        return(box, total_pages, page, data)
    
    async def get_data(self, character_id):
        """
        `coroutine`

        Get the data used for the box.

        --

        Return : list
        """

        data = await self.db.fetch(
            f"""
            SELECT character_unique_id, character_type, character_rarity, character_level FROM character_unique
            WHERE character_owner_id = {self.player.id} AND character_global_id = {character_id}
            ORDER BY character_level DESC;
            """
        )

        return(data)
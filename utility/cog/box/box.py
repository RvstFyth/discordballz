"""
Manages the box behaviour.

--

Author : DrLarck

Last update : 28/08/19 (DrLarck)
"""

# dependancies
import asyncio

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

    :coro:`display_box(page, data)` : Display the player's box.
    """

    # attribute
    def __init__(self, ctx, client, player):
        # basics
        self.client = client
        self.ctx = ctx
        self.player = player
        self.db = Database(self.client.db)
    
    # method
    async def manager(self):
        """
        `coroutine`

        Manages the box by changing the page, closing, etc.

        --

        Return : None
        """

        
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

    async def display_box(self, page = 1, data = None):
        """
        `coroutine`

        Displays the player's box

        - Parameter :

        `page` : int default 1 - The page to display.

        `data` : list default None - The data to use.

        --

        Return : box message, number of pages, current_page, data
        """

        # init
        box_display = ""

            # params
        total_pages = 1
        max_display = 5  # number of characters to display
        start_at = 0     # index of the character to display first
        end_at = 6       # idex of the character to display last  (= max_display + 1)
        getter = Character_getter()

        if(data == None):  # if no data provided, get the player's character
            data = await self.db.fetch(
            f"""
            SELECT DISTINCT character_global_id FROM character_unique 
            WHERE character_owner_id = {self.player.id}
            ORDER BY character_global_id ASC;
            """
            )

        if(page > 1):
            start_at += (end_at + 1) * page - 1  # display the character above the last one of the previous page
            end_at += max_display * page - 1

            # setup total pages
        total_pages = int(((len(data) - 1) / 8) + 1)

        if(len(data) < end_at):  # if there is not enough character to display
            end_at = len(data)

        if(page > total_pages):
            await self.ctx.send(f"<@{self.player.id}> Sorry, this page doesn't exist.")
            return
        
        # start displaying
        waiting_message = await self.ctx.send(f"<@{self.player.id}> Displaying ...")

        for row in range(start_at, end_at):
            await asyncio.sleep(0)

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
            box_display += f"#{character.info.id} - {character.image.icon}__{character.info.name}__ : *x{character_quantity}*\n"
        
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
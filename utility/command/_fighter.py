"""
Here are the fighter command utils

--

Author : DrLarck

Last update : 24/09/19 (DrLarck)
"""

# dependancies
import asyncio

# utils
from utility.cog.player.player import Player
from utility.cog.character.getter import Character_getter
from utility.database.database_manager import Database

# tools
class Fighter:
    """
    Add utils method to help the fighter command work properly.

    - Parameter :

    `ctx` : Represents the `commands.Context`.

    `client` : Represents a `discord.Client`. The client must handle a connection pool to the database.

    `player` : Represents a `Player`.

    - Method :

    :coro:`wait_for_fighter_index(data)` : Return the fighter's unique id.
    """
    
    # attribute
    def __init__(self, ctx, client, player):
        # basic
        self.ctx = ctx
        self.client = client
        self.player = player
        self.getter = Character_getter()
    
    # method
    async def fighter_command(self, slot, character_id):
        """
        Allow the player to select the fighter to set

        `character_id` : int - Represents the character to display
        """

        # init
        player = Player(self.ctx, self.client, self.ctx.message.author)
        tool = Fighter(self.ctx, self.client, player)

        # if a global id is passed
        if(character_id.isdigit()):
            box_data = await player.box.get_data(character_id)
            character_id = int(character_id)
            
            # ask the player to pick the id of his character
            explanation = await self.ctx.send(f"<@{player.id}> Please select a fighter among the following.\n**Close the box** (`❌`) once you have chosen your character, then, **type its index** number :")

            # display the available characters
            await player.box.manager(character_id)

            # ask for choice
            unique_id = await tool.wait_for_fighter_index(box_data)
            if(unique_id == None):
                await self.ctx.send(f"<@{player.id}> Error : character not found.")
                return

            character = await self.getter.get_from_unique(self.client, unique_id)
            await character.init()

            # set the fighter
            possible = await player.team.set_fighter(slot, unique_id)

            if(possible == False):  # the character is already in the team
                await self.ctx.send(f"<@{player.id}> You already have a {character.image.icon}**{character.info.name}** in your team. **Remove** it or choose a different character.")
            
            else:
                # confirm
                await self.ctx.send(f"<@{player.id}> You have successfully set {character.image.icon}**{character.info.name}** {character.type.icon}{character.rarity.icon} lv.{character.level:,} as **fighter {slot.upper()}** !")
            
            await explanation.delete()
        
        else:  # if the character_id is a unique id
            db = Database(self.client.db)
            # check if the player has the character
            owns_character = await db.fetchval(f"SELECT character_owner_name FROM character_unique WHERE character_unique_id = '{character_id}' AND character_owner_id = {player.id};")
            print(f"Owns character : {owns_character}")

            if(owns_character != None):
                character = await self.getter.get_from_unique(self.client, character_id)

                if(character == None):
                    await self.ctx.send(f"<@{player.id}> Character with unique id \"{character_id}\" not found. Please try with another id.\nYou can find your character's unique id by using `d!box [character id]`. The **unique id** format is `aaaa0`.")
                
                else:  # the character has been found
                    await character.init()

                    # set the fighter
                    possible = await player.team.set_fighter(slot, character_id)

                    if(possible == False):  # the character is already in the team
                        await self.ctx.send(f"<@{player.id}> You already have a {character.image.icon}**{character.info.name}** in your team. **Remove** it or choose a different character.")
                
                    else:
                        # confirm
                        await self.ctx.send(f"<@{player.id}> You have successfully set {character.image.icon}**{character.info.name}** {character.type.icon}{character.rarity.icon} lv.{character.level:,} as **fighter {slot.upper()}** !")
                
            else:  # doesn't own the character
                await self.ctx.send(f"<@{player.id}> Character `{character_id}` not found.")
                return

    async def wait_for_fighter_index(self, data):
        """
        `coroutine`

        Return the fighter unique id.

        - Parameter :

        `data` : Must be a list of data from the box.
        --

        Return : str, None if not found
        """

        # init 
        def fighter_predicate(message):
            success = False
            choice = 0
            
            if(message.author.id == self.player.id):
                if(message.channel.id == self.ctx.message.channel.id):  # the message should come from the same channel as the command
                    if((message.content).isdigit()):  # it must be a digit
                        choice = int(message.content)
                        if(choice >= 0 and choice <= len(data) - 1):  # if it's >= 0 and inferior to the len of data
                            success = True

            return(success)
        
        # get the choice
        try:
            message = await self.client.wait_for(
                "message",
                timeout = 120,
                check = fighter_predicate
            )
        
        except asyncio.TimeoutError:
            return(None)
        
        else:
            character_id = data[int(message.content) - 1][0]
            
            return(character_id)
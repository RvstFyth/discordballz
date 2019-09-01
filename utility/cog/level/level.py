"""
Manager the levelling

--

Author : DrLarck

Last update : 01/09/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.database.database_manager import Database
from utility.cog.character.getter import Character_getter

# leveller
class Leveller:
    """
    Manages the way the character and player level up.

    - Parameter :

    `client` : Represents a `discord.Client`. The client must handle a database connection pool.

    `ctx` : Represents the `commands.Context`.

    - Method :

    :coro:`character_levelling(player, unique_character, xp)` : Check if the character levels up or not.

    :coro:`player_levelling(player, xp)` : Same as `character_levelling()` but for players.
    """
    
    # attribute
    def __init__(self, client, ctx):
        # basic
        self.client = client
        self.ctx = ctx
        self.db = Database(self.client.db)
        self.getter = Character_getter()

    # method
    async def character_levelling(self, player, unique_character, xp):
        """
        `coroutine`

        Make the character levelling up.

        - Parameter :

        `player` : The player who is affected.

        `unique_character` : The character to level up

        `xp` : The amount of xp gained by the character

        --

        Return : send a message in the channel if the character is levelling up, otherwise None
        """

        # init
            # character
        character = await self.getter.get_from_unique(self.client, unique_character)
        await character.init()

        level = character.level

        # get the xp infos
        character_xp = int(await self.db.fetchval(
            f"SELECT character_xp FROM character_unique WHERE character_unique_id = {unique_character};")
        )

        character_xp += xp
        
        await self.db.execute(
            f"""
            UPDATE character_unique SET character_xp = {character_xp}
            WHERE character_unique_id = {unique_character};
            """
        )

        # sum the necessary xp + total exp to retrieve the nedded amount
        next_level = int((100 + (50 * level)) + ((level - 1) * (100 + (50 * level - 1))))

        # levelling it up
        while character_xp > next_level:
            await asyncio.sleep(0)

            # increase the level value
            level += 1

            # just get the new exp value after levelling
            next_level = int((100 + (50 * level)) + ((level - 1) * (100 + (50 * level - 1))))
        
        # if the level has changed
        if(level > character.level):
            # set the level
            await self.db.execute(
                f"""
                UPDATE character_unique SET character_level = {level}
                WHERE character_unique_id = {unique_character};
                """
            )

            await self.ctx.send(f"<@{player.id}> Your character {character.image.icon}**{character.info.name}** {character.type.icon}{character.rarity.value} has reached the level **{level:,}** :star: by earning *{xp:,}* as **XP** !")

        return
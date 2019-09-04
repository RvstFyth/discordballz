"""
Manager the levelling

--

Author : DrLarck

Last update : 04/09/19 (DrLarck)
"""

# dependancies
import asyncio
from random import randint

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
            # level per rarity
        max_level = {
            "0" : 20,
            "1" : 40,
            "2" : 60,
            "3" : 80,
            "4" : 120,
            "5" : 150
        }

            # character
        character = await self.getter.get_from_unique(self.client, unique_character)
        await character.init()

        level = character.level

        # get the xp infos
        character_xp = int(await self.db.fetchval(
            f"SELECT character_experience FROM character_unique WHERE character_unique_id = '{unique_character}';")
        )

        # check if the character's level is equal to its rarity or inferior
        if(character.level < max_level[f"{character.rarity.value}"]):
            character_xp += xp
            
            await self.db.execute(
                f"""
                UPDATE character_unique SET character_experience = {character_xp}
                WHERE character_unique_id = '{unique_character}';
                """
            )

            # sum the necessary xp + total exp to retrieve the nedded amount
            next_level = int((100 + (50 * level)) + ((level - 1) * (100 + (50 * level - 1))))

            # levelling it up
            while character_xp > next_level:
                await asyncio.sleep(0)

                # avoid the character to reach a too high level for its rarity
                if(level < max_level[f"{character.rarity.value}"]):
                    # increase the level value
                    level += 1

                    # just get the new exp value after levelling
                    next_level = int((100 + (50 * level)) + ((level - 1) * (100 + (50 * level - 1))))
                
                else:
                    break
            
            # if the level has changed
            if(level > character.level):
                # set the level
                await self.db.execute(
                    f"""
                    UPDATE character_unique SET character_level = {level}
                    WHERE character_unique_id = '{unique_character}';
                    """
                )

                return(f"Your character {character.image.icon}**{character.info.name}** {character.type.icon}{character.rarity.icon} has reached the level **{level:,}** :star: by earning *{xp:,}* as **XP** !")

            else:  # just xp gain
                return(f"Your character {character.image.icon}**{character.info.name}** {character.type.icon}{character.rarity.icon} has gained *{xp:,}* as **XP** !")

        return
    
    async def team_add_xp(self, player, team, xp):
        """
        `coroutine`

        Add the `xp` amount to the characters that are contained in `team`, then display a message.

        - Parameter :

        `player` : Represents the `team` owner.

        `team` : list - Represents the player's team. Contains characters' `unique id`.

        `xp` : int - The amount of xp gained by the team.

        --

        Return : Send a message.
        """

        # init
        displaying = f"<@{player.id}> "

        for character in team:
            await asyncio.sleep(0)

            if(character != None):
                xp = randint(int((0.9 * xp)), int((1.1 * xp)))  # rng xp
                future_display = await self.character_levelling(player, character, xp)

                if(future_display != None):
                    displaying += future_display
                    displaying += "\n"
        
        if(displaying != f"<@{player.id}> "):
            await self.ctx.send(displaying)
        
        else:
            return
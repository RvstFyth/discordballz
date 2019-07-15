"""
Manages the displaying of the characters.

--

Author : DrLarck

Last update : 15/07/19
"""

# dependancies
import asyncio

# utils
    # translation
from utility.translation.translator import Translator

    # embed
from utility.graphic.embed import Custom_embed

# displayer class
class Character_displayer:
    """
    Manages the displaying of character informations, teams, etc.

    - Parameter :

    `character` : Represents a `list` of :class:`Character()` objects.

    - Attribute : 

    - Method :

    :coro:`display(combat_format`[Optional]`)` : Displays the characters in `character` list.
    `combat_format`[bool] represents the format of the displaying. 
    """

    # attribute
    def __init__(self, client, ctx, player):
        # bot
        self.client = client
        self.player = player
        self.ctx = ctx

        # class
        self.character = []
    
    # method
    async def display(self, combat_format = False):
        """
        `coroutine`

        Displays the characters in `character` list.

        --

        Return : discord.Message (embedded)
        """

        # init
        translation = Translator(self.client.db, self.player)
        #_ = await translation.translate()

        if(combat_format):
            # posture icons
            posture_icon = [":crossed_swords:", ":fire:", ":shield:", ":confused:"]

            for character in self.character:
                await asyncio.sleep(0)

                # embed
                embed = Custom_embed(
                    self.client,
                    thumb = character.info['thumb']
                )

                embed = await embed.setup_embed()

                # posture
                posture = None

                if(character.posture["attacking"] == True):
                    posture = posture_icon[0]
                
                if(character.posture["charging"] == True):
                    posture = posture_icon[1]

                if(character.posture["defending"] == True):
                    posture = posture_icon[2]
                
                if(character.posture["stunned"] == True):
                    posture = posture_icon[3]
                
                # formatting the embed
                combat_format = f"__Name__ : **{character.info['name']}**\n"
                combat_format += f"__Health__ : **{character.health['current']:,}** / **{character.health['maximum']:,} :hearts: \n"
                combat_format += f"__Ki__ : **{character.ki['current']:,} :fire: \n"
                combat_format += f"__Posture__ : {posture}\n"
                combat_format += f"__Damage__ :\n:crossed_swords: **{character.damage['physical']['minimum']}** - **{character.damage['physical']['maximum']}** \n:rosette: **{character.damage['ki']['minimum']}** - **{character.damage['ki']['maximum']}** \n"
                combat_format += f"__Defense__ :\n:shield: **{character.defense['armor']}\n:rosette: **{character.defense['spirit']}\n"

                # now the effects
                    # buff
                if(len(character.effect["bonus"]) > 0):  # if the character has a buff
                    combat_format += f"__Bonus__ : "

                    for buff in character.effect["buff"]:
                        await asyncio.sleep(0)

                        combat_format += f"{buff.icon} x{buff.stack} ({buff.duration}) |"
                
                if(len(character.effect["malus"]) > 0):
                    combat_format += f"\n__Malus__ : "
                    
                    for debuff in character.effect["malus"]:
                        await asyncio.sleep(0)

                        combat_format += f"{debuff.icon} x{debuff.stac} ({debuff.duration}) |"
                
                # send the messages
                embed.add_field(name = f"{character.info['icon']}{character.info['name']}'s infos :", value = combat_format)

                await self.ctx.send(embed = embed)

        else:
            pass
        
        return


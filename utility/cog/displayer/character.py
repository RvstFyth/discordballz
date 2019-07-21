"""
Manages the displaying of the characters.

--

Author : DrLarck

Last update : 20/07/19
"""

# dependancies
import asyncio

# icons
from configuration.icon import game_icon

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
        self.character = None
    
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

            # embed
            embed = Custom_embed(
                self.client,
                thumb = self.character.image.thumb
            )

            embed = await embed.setup_embed()

            # posture
            posture = None

            if(self.character.posture.attacking == True):
                posture = posture_icon[0]
            
            if(self.character.posture.charging == True):
                posture = posture_icon[1]

            if(self.character.posture.defending == True):
                posture = posture_icon[2]
            
            if(self.character.posture.stunned == True):
                posture = posture_icon[3]
            
            # formatting the embed
            combat_format = f"__Name__ : **{self.character.info.name}**{self.character.type.icon}\n"
            combat_format += f"__Health__ : \n**{self.character.health.current:,}** / **{self.character.health.maximum}** :hearts: \n"
            combat_format += f"__Posture__ : {posture}\n"
            combat_format += f"__Damage__ :\n:crossed_swords: **{self.character.damage.physical_min}** - **{self.character.damage.physical_max}** \n{game_icon['ki_ability']} **{self.character.damage.ki_min}** - **{self.character.damage.ki_max}** \n"
            combat_format += f"__Defense__ :\n:shield: **{self.character.defense.armor}**\n:rosette: **{self.character.defense.spirit}**\n"
            combat_format += f"__Ki__ : **{self.character.ki.current}** :fire:"

            # now the effects
                # buff
            if(len(self.character.bonus) > 0):  # if the character has a buff
                combat_format += f"__Bonus__ : "

                for buff in self.character.bonus:
                    await asyncio.sleep(0)

                    combat_format += f"{buff.icon} x{buff.stack} ({buff.duration}) |"
            
            if(len(self.character.malus) > 0):
                combat_format += f"\n__Malus__ : "
                
                for debuff in self.character.malus:
                    await asyncio.sleep(0)

                    combat_format += f"{debuff.icon} x{debuff.stac} ({debuff.duration}) |"
            
            # send the messages
            embed.add_field(name = f"{self.character.image.icon}{self.character.info.name}'s infos :", value = combat_format)

            await self.ctx.send(embed = embed)

        else:  # if not in combat format
            pass
        
        return
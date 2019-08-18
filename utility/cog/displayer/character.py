"""
Manages the displaying of the characters.

--

Author : DrLarck

Last update : 16/08/19 (DrLarck)
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
    async def display(self,  basic_format = False, combat_format = False, team_format = False, index = 0):
        """
        `coroutine`

        Displays the characters in `character` list.

        --

        Return : discord.Message (embedded)
        """

        # init
        translation = Translator(self.client.db, self.player)
        #_ = await translation.translate()
        posture_icon = [":crossed_swords:", ":fire:", ":shield:", ":confused:"]
            # embed
        embed = Custom_embed(
            self.client,
            thumb = self.character.image.thumb
        )

        if(index == 0):
            index = ""
        
        embed = await embed.setup_embed()

        ## TEAM FORMAT ##
        if(team_format):
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
            
            team_format = f"__Level__ : **{self.character.level:,}**{self.character.rarity.icon}\n"
            team_format += f"__Health__ : \n**{self.character.health.current:,}** / **{self.character.health.maximum:,}** :hearts:\n"
            team_format += f"__Posture__ : {posture}\n"
            
            # display bonus and malus
            if(len(self.character.bonus) > 0):
                team_format += f"__Bonus__ : "

                for bonus in self.character.bonus:
                    await asyncio.sleep(0)

                    team_format += f"{bonus.icon} ({bonus.stack}|{bonus.duration}) "
            
            if(len(self.character.malus) > 0):
                team_format += f"__Malus__ : "

                for malus in self.character.malus:
                    await asyncio.sleep(0)

                    team_format += f"{malus.icon} ({malus.stack}|{malus.duration}) "
            
            embed.add_field(
                name = f"#{index} - {self.character.image.icon}{self.character.info.name}{self.character.type.icon}",
                value = team_format
            )

            await self.ctx.send(embed = embed)

        ## COMBAT FORMAT ## 
        if(combat_format):
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
            combat_format = f"__Health__ : \n**{self.character.health.current:,}** / **{self.character.health.maximum}** :hearts: \n"
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

                    combat_format += f"{debuff.icon} x{debuff.stack} ({debuff.duration}) |"
            
            # send the messages
            embed.add_field(name = f"{self.character.image.icon}{self.character.info.name}'s infos :", value = combat_format)

            await self.ctx.send(embed = embed)
        
        return
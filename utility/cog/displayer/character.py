"""
Manages the displaying of the characters.

--

Author : DrLarck

Last update : 12/09/19 (DrLarck)
"""

# dependancies
import asyncio

# icons
from configuration.icon import game_icon
from configuration.color import game_color

# utils
    # translation
from utility.translation.translator import Translator

    # embed
from utility.graphic.embed import Custom_embed

from utility.cog.displayer.color import Color_displayer

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
    async def display(self, summon_format = False, basic_format = False, combat_format = False, team_format = False, index = 0):
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

        ## SUMMON FORMAT ##
        if(summon_format):
            summon_format = f"__Name__ : {self.character.image.icon}*{self.character.info.name}* {self.character.type.icon} {self.character.rarity.icon} `#{self.character.info.id}`\n"
            summon_format += f"__Expansion__ : *{self.character.info.expansion}*{self.character.image.expansion}\n"
            summon_format += f"__Saga__ : *{self.character.info.saga}*\n"
            summon_format += f"__Damage__ :\n:crossed_swords: **{self.character.damage.physical_min:,}** - **{self.character.damage.physical_max:,}** \n{game_icon['ki_ability']} **{self.character.damage.ki_min:,}** - **{self.character.damage.ki_max:,}** \n"
            summon_format += f"__Defense__ :\n:shield: **{self.character.defense.armor:,}**\n:rosette: **{self.character.defense.spirit:,}**\n"
            summon_format += f"__Abilities__ :\n"
            # get the abilities
            ability_index = 1
            if(len(self.character.ability) > 0):
                for ability in self.character.ability:
                    await asyncio.sleep(0)

                    ability = ability(
                        None, None, None,
                        None, None, None
                    )
                    
                    if(ability_index == 1):
                        summon_format += f"`{ability_index}. {ability.name}`{ability.icon}"
                    
                    else:
                        summon_format += f" | `{ability_index}. {ability.name}`{ability.icon}"

                    ability_index += 1
            
            else:  # no ability
                summon_format += "--"
            
            # set the image
            embed = Custom_embed(
                self.client,
                thumb = self.player.avatar,
                colour = await Color_displayer().get_rarity_color(self.character.rarity.value)
            )

            # setup the embed
            embed = await embed.setup_embed()

            # config the embed
            embed.set_image(url = self.character.image.image)
            embed.add_field(
                name = f"{self.player.name}'s summon",
                value = summon_format,
                inline = False
            )

            await self.ctx.send(embed = embed)

        ## TEAM FORMAT ##
        elif(team_format):
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

                    if(bonus.is_permanent):
                        team_format += f"{bonus.icon} ({bonus.stack}|*∞*) "

                    else:    
                        team_format += f"{bonus.icon} ({bonus.stack}|{bonus.duration}) "
            
            if(len(self.character.malus) > 0):
                team_format += f"__Malus__ : "

                for malus in self.character.malus:
                    await asyncio.sleep(0)

                    if(malus.is_permanent):
                        team_format += f"{malus.icon} ({malus.stack}|*∞*) "

                    else:
                        team_format += f"{malus.icon} ({malus.stack}|{malus.duration}) "
            
            embed.add_field(
                name = f"#{index} - {self.character.image.icon}{self.character.info.name}{self.character.type.icon}",
                value = team_format
            )

            await self.ctx.send(embed = embed)

        ## COMBAT FORMAT ## 
        elif(combat_format):
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
            combat_format = f"__Health__ : \n**{self.character.health.current:,}** / **{self.character.health.maximum:,}** :hearts: \n"
            combat_format += f"__Posture__ : {posture}\n"
            combat_format += f"__Damage__ :\n:crossed_swords: **{self.character.damage.physical_min:,}** - **{self.character.damage.physical_max:,}** \n{game_icon['ki_ability']} **{self.character.damage.ki_min:,}** - **{self.character.damage.ki_max:,}** \n"
            combat_format += f"__Defense__ :\n:shield: **{self.character.defense.armor:,}**\n:rosette: **{self.character.defense.spirit:,}**\n"
            combat_format += f"__Ki__ : **{self.character.ki.current}** :fire:"

            # now the effects
                # buff
            if(len(self.character.bonus) > 0):  # if the character has a buff
                combat_format += f"\n__Bonus__ : "

                for buff in self.character.bonus:
                    await asyncio.sleep(0)

                    if(buff.is_permanent):
                        combat_format += f"{buff.icon}[{buff.stack}|*∞*]"    
                    
                    else:
                        combat_format += f"{buff.icon}[{buff.stack}|{buff.duration}]"
            
            if(len(self.character.malus) > 0):
                combat_format += f"\n__Malus__ : "
                
                for debuff in self.character.malus:
                    await asyncio.sleep(0)

                    combat_format += f"{debuff.icon}[{debuff.stack}|{debuff.duration}]"
            
            # send the messages
            embed.add_field(name = f"{self.character.image.icon}{self.character.info.name} {self.character.type.icon}{self.character.rarity.icon}'s infos :", value = combat_format)

            await self.ctx.send(embed = embed)
        
        return
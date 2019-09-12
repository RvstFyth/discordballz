"""
Manages the trigger phase.

--

Author : DrLarck

Last update : 12/09/19 (DrLarck)
"""

# dependancies
import asyncio
from random import randint

# util
from utility.cog.character.getter import Character_getter

# trigger phase manager
class Trigger_phase:
    """
    Manages the trigger phase.

    - Parameter :

    `team_a` : Represents the ally team

    `team_b` : Represents the opponent team

    - Method :

    :coro:`trigger_effect()` : Triggers all the active effects.

    :coro:`trigger_passive()` : Triggers all the character's passive effects.
    """

    # attribute
    def __init__(self, team_a, team_b):
        self.team_a = team_a
        self.team_b = team_b

    # method
    async def trigger_effect(self, ctx, character_index, character):
        """
        `coroutine`
        
        Triggers all the active effects.

        - Parameter :

        `ctx` : Current `commands.Context`.

        `character_index` : Represents the character's index number.

        `character` : Represents a `Character()`.

        --

        Return : None
        """

        # init
            # reference character
        character_getter = Character_getter()
        character_ref = await character_getter.get_character(character.info.id)
        await character_ref.init()

        health_change = character.health.current  # allow us to check the health change
        # check if its the first character of its team
        if(character_index == 1 or len(self.team_a) == 1):
            displaying = ""
        
        else:
            displaying = "```\n```"

        displaying += f"{character.image.icon} **{character.info.name}**{character.type.icon} :\n"
        effect = {
            "bonus" : "",
            "malus" : ""
        }
        send = False

        # trigger the effects
        if(character.health.current > 0):  # need the character to be alive
            # bonus
            if(len(character.bonus) > 0):
                for bonus in character.bonus:
                    await asyncio.sleep(0)

                    if(bonus.duration > 0):  # check if the bonus is still active
                        await bonus.apply()

                        if(bonus.is_permanent == False):
                            bonus.duration -= 1
                            effect["bonus"] += f"{bonus.icon}[{bonus.stack}|{bonus.duration}] "
                        
                        else:  # if the bonus is permanent 
                            effect["bonus"] += f"{bonus.icon}[{bonus.stack}|*∞*] "
                    
                    else:
                        character.bonus.remove(bonus)
                        await bonus.on_remove()  # activate the on_remove event of the effect
        
            # malus
            if(len(character.malus) > 0):
                for malus in character.malus:
                    await asyncio.sleep(0)

                    if(malus.duration > 0):
                        await malus.apply()

                        if(malus.is_permanent == False):
                            malus.duration -= 1
                            effect["malus"] += f"{malus.icon}[{malus.stack}|{malus.duration}] "
                        
                        else:
                            effect["malus"] += f"{malus.icon}[{malus.stack}|*∞*] "
                    
                    else:
                        character.malus.remove(malus)
                        await malus.on_remove()
        
        # displaying
            # health
        health_change = character.health.current - health_change  # check if there is health change
        if(health_change != 0):
            if(health_change > 0):
                displaying += f"__Health__ : +**{health_change:,}** :hearts:\n"
            
            else:
                displaying += f"__Health__ : **{health_change:,}** :hearts:\n"
            
            send = True
        
            # final
        if(effect["bonus"] != ""):
            displaying += f"__Bonus__ : {effect['bonus']}\n"
            send = True
        
        if(effect["malus"] != ""):
            displaying += f"__Malus__ : {effect['malus']}\n"
            send = True
        
        # regen
        # ki
        if(character.posture.attacking):
            character.ki.current += character.ki.regen + randint(1, 5)
            await character.ki.ki_limit()
        
        elif(character.posture.defending):
            character.ki.current += character.ki.regen
            await character.ki.ki_limit()
        
        else:  # if not attacking or defending, doesn't gain ki
            pass
        
            # displaying
            # only if the regen is different than the normal regen
        if(character.ki.regen != character_ref.ki.regen):
            if(character.ki.regen > 0):
                displaying += f"__Ki regen__ : +**{character.ki.regen:,}** :fire:\n"
            
            else:
                displaying += f"__Ki regen__ : **{character.ki.regen:,}** :fire:\n"

        # health
        character.health.current += character.health.regen

        # sending
        if(send):
            await ctx.send(displaying)

        return
    
    async def trigger_passive(self):
        """
        `coroutine`

        Triggers all the character's passive effects.

        --

        Return : None
        """

        return
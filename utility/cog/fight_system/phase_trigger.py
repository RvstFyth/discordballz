"""
Manages the trigger phase.

--

Author : DrLarck

Last update : 19/08/19 (DrLarck)
"""

# dependancies
import asyncio

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
    async def trigger_effect(self, ctx, character):
        """
        `coroutine`
        
        Triggers all the active effects.

        - Parameter :

        `ctx` : Current `commands.Context`.

        `character` : Represents a `Character()`.

        --

        Return : None
        """

        # init
        health_change = character.health.current  # allow us to check the health change
        displaying = f"```\n```{character.image.icon} **{character.info.name}**{character.type.icon} :\n"
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
                        bonus.duration -= 1

                        effect["bonus"] += f"{bonus.icon}({bonus.stack}|{bonus.duration}) "
                    
                    else:
                        character.bonus.remove(bonus)
                        await bonus.on_remove()  # activate the on_remove event of the effect
        
            # malus
            if(len(character.malus) > 0):
                for malus in character.malus:
                    await asyncio.sleep(0)

                    if(malus.duration > 0):
                        await malus.apply()
                        malus.duration -= 1

                        effect["malus"] += f"{malus.icon}({malus.stack}|{malus.duration}) "
                    
                    else:
                        character.malus.remove(malus)
                        await malus.on_remove()
        
        # displaying
            # health
        health_change = character.health.current - health_change  # check if there is health change
        print(f"change : {health_change}\nmalus : {len(character.malus)}")
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
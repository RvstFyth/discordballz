"""
Manages the trigger phase.

--

Author : DrLarck

Last update : 18/10/19 (DrLarck)
"""

# dependancies
import asyncio
from random import randint

# util
from utility.cog.character.getter import Character_getter

# graphic
from configuration.icon import game_icon

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

        # changment watcher
        health_change = character.health.current  # allow us to check the health change
        physical_change, ki_change = character.damage.physical_max, character.damage.ki_max
        armor_change, spirit_change = character.defense.armor, character.defense.spirit

        displaying = f"{character.image.icon} **{character.info.name}**{character.type.icon} :\n"
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
        
        # defense change
        armor_change = character.defense.armor - armor_change
        if(armor_change != 0):
            if(armor_change > 0):
                displaying += f"__Armor__ : +**{armor_change:,}** :shield:\n"
            
            else:
                displaying += f"__Armor__ : **{armor_change:,}** :shield:\n"
            
            send = True
        
        spirit_change = character.defense.spirit - spirit_change
        if(spirit_change != 0):
            if(spirit_change > 0):
                displaying += f"__Spirit__ : +**{spirit_change:,}** :rosette:\n"
            
            else:
                displaying += f"__Spirit__ : **{spirit_change:,}** :rosette:\n"
            
            send = True
        
        # damage change
        physical_change = character.damage.physical_max - physical_change
        if(physical_change != 0):
            if(physical_change > 0):
                displaying += f"__Physical damage__ : +**{physical_change:,}** :punch:\n"
            
            else:
                displaying += f"__Physical damage__ : **{physical_change:,}** :punch:\n"
            
            send = True
        
        ki_change = character.damage.ki_max - ki_change
        if(ki_change != 0):
            if(ki_change > 0):
                displaying += f"__Ki damage__ : +**{ki_change:,}** {game_icon['ki_ability']}\n"
            
            else:
                displaying += f"__Ki damage__ : **{ki_change:,}** {game_icon['ki_ability']}\n"
            
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
            displaying += "--\n"
            await ctx.send(displaying)

        return
    
    async def trigger_passive(self, client, ctx, character):
        """
        `coroutine`

        Triggers all the character's passive effects.

        - Parameter : 

        `ctx` : Represents the `commands.Context`.

        `character` : Represents a `Character()`.

        --

        Return : None
        """

        # first sort the passive
        new_passive = []
        if(character.passive_sorted == False):
            for passive in character.passive:
                await asyncio.sleep(0)

                passive = passive(
                    client,
                    ctx,
                    character,
                    self.team_a,
                    self.team_b
                )

                new_passive.append(passive)
            
            character.passive = new_passive
            character.passive_sorted = True

        # trigger all the passive if they've not been triggered 
        applied = False
        applied_list = []
        for _passive in character.passive:
            await asyncio.sleep(0)

            if not _passive.triggered :
                await _passive.apply()
            
                applied = True
                applied_list.append(_passive)
        
        # display the applied effect
        if(applied):
            displaying = f"{character.image.icon} **{character.info.name}**{character.type.icon} :\n"

            for passive_ in applied_list:
                await asyncio.sleep(0)

                displaying += f"• {passive_.icon}**__{passive_.name}__** : *{passive_.description}*"

            await ctx.send(displaying)
            await ctx.send("--")

        return
    
    async def trigger_leader(self, client, ctx, character_leader):
        """
        `coroutine`

        Trigger the leader skill of the passed character.

        --

        Return : None
        """

        # first sort the leader
        new_leader = []
        if(character_leader.leader_sorted == False):
            for leader in character_leader.leader:
                await asyncio.sleep(0)

                leader = leader(
                    client,
                    ctx,
                    character_leader,
                    self.team_a,
                    self.team_b
                )

                new_leader.append(leader)
            
            character_leader.leader = new_leader
            character_leader.leader_sorted = True

        # trigger all the leader if they've not been triggered 
        applied = False
        applied_list = []
        for _leader in character_leader.leader:
            await asyncio.sleep(0)

            if not _leader.triggered :
                await _leader.apply()
            
                applied = True
                applied_list.append(_leader)
        
        # display the applied effect
        if(applied):
            displaying = f"{character_leader.image.icon} **{character_leader.info.name}**{character_leader.type.icon} :\n"

            for leader_ in applied_list:
                await asyncio.sleep(0)

                displaying += f"• {leader_.icon}**__{leader_.name}__** : *{leader_.description}*"

            await ctx.send(displaying)
            await ctx.send("--")

        return
"""
Check if the target has an effect active on it.

--

Author : DrLarck

Last update : 19/10/19 (DrLarck)
"""

# dependancies
import asyncio

# effect checker
class Effect_checker:
    """
    Allows us to check if an unit has an effect active on it or not.

    - Parameter :

    `target` : Represents the target.

    - Method :

    :coro:`get_effect(effect_id, client, ctx, target, team_a, team_b)` : Get an effect instance.

    :coro:`get_buff(buff_instance)` : Research a buff onto the target

    :coro:`get_debuff(debuff_instance)` : Same as get_buff but for debuff.
    """

    # attribute
    def __init__(self, target):
        self.target = target
    
    # method
    async def get_effect(self, effect_id, client, ctx, target, team_a, team_b):
        """
        `coroutine`

        Get the effect instance if found, else return None.
        
        The returned effect is not suitable for a normal use. It's used to compare the effects based on their id.

        - Parameter :

        `effect_id` : int - The id of the effect you want to get.

        `client` : Represents a `discord.Client`.

        `ctx` : Represents the `commands.Context`.

        `target` : Represents a `Character()`, not `None`.

        `team A` | `B` : A  is the allied team, B the opponent one.
        
        --

        Return : Instance of the effect. Else : `None`.
        """

        # init
        effect = None

        # list of the effect
        # Dot Acid
        if(effect_id == 1):
            from utility.cog.character.ability.effect.dot.dot_acid import Dot_acid
            effect = Dot_acid(client, ctx, target, team_a, team_b)
        
        # Buff Unity is strength
        if(effect_id == 2):
            from utility.cog.character.ability.effect.buff.unity_is_strength import Buff_unity_is_strength
            effect = Buff_unity_is_strength(client, ctx, target, team_a, team_b)
        
        # Debuff acid explosion
        if(effect_id == 3):
            from utility.cog.character.ability.effect.debuff.acid_explosion import Debuff_acid_explosion
            effect = Debuff_acid_explosion(client, ctx, target, team_a, team_b)
        
        # Debuff Paralyzing burns
        if(effect_id == 4):
            from utility.cog.character.ability.effect.debuff.paralyzing_burns import Debuff_Paralyzing_burns
            effect = Debuff_Paralyzing_burns(client, ctx, target, team_a, team_b)

        # Buff Pilaf barrier
        if(effect_id == 5):
            from utility.cog.character.ability.effect.buff.pilaf_barrier import Buff_pilaf_barrier
            effect = Buff_pilaf_barrier(client, ctx, target, team_a, team_b)
        
        # Buff Triple pilots
        if(effect_id == 6):
            from utility.cog.character.ability.effect.buff.triple_pilots import Buff_triple_pilots
            effect = Buff_triple_pilots(client, ctx, target, team_a, team_b)
        
        # Passive Green Saibaiman passive
        if(effect_id == 7):
            from utility.cog.character.ability.effect.buff.saibaiman_gather_ki import Buff_gather_ki
            effect = Buff_gather_ki(client, ctx, target, team_a, team_b)
        
        # Event Last will, Acid !
        if(effect_id == 8):
            from utility.cog.character.ability.effect.on_event.last_will_acid import Event_last_will_acid
            effect = Event_last_will_acid(client, ctx, target, team_a, team_b)
        
        # Passive Last will, Acid !
        if(effect_id == 9):
            from utility.cog.character.ability.effect.buff.saibaiman_last_will_acid import Buff_last_will_acid
            effect = Buff_last_will_acid(client, ctx, target, team_a, team_b)
        
        # Passive Power charge
        if(effect_id == 10):
            from utility.cog.character.ability.effect.buff.saibaiman_power_charge import Buff_power_charge
            effect = Buff_power_charge(client, ctx, target, team_a, team_b)

        # Power of youth leader skill
        if(effect_id == 11):
            from utility.cog.character.ability.effect.buff.power_of_youth import Buff_power_of_youth
            effect = Buff_power_of_youth(client, ctx, target, team_a, team_b)
            
        return(effect)

    async def get_buff(self, buff):
        """
        `coroutine`

        Search for an effect in the `buff` list of the character. If the buff has been found return the current instance of it.
        Else return `None`.

        - Parameter :

        `buff` : Instance of `buff` to look for.

        --

        Return : Active instance of the effect. Else : `None`.
        """

        # init
        buff_id = buff.id 
        match = None

        for effect in self.target.bonus:
            await asyncio.sleep(0)

            if(effect.id == buff_id):
                match = effect
                break
            
        return(match)
    
    async def get_debuff(self, debuff):
        """
        `coroutine`

        Search for the debuff in the list of active debuffs on the target. If not found returns `None`.

        - Parameter : 

        `debuff` : Represents a debuff object.

        --

        Return : Active instance of the debuff. Else : `None`.
        """

        # init
        debuff_id = debuff.id 
        match = None

        for effect in self.target.malus:
            await asyncio.sleep(0)

            if(effect.id == debuff_id):
                match = effect

        return(match)
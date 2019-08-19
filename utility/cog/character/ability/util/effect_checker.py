"""
Check if the target has an effect active on it.

--

Author : DrLarck

Last update : 19/08/19 (DrLarck)
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

    :coro:`get_debugg(debuff_instance)` : Same as get_buff but for debuff.
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

        --

        Return : Instance of the effect. Else : `None`.
        """

        # init
        effect = None

        # list of the effect
        if(effect_id == 1):
            from utility.cog.character.ability.effect.dot.dot_acid import Dot_acid
            effect = Dot_acid(client, ctx, target, team_a, team_b)
            
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
            
        return(match)
    
    async def get_debuff(self, debuff):
        """
        `coroutine`

        Search for the debuff in the list of active debuffs on the target. If not found returns `None`.

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
"""
Manages the Unity is Strength ability.

--

Author : DrLarck

Last update : 28/09/19 (DrLarck)
"""

# dependancies
import asyncio

# utils
from utility.cog.displayer.move import Move_displayer
from utility.cog.character.ability.util.effect_checker import Effect_checker

# inheritance
from utility.cog.character.ability.ability import Ability

# spell
class Unity_is_strength(Ability):
    """
    Applies the Unity is Strenght buff on the Saibaimen.
    """

    # attribute
    def __init__(self, client, ctx, caster, target, team_a, team_b):
        # inheritance
        Ability.__init__(
            self,
            client,
            ctx,
            caster,
            target,
            team_a,
            team_b
        )

        # info
        self.name = "Unity is strength"
        self.description = f"""Applies the **__Unity is strength__** bonus on all the **Saibaiman** in your team.
Heals up the carriers of the bonus for an amount of **1 %** of the carrier's {self.game_icon['ki_ability']} per active **__Acid__** stack on the **enemy team**.
Moreover, **your team** stacks up **__Acid__** **2** time faster on the **enemy team** and increase their **maximum stack** and **duration** by **2**."""

        self.icon = "<:unity_is_strenght:585503883133059074>"
        self.cost = 60

        # special
        self.saibaimen = [1, 2, 3]  # represents the Saibaimen ids
    
    # method
    async def set_tooltip(self):
        self.tooltip = f"Add **__Unity is strength__**{self.game_icon['effect']['unity_is_strength']} bonus on all your **Saibaiman**."

        return

    async def use(self):
        """
        `coroutine`

        Applies the Unity is strenght buff on all the allied Saibaimen.

        --

        Return : str
        """

        # init
        await self.caster.posture.change_posture("attacking")
        move = Move_displayer()

        # applies the buff on the team
        for character in self.team_a:
            await asyncio.sleep(0)
            # init
            checker = Effect_checker(character)
            unity_buff = await checker.get_effect(
                2, 
                self.client, 
                self.ctx,
                character, 
                self.team_a, 
                self.team_b
            )

            ally_buff = None  # check if the ally already has the Unity is strenght active

            character.bonus.append(unity_buff)
            if character.info.id in self.saibaimen:
                # if the ally is a saibaimen
                # applies the buff
                ally_buff = await checker.get_buff(unity_buff)

                if(ally_buff != None):  # if the ally has the buff, reset duration
                    ally_buff.duration = unity_buff.initial_duration
                
                else:  # otherwise, add the buff
                    character.bonus.append(unity_buff)

        # setup the move display
        display = await move.get_new_move()
        display["name"] = self.name
        display["icon"] = self.icon
        display["ki"] = True

        display = await move.effect_move(display)

        return(display)
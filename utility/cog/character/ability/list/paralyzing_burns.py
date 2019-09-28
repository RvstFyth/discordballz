"""
Manages the paralyzing burns ability.

--

Author : DrLarck

Last update : 28/09/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability.ability import Ability
from utility.cog.character.ability.util.effect_checker import Effect_checker

# formatting
from utility.cog.displayer.move import Move_displayer

# icon
from configuration.icon import game_icon

# ability
class Paralyzing_burns(Ability):
    """
    Stuns the target according how many active acid stacks it has on it.
    Remove the acid stacks.

    Stun duration : 2 turns if == 3 acid 

    4 turns if >=3 acid

    The stun will be a malus effect which stuns at each applying.
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

        # stat
        self.name = "Paralyzing burns"
        self.description = f"""If the target has at least **3** stack of **__Acid__** active on it : get **Stunned** for **2** turns.
If the target has more than **3** **__Acid__** stack on it : get **Stunned** for **4** turns.
**Remove** al the **__Acid__** stacks on the target."""

        self.icon = self.game_icon['ability']['paralyzing_burns']
        self.cost = 75
        
        # targetting
        self.need_target = True
        self.target_enemy = True
    
    # method
    async def set_tooltip(self):
        self.tooltip = f"Stuns the target according to the amount of active **__Acid__**{self.game_icon['effect']['acid']} stacks on it."

        return

    async def use(self):
        """
        `coroutine`

        Applies the Paralyzing debuff on the target.

        If the target already has the debuff : reset the duration

        --

        Return : str
        """

        # init
        effect_checker = Effect_checker(self.target)
        move = Move_displayer()
        _move = ""

        has_paralyzing = None
        has_acid = None

        # effect reference
        acid_ref = await effect_checker.get_effect(
            1,
            self.client,
            self.ctx,
            self.target,
            self.team_a,
            self.team_b
        )

        paralyzing_ref = await effect_checker.get_effect(
            4,
            self.client,
            self.ctx,
            self.target,
            self.team_a,
            self.team_b
        )

        # set up the move
        _move = await move.get_new_move()

        _move["name"] = self.name
        _move["icon"] = self.icon
        _move["ki"] = True

        _move = await move.effect_move(_move)

        # check if the target has acid stack active
        has_acid = await effect_checker.get_debuff(acid_ref)

        if(has_acid != None):
            # get the amount of acid's stack the target has
            acid_stack = has_acid.stack 

            # check if the target has 3 or more active stacks
            if(acid_stack >= 3):
                # check if the target has an active paralyzing burns
                has_paralyzing = await effect_checker.get_debuff(paralyzing_ref)

                if(has_paralyzing != None):
                    # reset the duration
                    if(acid_stack == 3):
                        has_paralyzing.initial_duration = 2
                        has_paralyzing.duration = has_paralyzing.initial_duration
                    
                    elif(acid_stack > 3):
                        has_paralyzing.initial_duration = 4
                        has_paralyzing.duration = has_paralyzing.initial_duration
            
                else:  # the target doesn't have paralyzing burns active on it
                    # set the duration of the stun
                    if(acid_stack == 3):
                        paralyzing_ref.initial_duration = 2
                        paralyzing_ref.duration = paralyzing_ref.initial_duration
                    
                    elif(acid_stack > 3):
                        paralyzing_ref.initial_duration = 4
                        paralyzing_ref.duration = paralyzing_ref.initial_duration
                    
                    # apply the debuff on the target
                    self.target.malus.append(paralyzing_ref)
                
                # consums all the acid stacks
                self.target.malus.remove(has_acid)

            else:  # the target has less that 3 acid stacks
                pass
            
        else:
            # the target doesn't have acid stack, don't do nothing
            pass

        return(_move)
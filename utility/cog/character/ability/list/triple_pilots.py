"""
Manages the triple pilots ability.

--

Author : DrLarck

Last update : 28/09/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability.ability import Ability
from utility.cog.character.ability.util.effect_checker import Effect_checker
from utility.cog.displayer.move import Move_displayer

# ability
class Triple_pilots(Ability):
    """
    Consums one charge of Triple pilots to recover 30 % of Max health.
    """

    # attribute
    def __init__(self, client, ctx, caster, target, team_a, team_b):
        # inheritance
        Ability.__init__(self, client, ctx, caster, target, team_a, team_b)

        # info
        self.name = "Triple pilots"
        self.description = f"""This unit consums one stack of **__Triple pilots__** bonus to recover **30 %** of its **Maximum** :hearts:."""
        self.icon = "<:triple_pilots:627508544488603666>"

    # method
    async def set_tooltip(self):
        self.tooltip = f"Consums a charge of **__Triple pilots__**{self.game_icon['effect']['triple_pilots']} to restore **{int((30 * self.caster.health.maximum)/100):,}** :hearts:."
        
        return

    async def use(self):
        """
        `coroutine`

        Consums one stack of Triple pilots to recover health

        --

        Return : str
        """

        # init
        move = Move_displayer()
        heal = 0

        effect_checker = Effect_checker(self.caster)
        triple_ref = await effect_checker.get_effect(
            6,
            self.client,
            self.ctx,
            self.caster,
            self.team_a,
            self.team_b
        )

        # check if the caster has the triple pilots buff
        has_triple = await effect_checker.get_buff(triple_ref)

        if(has_triple != None) :
            if(has_triple.stack > 0):
                # consum a stack
                has_triple.stack -= 1

                # restore health
                heal = int((30 * self.caster.health.maximum) / 100)
                self.caster.health.current += heal
                await self.caster.health.health_limit()
            
            if(has_triple.stack <= 0):  # the caster doesn't have triple pilots stacks anymore
                self.caster.bonus.remove(has_triple)
        
        # set up the move
        _move = await move.get_new_move()

        _move["name"], _move["icon"] = self.name, self.icon
        _move = await move.effect_move(_move)
        
        if(heal > 0):
            _move += f"__Heal__ : **+{heal:,}** :hearts:"

        return(_move)
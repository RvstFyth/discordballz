"""
Ability super class.

--

Author : DrLarck

Last update : 26/07/19 (DrLarck)
"""

# dependance
import asyncio

# super class
class Ability:
    """
    Represents an ability.

    - Parameter :

    `client` : Represents the used `discord.Client`

    `ctx` : Represents the invocation `commands.Context`

    `target` : Represents the ability target as a `Character()` instance.

    `team` : Represents a list of `Character()`.

    - Attribute :

    `name` : Represents the ability name.

    `description` : Represents the ability description.

    `icon` : Represents the ability's icon as `discord.Emoji`.

    `cost` : Represents the ability ki cost.

    `cooldown` : Represents the ability cooldown.

    `need_target` : True if the target needs a target to be used.

    `target_ally` : True if the ability can target allies.

    `target_enemy` : True if the ability can target an oponnent.

    - Method :

    :coro:`init()` : Translates the ability name and description.

    :coro:`use()` : Triggers the ability.
    """

    # attribute
    def __init__(self, client, ctx, caster, target, team):
        # client
        self.client = client
        self.ctx = ctx
        self.caster = caster
        self.target = target
        self.team = team

        # attribute
        self.name = None
        self.description = None
        self.icon = None

        # condition
        self.cost = 0
        self.cooldown = 0

        # targetting
        self.need_target = False
        self.target_ally = False
        self.target_enemy = False
    
    # method
    async def init(self):
        """
        `coroutine`

        Translates the ability name and description.

        --

        Return : None
        """

        return
    
    async def use(self):
        """
        `coroutine`

        Triggers the ability.

        --

        Return : str (formatted string of the ability effect)
        """

        return
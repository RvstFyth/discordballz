"""
Represents a bonus effect

--

Author : DrLarck

Last update : 22/09/19 (DrLarck)
"""

# dependancies
import asyncio

# buff
class Effect:
    """
    Represents a bonus effect.

    - Parameter :

    `client` : Represents a `discord.Client` instance.

    `ctx` : Represents the `commands.Context`

    `carrier` : Represents the character who carries the buff.

    `team_a` | `b` : Represents the Ally team and the opponent team.

    - Attribute :

    `name` : default None - Represents the Buff's name.

    `description` : default None - Represents the Buff's description.

    `id` : default 0 - Represents the Buff's id.

    `icon` : default None - Represents the Buff's icon.

    `caster` : default None - Represents the Buff's caster.

    `initial_duration` : default 0 - Represents the Buff's initial duration.

    `duration` : default 0 - Represents the Buff's current duration.

    `is_permanent` : default False - Tells if an effect is permanent or not.

    `max_stack` : default 0 - Represents the Buff's max stacks.

    `stack` : default 0 - Represents the Buff's current stacks.

    `triggered` : default False - Tells if an effect has already been triggered or not.

    - Method :

    :coro:`translate()` : Allows you to translate the Buff's strings.

    :coro:`apply()` : Applies the Buff's effect.

    :coro:`on_remove()` : Does something on remove.
    """

    # attribute
    def __init__(self, client, ctx, carrier, team_a, team_b):
        # basic
        self.client = client
        self.ctx = ctx
        self.carrier = carrier
        self.team_a = team_a
        self.team_b = team_b

        # info
        self.name = None
        self.description = None
        self.id = 0
        self.icon = "<:notfound:617735236473585694>"
        self.caster = None

        # duration
        self.initial_duration = 1
        self.duration = 1
        self.is_permanent = False

        # stack
        self.max_stack = 1
        self.stack = 1

        # check
        self.triggered = False
    
    # method
    async def translate(self):
        return

    async def apply(self):
        return
    
    async def on_remove(self):
        return
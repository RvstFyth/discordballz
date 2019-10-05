"""
Manages the DOT super class.

--

Author : DrLarck

Last update : 29/09/19 (DrLarck)
"""

# dependancies
import asyncio

from configuration.icon import game_icon

# super dot class
class Dot:
    """
    Manages the DOT behaviour.

    - Parameter : 

    `client` : Represents the `discord.Client`

    `ctx` : Represents the `commands.Context`

    `team_a` | `team_b` : Represents a list of `Character()`.
    Team A represents the ally team of the caster and the Team B the opponent one.

    - Attribute :

    `name` : Represents the Dot name
    
    `description` : Represents the Dot description

    `id` : Represents the Dot id (default 0)
    
    `icon` : Represents the Dot icon

    `caster` : Represents the Dot caster

    `initial_duration` : Represents the Dot initial duration, usefull for duration refreshing.

    `duration` : Represents the Dot's current duration.

    `max_stack` : Represents the Dot's max stacks that it can handles.

    `stack` : Represents the Dot's active stacks.

    `total_damage : Represents the total damage the Dot is going to inflict.

    `tick_damage` : Represents the damages the Dot is inflicting at each tick.

    - Method :

    :coro:`translate()` : Allows you to translate the Dot's strings.

    :coro:`apply()` : Apply the Dot effects to the target.

    :coro:`set_damage()` : Set the tick damage. According to the Dot behaviour.

    :coro:`add_stack()` : Add a stack to the target.

    :coro:`on_remove()` : Do something on remove.
    """

    # attribute
    def __init__(self, client, ctx, team_a, team_b):
        # client
        self.client = client
        self.ctx = ctx
        self.team_a = team_a
        self.team_b = team_b

        # dot
        self.name = None
        self.description = None
        self.id = 0
        self.icon = "<:notfound:617735236473585694>"
        self.game_icon = game_icon
        self.caster = None

        # duration
        self.initial_duration = 0
        self.duration = 0
        self.is_permanent = False

        # stack
        self.max_stack = 0
        self.stack = 0

        # damage
        self.total_damage = 0
        self.tick_damage = 0

    # method
    async def translate(self):
        return

    async def apply(self):
        return

    # init
    async def set_damage(self):
        return
    
    async def add_stack(self):
        return
    
    async def on_remove(self):
        return
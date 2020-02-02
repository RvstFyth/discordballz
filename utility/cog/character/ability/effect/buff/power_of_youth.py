"""
Power of youth buff

--

Author :

Last update : 02/02/2020 (RvStFyth)
"""

import asyncio

from utility.cog.character.ability._effect import Effect


class Buff_power_of_youth(Effect):

    def __init__(self, client, ctx, carrier, team_a, team_b):
        # inheritance
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        # info
        self.name = "Power of youth!"
        self.icon = ""
        self.id = 11

        # duration
        self.is_permanent = False

    async def apply(self):
        """
        `coroutine`

        +10% damage with their first attack of the battle

        --

        :return:
        """
        self.carrier.damage.physical_max *= 1.1
        self.carrier.damage.ki_max *= 1.1


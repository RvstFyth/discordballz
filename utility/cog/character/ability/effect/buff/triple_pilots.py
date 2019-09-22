"""
Manages the triple pilots buff.

--

Author : DrLarck

Last update : 22/09/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability._effect import Effect

# buff
class Buff_triple_pilots(Effect):
    """
    Doesn't really do anything, it can be consummed by Pilaf Machine to restore health.
    """

    # attribute
    def __init__(self, client, ctx, carrier, team_a, team_b):
        # inheritance
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        # info
        self.name = "Triple pilots"
        self.id = 6
        
        # duration
        self.initial_duration = 1
        self.duration = 1
        self.is_permanent = True
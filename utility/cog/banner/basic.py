"""
Manages the basic banner.

--

Author : DrLarck

Last update : 30/01/20 (DrLarck)
"""

# dependancies
import asyncio

# utils
from utility.cog.banner._banner import Banner
from utility.command._summon import Summoner

# basic banner
class Basic_banner(Banner):
    """
    Represents a basic banner.
    """

    # class attr
    summonable = None

    # attribute
    def __init__(self):
        # inheritance
        Banner.__init__(self)
        # attr
        self.all = [
            1, 2, 3, 4, 5,
            6, 7, 8, 9, 10
        ]
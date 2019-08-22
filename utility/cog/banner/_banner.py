"""
Manages the banner object

--

Author : DrLarck

Last update : 22/08/19 (DrLarck)
"""
# dependancies
import asyncio

# banner object
class Banner:
    """
    Represents the Banner object.

    - Attribute :

    `summonable` : dict - List of summonable character for this banner. (i.e Summoner for dict keys)

    `all` : list - All the characters contained in the banner are stored here.
    """

    # class attr
    summonable = None

    # attribute
    def __init__(self):
        self.all = []  # stores all the characters the banner contains
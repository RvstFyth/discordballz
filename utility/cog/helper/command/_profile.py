"""
Profile help panel

--

Author : DrLarck

Last update : 08/01/2020 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.helper.command.command_help import Help_command

class Help_profile(Help_command):
    """
    Profile help panel
    """

    def __init__(self):
        Help_command.__init__(self)
        self.name = "Profile"
        self.description = "Display your profile which contains informations about you, your resources, collection, etc."
        self.invoke = "profile"
        self.aliases = ["p"]

        self.fields = [
            {
                "name" : "d!profile | p",
                "value" : "Display your informations, the amount of resources you have, the number of characters you own, your experience, level, etc."
            }
        ]
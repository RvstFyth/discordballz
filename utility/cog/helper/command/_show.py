"""
Show command help panel

--

Author : DrLarck

Last update : 08/01/2020 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.helper.command.command_help import Help_command

class Help_show(Help_command):
    """
    Show command help panel
    """

    def __init__(self):
        Help_command.__init__(self)
        self.name = "Show"
        self.description = "Display informations about the asked character"
        self.invoke = "show"

        self.fields = [
            {
                "name" : "d!show [id/unique id] [level]",
                "value" : "Display informations about a character."
            }
        ]

"""
Start help panel

--

Author : DrLarck

Last update : 12/01/2020 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.helper.command.command_help import Help_command

class Help_start(Help_command):
    """
    Start help panel
    """

    def __init__(self):
        Help_command.__init__(self)
        self.name = "Start"
        self.description = "Allow you to begin your adventure"
        self.invoke = "start"

        self.fields = [
            {
                "name" : "d!start",
                "value" : "Allow you to begin a new adventure"
            }
        ]
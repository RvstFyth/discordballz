"""
The help pannel for the box command

--

Author : DrLarck

Last update : 08/01/2020 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.helper.command.command_help import Help_command

class Help_box(Help_command):
    """
    The help pannel for the box command
    """
    
    # attribute
    def __init__(self):
        Help_command.__init__(self)
        self.name = "Box"
        self.description = "Display your collection of characters"
        self.invoke = "box"

        self.fields = [
            {
                "name" : "d!box",
                "value" : "Display your collection of characters"
            },
            {
                "name" : "d!box [id]",
                "value" : "Display the `unique id` of the character corresponding to the passed `id`"
            }
        ]
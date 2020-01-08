"""
Manages the summon help

--

Author : DrLarck

Last update : 08/01/2020 (DrLarck)
"""

# dependancies
import asyncio
from utility.cog.helper.command.command_help import Help_command

# graphic
from utility.graphic.embed import Custom_embed

class Help_summon(Help_command):
    def __init__(self):
        Help_command.__init__(self)
        self.name = "Summon"
        self.description = "Allow you to summon a new character"
        self.invoke = "summon"
        self.aliases = ["sum"]

        self.fields = [
            {
                "name" : "d!summon | sum",
                "value" : "Displays the command help."
            },
            {
                "name" : "d!summon basic",
                "value" : "Summon a random character from the **Basic** expansion."
            }
        ]
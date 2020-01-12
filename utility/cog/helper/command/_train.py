"""
Train help panel

--

Author : DrLarck

Last update : 12/01/2020 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.helper.command.command_help import Help_command

class Help_train(Help_command):
    """
    Train help panel
    """

    def __init__(self):
        Help_command.__init__(self)
        self.name = "Train"
        self.description = "Allow you to train your characters"
        self.invoke = "train"

        self.fields = [
            {
                "name" : "d!train",
                "value" : "Start a training fight to level up your characters"
            }
        ]
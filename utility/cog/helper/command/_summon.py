"""
Manages the summon help

--

Author : DrLarck

Last update : 29/08/19 (DrLarck)
"""

# dependancies
import asyncio

# graphic
from utility.graphic.embed import Custom_embed

async def _summon(client):
    """
    `coroutine`

    Displays the command.help for the summon command.

    --

    Return : send a discord.Message (embedded)
    """

    # init
    embed = Custom_embed(client)
    summon_help = await embed.setup_embed()

    # setup
    # title and desc
    summon_help.add_field(
        name = "Summon commands :",
        value = "Welcome to the **Summon** help pannel.\n__Aliases__ : sum",
        inline = False
    )

    # commands
    summon_help.add_field(
        name = "d!summon | sum",
        value = "Displays the command help.",
        inline = False
    )

    summon_help.add_field(
        name = "d!summon basic",
        value = "Summons a random character from the **Basic** expansion.",
        inline = False
    )

    return(summon_help)
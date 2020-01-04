"""
Manages the player's profile.

--

Author : DrLarck

Last update : 04/01/2020 (DrLarck)
"""

# dependancies
import asyncio
from discord.ext import commands

# util
from utility.cog.player.player import Player
    # graphic
from utility.graphic.embed import Custom_embed

# checker
from utility.command.checker.basic import Basic_checker

# icon
from configuration.icon import game_icon

# profile command
class Cmd_profile(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @commands.command(aliases = ["p"])
    async def profile(self, ctx):
        """
        Call the player's profile.
        """

        # init
            # player
        player = Player(ctx, self.client, ctx.message.author)
        await player.resource.update()  # update the resources count
        char_amount = await player.box.get_characters_amount()
            # embed
        profile_embed = await Custom_embed(self.client, thumb = player.avatar, title = f"{player.name}'s profile").setup_embed()

        # prepare the embed
        profile_embed.add_field(
            name = ":star: Level",
            value = 0,
            inline = True
        )

        profile_embed.add_field(
            name = f"{game_icon['dragonstone']} Dragon stone",
            value = f"{player.resource.dragonstone:,}",
            inline = True
        )

        profile_embed.add_field(
            name = f"{game_icon['zenis']} Zenis",
            value = f"{player.resource.zenis:,}",
            inline = True
        )

        profile_embed.add_field(
            name = ":trophy: Collection",
            value = f"{char_amount:,}",
            inline = True
        )

        # display the profile
        await ctx.send(embed = profile_embed)


def setup(client):
    client.add_cog(Cmd_profile(client))
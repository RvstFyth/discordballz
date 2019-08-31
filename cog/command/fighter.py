"""
Allows the player to manage his team

--

Author : DrLarck

Last update : 31/08/19 (DrLarck)
"""

# dependancies
import asyncio
from discord.ext import commands

# utils
from utility.cog.player.player import Player
from utility.command._fighter import Fighter
from utility.cog.character.getter import Character_getter
from utility.command._fighter import Fighter

# graphic
from utility.graphic.embed import Custom_embed
from utility.cog.displayer.icon import Icon_displayer

# check
from utility.command.checker.basic import Basic_checker

# command
class Cmd_fighter(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.getter = Character_getter()
        self.icon = Icon_displayer()

    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @commands.group()
    async def fighter(self, ctx):
        """
        The fighter command group
        """

        # display the fighter help here

    ################ FIGHTER ###################
    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @fighter.command()
    async def remove(self, ctx, slot):
        """
        Allows the player to remove a character from a slot.
        """

        # init
        player = Player(ctx, self.client, ctx.message.author)
        player_team = await player.team.get_team()
        getter = Character_getter()
        possible_slot = ["a", "b", "c"]


        # remove the slot
        if slot.lower() in possible_slot:
            await player.team.remove(slot)
            removed_character = await getter.get_from_unique(self.client, player_team[slot])
            await removed_character.init()

            await ctx.send(f"<@{player.id}> You have successfully removed {removed_character.image.icon}**{removed_character.info.name}** {removed_character.type.icon}{removed_character.rarity.icon} from the slot **{slot.upper()}**.")

        else:  # unexisting slot
            await ctx.send(f"<@{player.id}> Slot **{slot.upper()}** not found.")

        return
        
    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @fighter.command()
    async def team(self, ctx):
        """
        Displays the player's team.
        """

        # init
        player = Player(ctx, self.client, ctx.message.author)
        player_team = await player.team.get_team()
        player_team_info = await player.team.get_info()
        embed = await Custom_embed(self.client).setup_embed()

        char_a, char_b, char_c = None, None, None

        # set the info icon
        player_team_info["rarity"] = await self.icon.get_rarity_icon(player_team_info["rarity"])

        # set the player team display
        ### a 
        if(player_team["a"] == None):
            player_team["a"] = "--"
        
        else:
            char_a = await self.getter.get_from_unique(self.client, player_team["a"])
            char_a = f"{char_a.image.icon}{char_a.info.name} {char_a.type.icon}{char_a.rarity.icon} lv.{char_a.level:,}"
        
        ### b
        if(player_team["b"] == None):
            player_team["b"] = "--"
        
        else:
            char_b = await self.getter.get_from_unique(self.client, player_team["b"])
            char_b = f"{char_b.image.icon}{char_b.info.name} {char_b.type.icon}{char_b.rarity.icon} lv.{char_b.level:,}" 
        
        ### c
        if(player_team["c"] == None):
            player_team["c"] = "--"
        
        else:
            char_c = await self.getter.get_from_unique(self.client, player_team["c"])
            char_c = f"{char_c.image.icon}{char_c.info.name} {char_c.type.icon}{char_c.rarity.icon} lv.{char_c.level:,}"

        # set display
        display_infos = f"""
        *Average level* : {player_team_info['level']}
        *Average rarity* : {player_team_info['rarity']}
        """

        display_character = f"""
        A : **{char_a}** 👑
        B : **{char_b}**
        C : **{char_c}**
        """

        # set the embed
        embed.set_thumbnail(url = player.avatar)
        embed.add_field(
            name = f"{player.name}'s team",
            value = display_infos,
            inline = False
        )

        embed.add_field(
            name = "Fighters",
            value = display_character,
            inline = False
        )

        await ctx.send(embed = embed)

    #################### SET ####################
    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @fighter.group(invoke_without_command = True)
    async def set(self, cxt):
        """
        Allow the player to set a fighter
        """

        # display the set help here

    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @set.command()
    async def a(self, ctx, character_id):
        """
        Set the fighter slot a
        """

        # init
        player = Player(ctx, self.client, ctx.message.author)
        fighter = Fighter(ctx, self.client, player)

        await fighter.fighter_command("a", character_id)
    
    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @set.command()
    async def b(self, ctx, character_id):
        """
        Set the fighter slot b
        """

        # init
        player = Player(ctx, self.client, ctx.message.author)
        fighter = Fighter(ctx, self.client, player)

        await fighter.fighter_command("b", character_id)
    
    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @set.command()
    async def c(self, ctx, character_id):
        """
        Set the fighter slot c
        """

        # init
        player = Player(ctx, self.client, ctx.message.author)
        fighter = Fighter(ctx, self.client, player)

        await fighter.fighter_command("c", character_id)

def setup(client):
    client.add_cog(Cmd_fighter(client))
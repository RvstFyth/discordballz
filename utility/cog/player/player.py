"""
Manages the player object.

--

Author : DrLarck

Last update : 26/08/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.player.attribute.resource import Player_resource

# player
class Player:
    """
    Represents a player.

    - Parameter : 
    
    `client` : Represents a `discord.Client`. The client must handle a database connection pool.

    `player` : Represents a `discord.Member`

    - Attribute :

    `name` : Represents the player's name.

    `id` : Represents the player's id.

    `avatar` : Represents the player's avatar url
    """

    # attribute
    def __init__(self, client, player):
        # basics
        self.client = client
        # player infos
        self.name = player.name
        self.id = player.id
        self.avatar = player.avatar_url

        # resource
        self.resource = Player_resource(self.client, self)
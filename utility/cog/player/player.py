"""
Manages the player object.

--

Author : DrLarck

Last update : 19/08/19
"""

# dependancies
import asyncio

# player
class Player:
    """
    Represents a player.

    - Parameter : 
    
    `player` : Represents a `discord.Member`

    - Attribute :

    `name` : Represents the player's name.

    `id` : Represents the player's id.

    `avatar` : Represents the player's avatar url
    """

    # attribute
    def __init__(self, player):
        # player infos
        self.name = player.name
        self.id = player.id
        self.avatar = player.avatar_url
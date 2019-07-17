"""
Manages the character's rarity attribute.

--

Author : DrLarck

Last update : 17/07/19
"""

# class rarity
class Character_rarity:
    """
    Manages the character's rarity attribute.

    - Attribute :

    `icon` : Represents the rarity icon (emoji).

    `value` : Represents the rarity value (0 to 5)
    """

    # attribute
    def __init__(self):
        self.icon = None
        self.value = 0
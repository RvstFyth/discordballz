"""
Manages the character's defense attribute.

--

Author : DrLarck

Last update : 18/07/19
"""

# defense
class Character_defense:
    """
    Manages the character's defense attribute.

    - Attribute :

    `armor` : Represents the armor value.

    `spirit` : Represents the ki defense.

    `dodge` : Represents the dodge chance as %.

    `parry` : Represents the parry chance as %.

    `damage_reduction` : Represents the damage reduction as %.
    """

    # attribute
    def __init__(self):
        self.armor = 0
        self.spirit = 0
        self.dodge = 0  # % chance
        self.parry = 0  # % chance
        self.damage_reduction = 0  # %
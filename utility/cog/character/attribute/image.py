"""
Manages the character's images.

--

Author : DrLarck

Last update : 01/09/19 (DrLarck)
"""

# class image
class Character_image:
    """
    Manages the character's images.

    - Attribute :

    `image` : Represents the image url of the character.

    `icon` : Represents the character icon (emoji).

    `thumb` : Represents the character thumbnail (url)
    """

    # attribute 
    def __init__(self):
        self.image = "https://i.imgur.com/eMiHxeP.png"
        self.icon = "<:notfound:617735236473585694>"
        self.thumb = "https://i.imgur.com/eMiHxeP.png"
        self.expansion = None
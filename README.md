# Discord Quote Bot
Code for a discord bot that will paste a discord message to a landscape image to make it look like an inspirational quote.

- You can make your own quote bot for your friends by copying this code and then pasting your bot token to the `token` variable
- You can modify the background images through the gfx folder, make sure to add the new backgrounds in the ``images`` list and update ``numImages``
- - Currently all images have been set to be 1200x625 (16:9), this can be changed by modifying the ``imgWidth`` and ``imgHeight`` variables if a different ratio is desired, you will also likely have to modify the font size and the number of characters in the ``textwrap`` function as well if you do this

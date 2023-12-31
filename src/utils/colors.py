from cmu_graphics import rgb


# CITE: all colors are grabbed from https://generals.io by inspecting
# the HTML webpage content
class Colors:
    """
    Colors used in the game.
    """

    # grid colors
    BACKGROUND = rgb(34, 34, 34)
    BORDER = rgb(0, 0, 0)
    VISIBLE_CELL = rgb(220, 220, 220)
    FOG = rgb(57, 57, 57)
    VISIBLE_MOUNTAIN = rgb(187, 187, 187)
    VISIBLE_CITY = rgb(128, 128, 128)

    SURROUNDING_FOG_VISIBLE = rgb(108, 108, 108)
    SURROUNDING_FOG_NOT_VISIBLE = rgb(43, 43, 43)

    SURROUNDING_MOUNTAIN_VISIBLE = rgb(187, 187, 187)
    SURROUNDING_CITY_VISIBLE = rgb(72, 72, 72)
    SURROUNDING_OBSTACLE_NOT_VISIBLE = rgb(43, 43, 43)

    SURROUNDING_BLUE_VISIBLE = rgb(48, 60, 107)
    SURROUNDING_RED_VISIBLE = rgb(123, 30, 25)

    PREMOVE = rgb(0, 0, 0)

    # theme colors
    RED = rgb(254, 48, 0)
    BLUE = rgb(66, 99, 216)
    WHITE = rgb(255, 255, 255)
    ACCENT = rgb(0, 128, 128)
    BLACK = rgb(0, 0, 0)

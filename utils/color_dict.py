class ColorDict:
  """
  Centralize color vals here to avoid declaring colors in every function and/or class
  """

  def __init__(self) -> None:
    self.colors = self.all_colors()

  def all_colors(self):
    return {
      "bg_blue": (120, 220, 240),
      "bg_green": (80, 220, 140),
      "black": (0, 0, 0),
      "blue": (50, 20, 250),
      "brown": (52, 26, 0),
      "dark_blue": (64, 25, 255),
      "off_dark_blue": (125, 110, 170),
      "green": (25, 255, 140),
      "off_green": (110, 140, 130),
      "grey25": (25, 25, 25),
      "grey80": (80, 80, 80),
      "grey140": (140, 140, 140),
      "grey210": (195, 210, 210),
      "grey230": (230, 230, 230),
      "highlight": (180, 180, 180),
      "light_blue": (220, 220, 250),
      "olive_green": (85,107,47),
      "orange": (255, 153, 51),
      "off_orange": (160, 140, 115),
      "off_white": (220, 220, 226),
      "purple": (136, 0, 204),
      "off_purple": (110, 65, 140),
      "red": (150, 25, 25),
      "bright_red": (255, 51, 51),
      "off_bright_red": (190, 140, 140),
      "water_blue": (25, 255, 255),
      "off_water_blue": (110, 145, 150),
      "white": (250, 250, 250),
      "yellow": (240, 230, 175),
      "bright_yellow": (255, 255, 51),
      "off_bright_yellow": (180, 180, 145)
    }

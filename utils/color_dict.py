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
      "grey80": (80, 80, 80),
      "grey140": (140, 140, 140),
      "grey210": (195, 210, 210),
      "grey230": (230, 230, 230),
      "highlight": (180, 180, 180),
      "light_blue": (220, 220, 250),
      "olive_green": (85,107,47),
      "off_white": (220, 220, 226),
      "red": (150, 25, 25),
      "water_blue": (30, 40, 180),
      "white": (250, 250, 250),
      "yellow": (240, 230, 175),
    }

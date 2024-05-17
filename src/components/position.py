class PositionComponent:
  """A class representing the position of an object.

  Attributes:
    x (int): The x-coordinate of the position.
    y (int): The y-coordinate of the position.
  """

  def __init__(self, x, y):
    """
    Initialize a new PositionComponent instance.

    Args:
      x (int): The initial x-coordinate of the position.
      y (int): The initial y-coordinate of the position.
    """
    self.x = x
    self.y = y
  
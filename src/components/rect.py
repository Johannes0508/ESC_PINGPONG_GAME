from pygame import Rect


class RectComponent:
  """A class representing a rectangular component.

  Attributes:
    rect (Rect): A rectangle with specified dimensions.

  Args:
    x (int): The x-coordinate of the top-left corner of the rectangle.
    y (int): The y-coordinate of the top-left corner of the rectangle.
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
  """  

  def __init__(self, x, y, width, height):
    self.rect = Rect(x, y, width, height)

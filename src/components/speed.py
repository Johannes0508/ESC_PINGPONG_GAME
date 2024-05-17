class SpeedComponent:
  """A class representing the speed component of an object.

  Attributes:
    speed (float): The overall speed of the object.
    x_speed (float): The speed of the object in the x-direction.
    y_speed (float): The speed of the object in the y-direction.
  """

  def __init__(self, speed):
    self.speed = speed  
    self.x_speed = self.speed  
    self.y_speed = -self.speed  

import pygame
from components import RadiusComponent, RectComponent
from config import screen_height, screen_width, white

screen = pygame.display.set_mode((screen_width, screen_height))


class RenderingSystem:
  """A class responsible for rendering game entities on the screen.

  This class provides methods to draw the player's paddle and the ball on the screen.

  Attributes:
    None

  Methods:
    draw_paddle: Draws the player's paddle on the screen.
    draw_ball: Draws the ball on the screen.
  """

  def draw_paddle(self, entity):
    """
    Draw the paddle on the screen.

    Args:
      entity: The entity representing the paddle.

    Returns:
      None
    """
    rect = entity.get_component(RectComponent).rect
    pygame.draw.rect(screen, white, rect)

  def draw_ball(self, entity):
    """Draws a ball on the screen.

    Args:
      entity (Entity): The entity representing the ball.
    """
    ball_radius = entity.get_component(RadiusComponent).radius
    rect = entity.get_component(RectComponent).rect
    pygame.draw.circle(screen, white, rect.center, ball_radius)

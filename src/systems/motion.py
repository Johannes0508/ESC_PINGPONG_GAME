import pygame
from components import RectComponent, SpeedComponent, WinnerComponent
from config import margin, screen_height, screen_width


class MotionSystem:
  """A class that handles the movement of players and the ball in a ping pong game.

  This class contains methods to move the player, move the AI, and move the ball.
  """

  def move_player(self, entity_player):
    rect = entity_player.get_component(RectComponent).rect
    speed = entity_player.get_component(SpeedComponent).speed
    key = pygame.key.get_pressed()

    if key[pygame.K_UP] and rect.top > margin:
      rect.y -= speed
    if key[pygame.K_DOWN] and rect.bottom < screen_height:
      rect.y += speed

  def move_ai(self, entity_ball, entity_ai):
    rect_ai = entity_ai.get_component(RectComponent).rect
    speed_ai = entity_ai.get_component(SpeedComponent).speed
    rect_ball = entity_ball.get_component(RectComponent).rect

    if rect_ai.centery < rect_ball.centery and rect_ai.bottom < screen_height:
      rect_ai.y += speed_ai
    if rect_ai.centery > rect_ball.centery and rect_ai.top > margin:
      rect_ai.y -= speed_ai

  def move_ball(self, entity_ball, entity_player, entity_ai):
    rect_ball = entity_ball.get_component(RectComponent).rect
    speed_ball = entity_ball.get_component(SpeedComponent)
    rect_player = entity_player.get_component(RectComponent).rect
    rect_ai = entity_ai.get_component(RectComponent).rect

    if rect_ball.top <= margin or rect_ball.bottom >= screen_height:
      speed_ball.y_speed *= -1
    if rect_ball.colliderect(rect_player) or rect_ball.colliderect(rect_ai):
      speed_ball.x_speed *= -1

    rect_ball.x += speed_ball.x_speed
    rect_ball.y += speed_ball.y_speed

    if rect_ball.right >= screen_width:
      entity_ball.get_component(WinnerComponent).winner = 1
    elif rect_ball.left <= 0:
      entity_ball.get_component(WinnerComponent).winner = -1

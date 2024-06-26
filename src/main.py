import pygame  # Importera pygame-biblioteket
from components import (
  PositionComponent,
  RadiusComponent,
  RectComponent,
  SpeedComponent,
  WinnerComponent,
)

from systems import MotionSystem, RenderingSystem

from entities import Entity

pygame.init()  # Initialisera pygame-modulen

screen_width = 600  # Bredden på spelbildskärmen
screen_height = 500  # Höjden på spelbildskärmen

fpsClock = pygame.time.Clock(
)  # Skapa en klocka för att hålla koll på bilduppdateringshastigheten

# Skapa en spelbildskärm med specificerade dimensioner
screen = pygame.display.set_mode((screen_width, screen_height))

# Ange titeln på fönstret
pygame.display.set_caption('Pong')

# Skapa ett typsnitt för textrendering
font = pygame.font.SysFont('Constantia', 30)

# Definiera variabler för spelet
margin = 50  # Avståndet från överkanten till spelfältet
cpu_score = 0  # Motståndarens poäng
player_score = 0  # Spelarens poäng
fps = 60  # Bilduppdateringshastigheten (frames per second)
live_ball = False  # Flagga som indikerar om bollen är i spel eller inte
winner = 0  # Flagga som håller koll på vinnaren av varje omgång
speed_increase = 0  # Variabel för att öka bollens hastighet

# Definiera färger som används i spelet
bg = (50, 25, 50)  # Bakgrundsfärg
white = (255, 255, 255)  # Vit färg för linjer, text och spelobjekt


# Funktion för att rita spelplanen
def draw_board():
  screen.fill(bg)  # Fyll skärmen med bakgrundsfärgen
  # Rita en linje över skärmen för att markera spelfältets övre kant
  pygame.draw.line(screen, white, (0, margin), (screen_width, margin), 2)


# Funktion för att rita text på skärmen
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)  # Skapa en textbild
  screen.blit(
      img, (x, y))  # Rita textbilden på skärmen vid specificerade koordinater


# class MotionSystem:
#   """A class that handles the movement of players and the ball in a ping pong game.

#   This class contains methods to move the player, move the AI, and move the ball.
#   """

#   def move_player(self, entity_player):
#     rect = entity_player.get_component(RectComponent).rect
#     speed = entity_player.get_component(SpeedComponent).speed
#     key = pygame.key.get_pressed()

#     if key[pygame.K_UP] and rect.top > margin:
#       rect.y -= speed
#     if key[pygame.K_DOWN] and rect.bottom < screen_height:
#       rect.y += speed

#   def move_ai(self, entity_ball, entity_ai):
#     rect_ai = entity_ai.get_component(RectComponent).rect
#     speed_ai = entity_ai.get_component(SpeedComponent).speed
#     rect_ball = entity_ball.get_component(RectComponent).rect

#     if rect_ai.centery < rect_ball.centery and rect_ai.bottom < screen_height:
#       rect_ai.y += speed_ai
#     if rect_ai.centery > rect_ball.centery and rect_ai.top > margin:
#       rect_ai.y -= speed_ai

#   def move_ball(self, entity_ball, entity_player, entity_ai):
#     rect_ball = entity_ball.get_component(RectComponent).rect
#     speed_ball = entity_ball.get_component(SpeedComponent)
#     rect_player = entity_player.get_component(RectComponent).rect
#     rect_ai = entity_ai.get_component(RectComponent).rect

#     if rect_ball.top <= margin or rect_ball.bottom >= screen_height:
#       speed_ball.y_speed *= -1
#     if rect_ball.colliderect(rect_player) or rect_ball.colliderect(rect_ai):
#       speed_ball.x_speed *= -1

#     rect_ball.x += speed_ball.x_speed
#     rect_ball.y += speed_ball.y_speed

#     if rect_ball.right >= screen_width:
#       entity_ball.get_component(WinnerComponent).winner = 1
#     elif rect_ball.left <= 0:
#       entity_ball.get_component(WinnerComponent).winner = -1


# class RenderingSystem:
#   """A class responsible for rendering game entities on the screen.

#   This class provides methods to draw the player's paddle and the ball on the screen.

#   Attributes:
#     None

#   Methods:
#     draw_paddle: Draws the player's paddle on the screen.
#     draw_ball: Draws the ball on the screen.
#   """
#   def draw_paddle(self, entity):
#     """
#     Draw the paddle on the screen.

#     Args:
#       entity: The entity representing the paddle.

#     Returns:
#       None
#     """
#     rect = entity.get_component(RectComponent).rect
#     pygame.draw.rect(screen, white, rect)

#   def draw_ball(self, entity):
#     """Draws a ball on the screen.

#     Args:
#       entity (Entity): The entity representing the ball.
#     """    
#     ball_radius = entity.get_component(RadiusComponent).radius
#     rect = entity.get_component(RectComponent).rect
#     pygame.draw.circle(screen, white, rect.center, ball_radius)


entity_player = Entity()  
entity_ai = Entity()  
entity_ball = Entity()  

entity_player.add_component(
    PositionComponent(screen_width - 40, screen_height //
                      2))  
entity_player.add_component(
    SpeedComponent(5))  
entity_player.add_component(
    RectComponent(screen_width - 40, screen_height // 2, 20,
                  100))  

entity_ai.add_component(PositionComponent(
    20, screen_height // 2))  
entity_ai.add_component(
    SpeedComponent(5)) 
entity_ai.add_component(RectComponent(
    20, screen_height // 2, 20, 100)) 

entity_ball.add_component(
    PositionComponent(screen_width // 2, screen_height //
                      2)) 
entity_ball.add_component(
    SpeedComponent(4))  
entity_ball.add_component(
    RadiusComponent(8))  
entity_ball.add_component(
    RectComponent(screen_width // 2, screen_height // 2, 16,
                  16))  
entity_ball.add_component(
    WinnerComponent()) 

run = True
while run:
  fpsClock.tick(fps)  
  draw_board()  
  draw_text(f'CPU: {cpu_score}', font, white, 20,
            15)  
  draw_text(f'P1: {player_score}', font, white, screen_width - 100,
            15)  
  RenderingSystem().draw_paddle(
      entity_player)  
  RenderingSystem().draw_paddle(entity_ai) 

  if live_ball:  # Om bollen är i spel
    MotionSystem().move_ball(entity_ball, entity_player,
                             entity_ai)  # Hantera bollens rörelse
    MotionSystem().move_player(entity_player)  # Hantera spelarens rörelse
    MotionSystem().move_ai(entity_ball, entity_ai)  # Hantera AI:ns rörelse
    RenderingSystem().draw_ball(entity_ball)  # Rita ut bollen på skärmen
    winner = entity_ball.get_component(
        WinnerComponent).winner  # Hämta vinnarkomponenten för bollen
    if winner != 0:  # Om det finns en vinnare
      live_ball = False  # Sätt flaggan för att indikera att bollen inte längre är i spel
      cpu_score += winner == 1  # Öka motståndarens poäng om vinnaren är CPU
      player_score += winner == -1  # Öka spelarens poäng om vinnaren är spelaren
  else:
    draw_text('CLICK ANYWHERE TO START', font, white, 100,
              screen_height // 2)  # Visa en startmeddelande på skärmen

  # Lyssna på händelser från användaren eller systemet
  for event in pygame.event.get():
    if event.type == pygame.QUIT:  # Om fönstret stängs
      run = False  # Avsluta huvudspelloopen
    elif event.type == pygame.MOUSEBUTTONDOWN and not live_ball:  # Om musknappen trycks ner och bollen inte är i spel
      live_ball = True  # Sätt flaggan för att indikera att bollen är i spel
      entity_ball.get_component(PositionComponent).__init__(
          screen_width // 2, screen_height // 2)  # Återställ bollens position
      speed_component = entity_ball.get_component(
          SpeedComponent)  # Hämta hastighetskomponenten för bollen
      if winner == 1:  # Om vinnaren var CPU
        speed_component.x_speed = -4  # Sätt bollens hastighet i x-led till vänster
      else:
        speed_component.x_speed = 4  # Annars, sätt bollens hastighet i x-led till höger
      speed_component.y_speed = -4  # Sätt bollens hastighet i y-led uppåt
      entity_ball.get_component(
          WinnerComponent).winner = 0  # Återställ vinnarkomponenten för bollen

  pygame.display.update()  # Uppdatera skärmen

pygame.quit()  # Avsluta pygame-modulen

import pygame  # Importera pygame-biblioteket
from pygame import Rect  # Importera Rect-klassen från pygame

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


# Klassdefinitioner för komponenter
class Entity:
  id_counter = 0  # En räknare för att skapa unika ID:n för enheterna

  def __init__(self):
    self.id = Entity.id_counter  # Unikt ID för varje enhet
    Entity.id_counter += 1  # Öka ID-räknaren för nästa enhet
    self.components = {
    }  # En dictionary för att hålla komponenterna hos enheten

  # Metod för att lägga till en komponent till enheten
  def add_component(self, component):
    self.components[type(component)] = component

  # Metod för att hämta en komponent från enheten
  def get_component(self, component_type):
    return self.components.get(component_type, None)


# Komponent för att hantera position
class PositionComponent:

  def __init__(self, x, y):
    self.x = x  # X-koordinat för positionen
    self.y = y  # Y-koordinat för positionen


# Komponent för att hantera hastighet
class SpeedComponent:

  def __init__(self, speed):
    self.speed = speed  # Hastigheten
    self.x_speed = self.speed  # Hastighet i x-riktning
    self.y_speed = -self.speed  # Hastighet i y-riktning


# Komponent för att hantera rektangulär form
##
class RectComponent:

  def __init__(self, x, y, width, height):
    self.rect = Rect(x, y, width,
                     height)  # En rektangel med specificerade dimensioner


# Komponent för att hantera cirkulär form
class RadiusComponent:

  def __init__(self, radius):
    self.radius = radius  # Radien för cirkulär form


# Komponent för att hålla reda på vinnaren
class WinnerComponent:

  def __init__(self, winner=0):
    self.winner = winner  # Flagga för att hålla reda på vinnaren


# System för rörelsehantering
class MotionSystem:
  # Metod för att hantera spelarens rörelse
  def move_player(self, entity_player):
    rect = entity_player.get_component(
        RectComponent).rect  # Hämta rektangelkomponenten för spelaren
    speed = entity_player.get_component(
        SpeedComponent).speed  # Hämta hastighetskomponenten för spelaren
    key = pygame.key.get_pressed(
    )  # Hämta vilka tangentknappar som är nedtryckta
    # Om pil upp-tangenten är nedtryckt och spelarens överkant är inom synfältet, flytta spelaren uppåt
    if key[pygame.K_UP] and rect.top > margin:
      rect.y -= speed
    # Om pil ner-tangenten är nedtryckt och spelarens nederkant är inom synfältet, flytta spelaren nedåt
    if key[pygame.K_DOWN] and rect.bottom < screen_height:
      rect.y += speed

  # Metod för att hantera AI:ns rörelse
  def move_ai(self, entity_ball, entity_ai):
    rect_ai = entity_ai.get_component(
        RectComponent).rect  # Hämta rektangelkomponenten för AI:n
    speed_ai = entity_ai.get_component(
        SpeedComponent).speed  # Hämta hastighetskomponenten för AI:n
    rect_ball = entity_ball.get_component(
        RectComponent).rect  # Hämta rektangelkomponenten för bollen
    # Om bollens centrum är över AI:ns centrum och AI:ns botten är inom synfältet, flytta AI:n nedåt
    if rect_ai.centery < rect_ball.centery and rect_ai.bottom < screen_height:
      rect_ai.y += speed_ai
    # Om bollens centrum är under AI:ns centrum och AI:ns topp är inom synfältet, flytta AI:n uppåt
    if rect_ai.centery > rect_ball.centery and rect_ai.top > margin:
      rect_ai.y -= speed_ai

  # Metod för att hantera bollens rörelse
  def move_ball(self, entity_ball, entity_player, entity_ai):
    rect_ball = entity_ball.get_component(
        RectComponent).rect  # Hämta rektangelkomponenten för bollen
    speed_ball = entity_ball.get_component(
        SpeedComponent)  # Hämta hastighetskomponenten för bollen
    rect_player = entity_player.get_component(
        RectComponent).rect  # Hämta rektangelkomponenten för spelaren
    rect_ai = entity_ai.get_component(
        RectComponent).rect  # Hämta rektangelkomponenten för AI:n

    # Logik för bollens rörelse
    # Om bollens övre kant är över spelfältets överkant eller bollens nedre kant är under spelfältets nederkant, byt rörelseriktning i y-led
    if rect_ball.top <= margin or rect_ball.bottom >= screen_height:
      speed_ball.y_speed *= -1
    # Om bollen kolliderar med spelaren eller AI:n, byt rörelseriktning i x-led
    if rect_ball.colliderect(rect_player) or rect_ball.colliderect(rect_ai):
      speed_ball.x_speed *= -1
    # Uppdatera bollens position baserat på dess hastighet i x- och y-led
    rect_ball.x += speed_ball.x_speed
    rect_ball.y += speed_ball.y_speed

    # Logik för poänguppdatering
    # Om bollen når högerkanten av skärmen, öka motståndarens poäng
    if rect_ball.right >= screen_width:
      entity_ball.get_component(WinnerComponent).winner = 1
    # Om bollen når vänsterkanten av skärmen, öka spelarens poäng
    elif rect_ball.left <= 0:
      entity_ball.get_component(WinnerComponent).winner = -1


# System för rendering av spelobjekt
class RenderingSystem:
  # Metod för att rita ut spelarens paddel på skärmen
  def draw_paddle(self, entity):
    rect = entity.get_component(
        RectComponent).rect  # Hämta rektangelkomponenten för enheten
    # Rita en rektangel på skärmen med spelarens paddelposition och dimensioner
    pygame.draw.rect(screen, white, rect)

  # Metod för att rita ut bollen på skärmen
  def draw_ball(self, entity):
    ball_radius = entity.get_component(
        RadiusComponent).radius  # Hämta radien för bollen
    rect = entity.get_component(
        RectComponent).rect  # Hämta rektangelkomponenten för bollen
    # Rita en cirkel på skärmen med bollens position och radien
    pygame.draw.circle(screen, white, rect.center, ball_radius)


# Skapa instanser av spelentiteter
entity_player = Entity()  # Skapa en instans för spelaren
entity_ai = Entity()  # Skapa en instans för AI:n
entity_ball = Entity()  # Skapa en instans för bollen

# Lägg till komponenter till spelentiteterna
entity_player.add_component(
    PositionComponent(screen_width - 40, screen_height //
                      2))  # Lägg till positionskomponent för spelaren
entity_player.add_component(
    SpeedComponent(5))  # Lägg till hastighetskomponent för spelaren
entity_player.add_component(
    RectComponent(screen_width - 40, screen_height // 2, 20,
                  100))  # Lägg till rektangelkomponent för spelaren

entity_ai.add_component(PositionComponent(
    20, screen_height // 2))  # Lägg till positionskomponent för AI:n
entity_ai.add_component(
    SpeedComponent(5))  # Lägg till hastighetskomponent för AI:n
entity_ai.add_component(RectComponent(
    20, screen_height // 2, 20, 100))  # Lägg till rektangelkomponent för AI:n

entity_ball.add_component(
    PositionComponent(screen_width // 2, screen_height //
                      2))  # Lägg till positionskomponent för bollen
entity_ball.add_component(
    SpeedComponent(4))  # Lägg till hastighetskomponent för bollen
entity_ball.add_component(
    RadiusComponent(8))  # Lägg till radienkomponent för bollen
entity_ball.add_component(
    RectComponent(screen_width // 2, screen_height // 2, 16,
                  16))  # Lägg till rektangelkomponent för bollen
entity_ball.add_component(
    WinnerComponent())  # Lägg till vinnarkomponent för bollen

# Huvudspel-loop
run = True
while run:
  fpsClock.tick(fps)  # Håll uppdateringshastigheten till fps-värdet

  draw_board()  # Rita spelplanen på skärmen
  draw_text(f'CPU: {cpu_score}', font, white, 20,
            15)  # Rita motståndarens poäng på skärmen
  draw_text(f'P1: {player_score}', font, white, screen_width - 100,
            15)  # Rita spelarens poäng på skärmen

  RenderingSystem().draw_paddle(
      entity_player)  # Rita ut spelarens paddel på skärmen
  RenderingSystem().draw_paddle(entity_ai)  # Rita ut AI:ns paddel på skärmen

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

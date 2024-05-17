screen_width = 600  # Bredden på spelbildskärmen
screen_height = 500  # Höjden på spelbildskärmen

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

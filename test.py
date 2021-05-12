#Importieren u. initialisieren der Pygame-Bibliothek
import pygame
from pygame.locals import *
pygame.init()

# Variablen/KONSTANTEN setzen
W, H = 800, 600
FPS  = 60
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)
programIcon = pygame.image.load('img/icon.jpg')
myfont = pygame.font.SysFont('Comic Sans MS', 30)

pygame.display.set_icon(programIcon)

# Definieren und Öffnen eines neuen Fensters
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mastermind")
clock = pygame.time.Clock()

# Schleife Hauptprogramm
while True:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        # Beenden bei [ESC] oder [X]
        if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            pygame.quit()

    # Spiellogik

    # Spielfeld löschen
    screen.fill(WEISS)

    # Spielfeld/figuren zeichnen
    textsurface = myfont.render('Mastermind', False, (0, 0, 0))
    screen.blit(textsurface,(350,0))
    pygame.draw.rect(screen, SCHWARZ, [10, 20, 100, 100], 1)
    pygame.draw.rect(screen, SCHWARZ, [10, 20, 100, 100], 1)
    pygame.draw.rect(screen, SCHWARZ, [10, 20, 100, 100], 1)
    pygame.draw.rect(screen, SCHWARZ, [10, 20, 100, 100], 1)

    # Fenster aktualisieren
    pygame.display.flip()
    clock.tick(FPS)
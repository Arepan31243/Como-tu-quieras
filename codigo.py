import pygame
import sys

# Disfruta del Pong clásico. 
# Mueve tu paleta para golpear la bola, evita que pase de tu lado y anota puntos contra la máquina o contra un amigo. 
# Ideal para partidas rápidas.

pygame.init()

ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego basiquisimo de pong kjhasdkjlasjkasd")

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

reloj = pygame.time.Clock()
FPS = 60

PALETA_ANCHO = 15
PALETA_ALTO = 90

paleta_jugador1 = pygame.Rect(50, ALTO // 2 - PALETA_ALTO // 2, PALETA_ANCHO, PALETA_ALTO)
paleta_jugador2 = pygame.Rect(ANCHO - 50 - PALETA_ANCHO, ALTO // 2 - PALETA_ALTO // 2, PALETA_ANCHO, PALETA_ALTO)

PELOTA_RADIO = 10
pelota = pygame.Rect(ANCHO // 2 - PELOTA_RADIO, ALTO // 2 - PELOTA_RADIO, PELOTA_RADIO * 2, PELOTA_RADIO * 2)

velocidad_paletas = 6
velocidad_pelota_x = 5
velocidad_pelota_y = 5

jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_w] and paleta_jugador1.top > 0:
        paleta_jugador1.y -= velocidad_paletas
    if teclas[pygame.K_s] and paleta_jugador1.bottom < ALTO:
        paleta_jugador1.y += velocidad_paletas

    if teclas[pygame.K_UP] and paleta_jugador2.top > 0:
        paleta_jugador2.y -= velocidad_paletas
    if teclas[pygame.K_DOWN] and paleta_jugador2.bottom < ALTO:
        paleta_jugador2.y += velocidad_paletas

    pelota.x += velocidad_pelota_x
    pelota.y += velocidad_pelota_y

    if pelota.top <= 0 or pelota.bottom >= ALTO:
        velocidad_pelota_y *= -1

    if pelota.colliderect(paleta_jugador1) or pelota.colliderect(paleta_jugador2):
        velocidad_pelota_x *= -1

    if pelota.left <= 0 or pelota.right >= ANCHO:
        pelota.center = (ANCHO // 2, ALTO // 2)
        velocidad_pelota_x *= -1

    ventana.fill(NEGRO)

    pygame.draw.aaline(ventana, BLANCO, (ANCHO // 2, 0), (ANCHO // 2, ALTO))

    pygame.draw.rect(ventana, BLANCO, paleta_jugador1)
    pygame.draw.rect(ventana, BLANCO, paleta_jugador2)
    pygame.draw.ellipse(ventana, BLANCO, pelota)

    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()
sys.exit()

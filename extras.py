import random
import pygame
from pygame.locals import *
from configuracion import *


def dameLetraApretada(key):
    if K_0 <= key and key <= K_9:
        return str(key - K_0)
    else:
        return ""


def dibujar(screen, productos_en_pantalla, producto_principal, producto_candidato, puntos, segundos):

    defaultFont = pygame.font.Font(pygame.font.get_default_font(), 20)
    defaultFontGrande = pygame.font.Font(pygame.font.get_default_font(), 17)
    defaultFontPregunta = pygame.font.Font(pygame.font.get_default_font(), 25)

    # Fondo
    background = pygame.image.load("img/fondo.png").convert()
    screen.blit(background, [0,0])
    
    ren1 = defaultFont.render(producto_candidato, 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    if (segundos < 15):
        ren3 = defaultFont.render(
            "Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren3 = defaultFont.render(
            "Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
        
   # Dibujar los nombres de los productos 
    x_pos = 115
    y_pos = ALTO - (ALTO-285)
    espacio_vertical = 93  # Espacio vertical entre filas
    espacio_horizontal = 360  # Espacio horizontal entre columnas

    # Contadores para controlar el posicionamiento
    fila_actual = 0
    columna_actual = 0

    # Dibujar la pregunta y el producto
    screen.blit(defaultFontPregunta.render("Producto con precio similar a:", 1, COLOR_LETRAS), (200, 110))
    screen.blit(defaultFontPregunta.render(producto_principal[0], 1, COLOR_LETRAS), (220, 150))

    # Dibujar los nombres de los productos en tres filas verticales
    for producto in productos_en_pantalla:
        nombre_en_pantalla = producto[0] + producto[1]

        if producto[0] == producto_principal[0] and producto[1] == producto_principal[1]:
            screen.blit(defaultFontGrande.render(nombre_en_pantalla,
                        1, COLOR_TIEMPO_FINAL), (x_pos + columna_actual * espacio_horizontal, y_pos + fila_actual * espacio_vertical))
        else:
            screen.blit(defaultFontGrande.render(
                nombre_en_pantalla, 1, COLOR_LETRAS), (x_pos + columna_actual * espacio_horizontal, y_pos + fila_actual * espacio_vertical))
        
        columna_actual += 1
        if columna_actual >= 2:
            columna_actual = 0
            fila_actual += 1

    screen.blit(ren1, (190, 570))
    screen.blit(ren2, (600, 10))
    screen.blit(ren3, (10, 10))


def cargar_musica():
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.load("./sounds/musica.mp3")
    pygame.mixer.music.play(-1)


#def cargar_sonidos(e):
#    sonido_clic = pygame.mixer.Sound("./sounds/moneda.mp3")
#    sonido_clic.set_volume(0.5)
#    if e.type == MOUSEBUTTONDOWN:
#        sonido_clic.play()

def sonido_correcto():
    sonido_clic = pygame.mixer.Sound("./sounds/moneda.mp3")
    sonido_clic.set_volume(0.5)
    sonido_clic.play()

def sonido_incorrecto():
    sonido_clic = pygame.mixer.Sound("./sounds/error.mp3")
    sonido_clic.set_volume(1)
    sonido_clic.play()

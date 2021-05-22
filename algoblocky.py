import pygame
import math
import logging

logging.basicConfig(level=logging.DEBUG)

#
# Init Pygame
#

pygame.init()
clock = pygame.time.Clock()

screen_width  = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('__ ALGO BLOCKY __')

#
# Couleurs et directions
#

class colors:
    RED    = ( 255, 0, 0 )
    GREEN  = ( 0, 255, 0 )
    BLUE   = ( 0, 0, 255 )
    ORANGE = ( 255, 136, 0 )
    YELLOW = ( 255, 255, 0 )
    CYAN   = ( 0, 255, 0 )
    VIOLET = ( 136, 0, 255 )
    FUCSHIA= ( 136, 0, 255 )
    WHITE  = ( 255, 255, 255 )
    GREY   = ( 136, 136, 136 )
    BLACK  = ( 0, 0, 0 )

class directions:
    RIGHT = 90
    UP    = 180
    LEFT  = 270
    DOWN  = 0

#
# Init écran
#

screen.fill(colors.BLACK)

#
# Stylo
#

class Pen:
    
    def __init__(self):
        self.color = colors.WHITE
        self.width = 3
        self.angle = directions.RIGHT
        self.position = [ screen_width//2, screen_height//2 ]
        self.is_down = True

pen = Pen()

#
# Fonctions
#

#
# Mettre à jour l'écran.
#

def screen_update():
    pygame.display.update()

#
# Faire avancer le stylo.
#

def avancer(length):
    
    dest_x = pen.position[0] + math.sin(math.radians(pen.angle)) * length
    dest_y = pen.position[1] + math.cos(math.radians(pen.angle)) * length

    logging.debug(f" > draw a line with length {length} from {pen.position} to ({dest_x}, {dest_y})")

    if pen.is_down:
        pygame.draw.line(screen,
                     pen.color,
                     pen.position,
                     [ dest_x, dest_y ],
                     pen.width)

    # Mettre à jour la position du crayon
    pen.position = [ dest_x, dest_y ]

    screen_update()

#
# Changer la couleur du stylo.
#

def couleur(couleur):
    pen.color = couleur

#
# Changer l'orientation du stylo
#

def orienter(direction):
    pen.angle = direction

#
# Déssiner un point
#

def point(width):
    pygame.draw.circle(screen, pen.color, pen.position, width)

#
# Lever/poser le stylo
#

def lever_stylo():
    pen.is_down=False

def poser_stylo():
    pen.is_down=True

#
# Garder l'écran ouvert.
#

def loop_forever():

    screen_update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
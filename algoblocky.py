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
    RED = ( 255, 0, 0 )
    GREEN = ( 0, 255, 0 )
    BLUE = ( 0, 0, 255 )
    ORANGE = ( 255, 136, 0 )
    YELLOW = ( 255, 255, 0 )
    CYAN = ( 0, 255, 0 )
    VIOLET = ( 136, 0, 255 )
    FUCSHIA = ( 136, 0, 255 )
    WHITE = ( 255, 255, 255 )
    GREY = ( 136, 136, 136 )
    BLACK = ( 0, 0, 0 )

class directions:
    RIGHT = -90
    UP = -180
    LEFT = -270
    DOWN = 0

#
# Init écran
#

screen.fill(colors.BLACK)

#
# Stylo
#

pen_color = colors.WHITE
pen_width = 3
pen_angle = directions.RIGHT
pen_position = [ screen_width//2, screen_height//2 ]
pen_down = True

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
    
    global pen_position

    dest_x = pen_position[0] + math.sin(math.radians(pen_angle * -1)) * length
    dest_y = pen_position[1] + math.cos(math.radians(pen_angle * -1)) * length

    logging.debug(f" > draw a line with length {length} from {pen_position} to ({dest_x}, {dest_y})")

    if pen_down:
        pygame.draw.line(screen,
                     pen_color,
                     pen_position,
                     [ dest_x, dest_y ],
                     pen_width)

    # Mettre à jour la position du crayon
    pen_position = [ dest_x, dest_y ]

    screen_update()

#
# Changer la couleur du stylo.
#

def couleur(couleur):
    
    global pen_color
    pen_color = couleur

#
# Changer l'orientation du stylo
#

def orienter(direction):
    global pen_angle
    pen_angle = direction

#
# Désinner un point
#

def point(width):
    pygame.draw.circle(screen, pen_color, pen_position, width)

#
# Garder l'écran ouvert.
#

def loop_forever():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
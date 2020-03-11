# ##### TODO #####
# floor obj
# ball obj
# ball gravity
# collision with floor
# drawBall func
# drawFloor func
# launchBall(v_0, theta) func

import pygame as pg
from pygame.locals import *
import time
from datetime import datetime
from datetime import timedelta
import random
import pygame.font as font
import math

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 420
BACKGROUND_COLOR = 200, 200, 200

GAMEBOARD_COLOR = 0, 0, 0
OBJ_COLOR = 200, 0, 0
FLOOR_COLOR = 204, 174, 98
FLOOR_HEIGHT = 50

GRAVITY = 0.4

# initial statement
v_0 = 12
theta = 45

rad = math.radians(theta)
v_x0 = v_0*math.cos(rad)
v_y0 = -v_0*math.sin(rad)


class Object:
    color = OBJ_COLOR
    radius = 20
    velocity = [v_x0, v_y0]

    def __init__(self):
        self.x = self.radius
        self.y = SCREEN_HEIGHT-FLOOR_HEIGHT-self.radius-1
        # self.y = self.radius

    def movement(self):
        if self.y < SCREEN_HEIGHT-FLOOR_HEIGHT-self.radius:
            self.y += self.velocity[1]
            self.x += self.velocity[0]
        else:
            self.y = SCREEN_HEIGHT-FLOOR_HEIGHT-self.radius  # collision
            # self.velocity[1] *= -1

    def draw(self):
        pg.draw.circle(screen, self.color,
                       (int(self.x), int(self.y)), self.radius)


class Floor:
    color = FLOOR_COLOR

    def __init__(self):
        pass

    def draw(self):
        pg.draw.rect(screen, self.color, (0, SCREEN_HEIGHT -
                                          FLOOR_HEIGHT, SCREEN_WIDTH, FLOOR_HEIGHT))


class GameBoard:
    width = 20
    height = 20

    def __init__(self):
        self.object = Object()
        self.floor = Floor()

    def draw(self, screen):
        self.floor.draw()
        self.object.draw()


class SnakeExcessiveException(Exception):  # exception for clear
    pass


class SnakeCollisionException(Exception):  # exception for collision
    pass


# initialize
pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_board = GameBoard()
FONT = pg.font.Font(None, 24)
clock = pg.time.Clock()


def draw_background(screen):
    rect = pg.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.draw.rect(screen, BACKGROUND_COLOR, rect)


while True:
    events = pg.event.get()

    font = pg.font.Font(None, 30)
    for event in events:
        if event.type == pg.QUIT:  # quit
            exit()

    game_board.object.velocity[0]
    game_board.object.velocity[1] += GRAVITY  # gravity
    game_board.object.movement()

    draw_background(screen)
    game_board.draw(screen)
    pg.display.flip()  # update
    clock.tick(60)

pg.quit()

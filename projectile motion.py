# ##### TODO #####
# v floor obj
# v ball obj
# v ball gravity
# v collision with floor
# v drawBall func
# v drawFloor func
# v launchBall(v_0, theta) func
# x launch button v_0 & theta input box
# v mark while flying
# v show legend of each motion(degree, v_0) (all color different)

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
BACKGROUND_COLOR = (206, 214, 224)

GAMEBOARD_COLOR = 0, 0, 0
OBJ_COLOR = 200, 0, 0
FLOOR_COLOR = 204, 174, 98
FLOOR_HEIGHT = 50

RED = (238, 82, 83)
GREEN = (16, 172, 132)
BLUE = (10, 189, 227)

TURN_INTERVAL = timedelta(seconds=0.1)  # trace mark interval
GRAVITY = 0.4

# initial statement
v_0 = 15
theta1 = 30
theta2 = 45
theta3 = 60

rad1 = math.radians(theta1)
v_x01 = v_0*math.cos(rad1)
v_y01 = -v_0*math.sin(rad1)
rad2 = math.radians(theta2)
v_x02 = v_0*math.cos(rad2)
v_y02 = -v_0*math.sin(rad2)
rad3 = math.radians(theta3)
v_x03 = v_0*math.cos(rad3)
v_y03 = -v_0*math.sin(rad3)


class GameBoard:
    width = 20
    height = 20

    def __init__(self):
        self.object1 = Object([v_x01, v_y01], RED)
        self.object2 = Object([v_x02, v_y02], GREEN)
        self.object3 = Object([v_x03, v_y03], BLUE)
        self.floor = Floor()

    def draw(self, screen):
        self.floor.draw()
        self.object1.draw()
        self.object2.draw()
        self.object3.draw()


class Floor:
    color = FLOOR_COLOR

    def __init__(self):
        pass

    def draw(self):
        pg.draw.rect(screen, self.color, (0, SCREEN_HEIGHT -
                                          FLOOR_HEIGHT, SCREEN_WIDTH, FLOOR_HEIGHT))


class Object:
    color = OBJ_COLOR
    radius = 20
    velocity = [0, 0]
    num = 0
    trace = []

    def __init__(self, velocity, color):
        self.velocity = velocity
        self.x = self.radius
        self.y = SCREEN_HEIGHT-FLOOR_HEIGHT-self.radius-1
        self.color = color
        self.createMark(color)
        # self.y = self.radius

    def movement(self):
        if self.y < SCREEN_HEIGHT-FLOOR_HEIGHT-self.radius:
            self.y += self.velocity[1]
            self.x += self.velocity[0]
        else:
            self.y = SCREEN_HEIGHT-FLOOR_HEIGHT-self.radius  # collision
            # self.velocity[1] *= -1

    def createMark(self, color):
        if self.y < SCREEN_HEIGHT-FLOOR_HEIGHT-self.radius:
            new = Trace(self.x, self.y, color)
            self.trace.append(new)

    def draw(self):
        for each in self.trace:
            each.draw()
        pg.draw.circle(screen, self.color,
                       (int(self.x), int(self.y)), self.radius)


class Trace:
    color = OBJ_COLOR
    radius = 4
    x = 0
    y = 0

    def __init__(self, x, y, color):
        self.color = color
        self.x = x
        self.y = y

    def draw(self):
        pg.draw.circle(screen, self.color,
                       (int(self.x), int(self.y)), self.radius)


class SnakeExcessiveException(Exception):  # exception for clear
    pass


class SnakeCollisionException(Exception):  # exception for collision
    pass


# initialize
pg.init()
pg.display.set_caption("physics  simulator")
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_board = GameBoard()
FONT = pg.font.Font(None, 32)
last_turn_time = datetime.now()
clock = pg.time.Clock()


def draw_background(screen):
    rect = pg.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.draw.rect(screen, BACKGROUND_COLOR, rect)


def display_text(screen, text, x, y):
    text = FONT.render(text, True, (0, 0, 0))
    screen.blit(text, (x, y))


while True:
    events = pg.event.get()

    font = pg.font.Font(None, 30)
    for event in events:
        if event.type == pg.QUIT:  # quit
            exit()

    if TURN_INTERVAL < datetime.now() - last_turn_time:  # each interval
        game_board.object1.createMark(RED)
        game_board.object2.createMark(GREEN)
        game_board.object3.createMark(BLUE)
        last_turn_time = datetime.now()
        # print(game_board.object1.y, game_board.object2.y, game_board.object3.y) # check height
        # print(game_board.object1.velocity[0], game_board.object2.velocity[0], game_board.object3.velocity[0])  # check height

    game_board.object1.velocity[1] += GRAVITY  # gravity
    game_board.object2.velocity[1] += GRAVITY  # gravity
    game_board.object3.velocity[1] += GRAVITY  # gravity
    game_board.object1.movement()
    game_board.object2.movement()
    game_board.object3.movement()

    draw_background(screen)
    game_board.draw(screen)
    text = "v: %d   degree: red: %d, green: %d, blue: %d" % (
        v_0, theta1, theta2, theta3)
    display_text(screen, text, 12, 12)
    pg.display.flip()  # update
    clock.tick(60)

pg.quit()

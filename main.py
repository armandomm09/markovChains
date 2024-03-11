from enum import Enum

from gridworld.grid import Grid
import pygame
import random


while True:
    print("\n Juego 1: \n En todas las casillas tiene 25% de ir a cualquier lado ")
    print("\n Juego 2: \n Las casillas tienen una probabilidad especifica de movimiento \n")
    numeroDeJuego = int(input("Ingresa el numero de juego que quieres jugar "))
    if (numeroDeJuego == 1 or numeroDeJuego == 2): break

maxX = 4
maxY = 3
x = 1
y = 2

grid = Grid(maxX, maxY, 90, 90, title='Tic Tac Toe', margin=1, framerate=2)

"""grid[0, 0] = 'O'
grid[1, 1] = 'X'
grid[2, 1] = 'O'
grid[2, 2] = 'X'"""

"""def key_action(key):

    global x, y
    oldx, oldy = x, y
    if key == pygame.K_LEFT and x > 0:
        x = x - 1
    if key == pygame.K_RIGHT and x < maxX-1:
        x += 1

    if key == pygame.K_DOWN and y < maxy-1:
        y += 1
    if key == pygame.K_UP and y > 0:
        y -= 1
    grid[oldx, oldy] = ''
    grid[x, y] = 'O'

grid.set_key_action(key_action)"""


class Dir(Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'


transJuego1 = {
    (0, 1): {Dir.UP: 0.25, Dir.DOWN: 0.25, Dir.LEFT: 0.25, Dir.RIGHT: 0.25},
    (0, 2): {Dir.UP: 0.25, Dir.DOWN: 0.25, Dir.LEFT: 0.25, Dir.RIGHT: 0.25},
    (1, 0): {Dir.UP: 0.25, Dir.DOWN: 0.25, Dir.LEFT: 0.25, Dir.RIGHT: 0.25},
    (1, 1): {Dir.UP: 0.25, Dir.DOWN: 0.25, Dir.LEFT: 0.25, Dir.RIGHT: 0.25},
    (1, 2): {Dir.UP: 0.25, Dir.DOWN: 0.25, Dir.LEFT: 0.25, Dir.RIGHT: 0.25},
    (2, 0): {Dir.UP: 0.25, Dir.DOWN: 0.25, Dir.LEFT: 0.25, Dir.RIGHT: 0.25},
    (2, 1): {Dir.UP: 0.25, Dir.DOWN: 0.25, Dir.LEFT: 0.25, Dir.RIGHT: 0.25},
    (2, 2): {Dir.UP: 0.25, Dir.DOWN: 0.25, Dir.LEFT: 0.25, Dir.RIGHT: 0.25},
    (3, 0): {Dir.UP: 0.25, Dir.DOWN: 0.25, Dir.LEFT: 0.25, Dir.RIGHT: 0.25},
    (3, 2): {Dir.UP: 0.25, Dir.DOWN: 0.25, Dir.LEFT: 0.25, Dir.RIGHT: 0.25},
}
transJuego2 = {
    (0, 1): {Dir.UP: 1.0, Dir.DOWN: 0.0, Dir.LEFT: 0.0, Dir.RIGHT: 0.0},
    (0, 2): {Dir.UP: 1.0, Dir.DOWN: 0.0, Dir.LEFT: 0.0, Dir.RIGHT: 0.0},
    (1, 0): {Dir.UP: 0, Dir.DOWN: 0.0, Dir.LEFT: 1, Dir.RIGHT: 0},
    (1, 1): {Dir.UP: 0.33, Dir.DOWN: 0.0, Dir.LEFT: 0.34, Dir.RIGHT: 0.33},
    (1, 2): {Dir.UP: 0.33, Dir.DOWN: 0.0, Dir.LEFT: 0.34, Dir.RIGHT: 0.33},
    (2, 0): {Dir.UP: 0, Dir.DOWN: 0.33, Dir.LEFT: 0.34, Dir.RIGHT: 0.33},
    (2, 1): {Dir.UP: 0.0, Dir.DOWN: 0.0, Dir.LEFT: 0.0, Dir.RIGHT: 1.0},
    (2, 2): {Dir.UP: 0.5, Dir.DOWN: 0.0, Dir.LEFT: 0.0, Dir.RIGHT: 0.5},
    (3, 0): {Dir.UP: 0.0, Dir.DOWN: 1.0, Dir.LEFT: 0.0, Dir.RIGHT: 0.0},
    (3, 2): {Dir.UP: 1.0, Dir.DOWN: 0.0, Dir.LEFT: 0.0, Dir.RIGHT: 0.0},
}

trans = {}

if numeroDeJuego == 1:
    trans = transJuego1
else:
    trans = transJuego2


def tick():
    global x, y
    oldx, oldy = x, y

    current_probs = trans[(x, y)]
    value = random.random()

    if value < current_probs[Dir.UP]:
        if y > 0:
            y -= 1
    elif value < current_probs[Dir.UP] + current_probs[Dir.DOWN]:
        if y < maxY - 1:
            y += 1
    elif value < current_probs[Dir.UP] + current_probs[Dir.DOWN] + current_probs[Dir.LEFT]:
        if x > 0:
            x -= 1
    else:
        if x < maxX - 1:
            x += 1

    grid[oldx, oldy] = ''
    grid[x, y] = '@'

    if (x, y) == (0, 0) or (x, y) == (3, 1):
        print("¡El juego ha terminado!")
        pygame.quit()
        exit()


grid.set_timer_action(tick)

grid.run()

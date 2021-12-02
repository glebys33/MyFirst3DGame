import math


# настройки игры
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH / 2
HALF_HEIGHT = HEIGHT / 2
FPS = 60
TILE = 100

# лучи для 3D
FOV = math.pi / 3
HALF_FOV = FOV / 2
N_RAYS = 120
MAX_DEPHH = 800
DELTA_ANGLE = FOV / N_RAYS
DIST = N_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // N_RAYS

# настройки игрока
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 3

# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (125, 125, 125)
BROWN = (121, 77, 24)
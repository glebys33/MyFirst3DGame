import math


# настройки игры
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH / 2
HALF_HEIGHT = HEIGHT / 2
FPS = 60
TILE = 100
FPS_POS = (WIDTH - 65, 5)

# лучи для 3D
FOV = math.pi / 3
HALF_FOV = FOV / 2
N_RAYS = 300
MAX_DEPHH = 800
DELTA_ANGLE = FOV / N_RAYS
DIST = N_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = DIST * TILE
SCALE = WIDTH // N_RAYS

# Миникарта
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE

# настройки игрока
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 2

# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (125, 125, 125)
BROWN = (121, 77, 24)
SKYBLUE = (34, 113, 179)
YELOW = (255, 255, 0)
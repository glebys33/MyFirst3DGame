import pygame
import math
from config import *
from map import world_map


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        # Предвижение игрока
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
        if keys[pygame.K_a]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
        if keys[pygame.K_d]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02


# Отрисовка всего
class Drawing:
    def __init__(self, screen, screen_map):
        self.screen = screen
        self.screen_map = screen_map
        self.font = pygame.font.SysFont("Arial", 36, bold=True)

    def background(self):
        # Отрисовка неба и земли
        pygame.draw.rect(self.screen, SKYBLUE, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.screen, BROWN, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, player_pos, player_angle):
        # Отрисовка стен
        ray_castion(self.screen, player_pos, player_angle)

    def fps(self, clock):
        # Вывод fps
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.screen.blit(render, FPS_POS)


def squareangle(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE


# Функция каторая отрисовавает стены
def ray_castion(screen, player_pos, player_angle):
    ox, oy = player_pos
    xm, ym = squareangle(ox, oy)
    cur_angle = player_angle - HALF_FOV
    for ray in range(N_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        # Алгоритм для вертикалий
        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WIDTH, TILE):
            depth_v = (x - ox) / cos_a
            y = oy + depth_v * sin_a
            if squareangle(x + dx, y) in world_map:
                break
            x += dx * TILE
        # Алгоритм для горизонталий
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, HEIGHT, TILE):
            depth_h = (y - oy) / sin_a
            x = ox + depth_h * cos_a
            if squareangle(x, y + dy) in world_map:
                break
            y += dy * TILE

        # Выбор точки пересечения
        depth = depth_v if depth_v < depth_h else depth_h
        depth *= math.cos(player_angle - cur_angle)
        proj_height = PROJ_COEFF / depth
        c = 255 / (1 + depth * depth * 0.0001)
        color = (c, c//2, c//3)
        pygame.draw.rect(screen, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
        cur_angle += DELTA_ANGLE


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
    clock = pygame.time.Clock()
    player = Player()
    drawer = Drawing(screen, screen_map)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        player.movement()
        screen.fill(BLACK)

        drawer.background()
        drawer.world(player.pos, player.angle)
        drawer.fps(clock)
        drawer.mini_map(player)

        pygame.display.flip()
        clock.tick()
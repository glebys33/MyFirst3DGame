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


def ray_castion(screen, player_pos, player_angle):
    cur_angle = player_angle - HALF_FOV
    xo, yo = player_pos
    for ray in range(N_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(MAX_DEPHH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            # pygame.draw.line(screen, GRAY, player_pos, (x, y), 2)
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                depth *= math.cos(player_angle - cur_angle)
                proj_height = PROJ_COEFF / depth
                c = 255 / (1 + depth * depth * 0.0001)
                color = (c, c, c)
                pygame.draw.rect(screen, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                break
        cur_angle += DELTA_ANGLE


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    player = Player()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        player.movement()
        screen.fill(BLACK)

        ray_castion(screen, player.pos, player.angle)

        #pygame.draw.circle(screen, GREEN, player.pos, 12)
        #pygame.draw.line(screen, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
        #                                             player.y + WIDTH * math.sin(player.angle)))
        #for x,y in world_map:
        #    pygame.draw.rect(screen, GRAY, (x, y, TILE, TILE), 2)

        pygame.display.flip()
        clock.tick(FPS)
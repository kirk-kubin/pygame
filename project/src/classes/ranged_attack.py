import pygame as pg
from pygame.sprite import Sprite

ranged_image = pg.image.load("project/images/bullet/bullet.png")
ranged_image = pg.transform.scale(ranged_image, (ranged_image.get_width() + 23.333, ranged_image.get_height() + 10))


class Ranged_attack(Sprite):
    def __init__(self, player, keys):
        super().__init__()
        self.image = ranged_image
        self.rect = self.image.get_rect()

        # Initialize position based on player's position
        self.pos_x = player.rect.right - 40
        self.pos_y = player.rect.centery - 45
        self.alt_speed = 3
        self.initial_x = self.pos_x  # Store the initial x-coordinate where the bullet was fired
        self.player_controlled_distance = 50  # Number of pixels the player can control the bullet
        self.speed = 10
        self.player_controlled = True  # Flag to indicate if the player can control the bullet
        self.keys = keys

    def update(self):
        if self.player_controlled:
            if (self.keys[pg.K_w] or self.keys[pg.K_s]) and (self.keys[pg.K_d] or self.keys[pg.K_a]):
                self.alt_speed = 2
            if self.keys[pg.K_w]:
                self.pos_y -= self.alt_speed
            if self.keys[pg.K_a]:
                self.pos_x -= self.alt_speed
            if self.keys[pg.K_d]:
                self.pos_x += self.alt_speed
            if self.keys[pg.K_s]:
                self.pos_y += self.alt_speed

            # Disable player control once the bullet has traveled the specified distance
            if abs(self.pos_x - self.initial_x) >= self.player_controlled_distance:
                self.player_controlled = False

        self.pos_x += self.speed

        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
import pygame as pg
from pygame.sprite import Sprite
from pygame.sprite import Group

bullets = Group()
bullet_image = pg.image.load("project/images/enemies/projectiles/bullet.png")
bullet_image = pg.transform.scale(bullet_image, (bullet_image.get_width() + 25, bullet_image.get_height() + 12.5))

class Gunner_attack(Sprite):
    def __init__(self, gunner):
        super().__init__()
        self.pos_x = gunner.rect.right - 250
        self.pos_y = gunner.rect.centery - 40
        self.image = bullet_image
        self.rect = self.image.get_rect()

        self.screen_width = 960
        self.screen_height = 540
        self.speed = 5

        bullets.add(self)  # Add the bullet to the bullets_group

    def update(self):
        self.pos_x -= self.speed
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

        if self.rect.x < -self.screen_width:
            self.kill()

bomb_image = pg.image.load("project/images/enemies/projectiles/bomb.png")
bomb_image = pg.transform.scale(bomb_image, (bomb_image.get_width() + 20, bomb_image.get_height() + 40))

class Bomber_attack(Sprite):
    def __init__(self, bomber):
        super().__init__()
        self.pos_x = bomber.rect.right - 160
        self.pos_y = bomber.rect.centery - 40
        self.image = bomb_image
        self.rect = self.image.get_rect()

        self.screen_width = 960
        self.screen_height = 540
        self.speed = 5

        bullets.add(self)  # Add the bullet to the bullets_group

    def update(self):
        self.pos_x -= 0.25
        self.pos_y += self.speed
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

        if self.rect.y > self.screen_height + 100:
            self.kill()
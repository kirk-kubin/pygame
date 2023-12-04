import pygame as pg
from pygame.sprite import Sprite
from resources import *

flash_image, flash_image1, flash_image2, flash_image3, flash_image4, flash_image5 = load_flash_images()

class Flash(Sprite):
    def __init__(self, player):
        super().__init__()
        self.current_frame = 0
        self.last_update = 0
        self.image = flash_image
        self.rect = self.image.get_rect()
        self.player = player
        self.counter = 0
        self.flash_frames = [
            flash_image, flash_image1, flash_image2, flash_image3, flash_image4, flash_image5
        ]

    def update(self):
        self.animate()

        self.pos_x = self.player.rect.right + 45
        self.pos_y = self.player.rect.centery - 38
        self.rect.center = (self.pos_x, self.pos_y)

    def animate(self):
        now = pg.time.get_ticks()

        if now - self.last_update > 35:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.flash_frames)
            self.image = self.flash_frames[self.current_frame]
            self.rect = self.image.get_rect()
            self.counter += 1
            if self.counter == 6:
                self.kill()
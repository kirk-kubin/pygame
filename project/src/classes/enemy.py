import pygame as pg
import random
from pygame.sprite import Sprite
from classes.enemy_attacks import *
from resources import load_gunner_images
from resources import load_bomber_images

class Gunner(Sprite):
    def __init__(self,hp,all_sprites,gunner_bullets_group):
        super().__init__()
        idle_image,idle_image1,idle_image2,idle_image3,shooting_image,shooting_image1,shooting_image2,shooting_image3,death_image,death_image1,death_image2,death_image3 = load_gunner_images()
        self.screen_width = 960
        self.screen_height = 540
        self.attack_cooldown = 2000
        self.last_attack_time = 0
        self.down = True
        self.up = False
        self.pos_x = self.screen_width + 100
        self.pos_y = random.randint(100,self.screen_height - 100)
        self.speed = 3
        self.all_sprites = all_sprites
        self.gunner_bullets_group = gunner_bullets_group
        self.hp = hp
        self.current_frame = 0
        self.last_update = 0
        self.death_counter = 0

        self.idle = True
        self.shooting = False
        self.death = False

        self.idle_frames = [
            idle_image,idle_image1,idle_image2,idle_image3
        ]
        self.shooting_frames = [
            shooting_image,shooting_image1,shooting_image2,shooting_image3
        ]
        self.death_frames = [
            death_image,death_image1,death_image2,death_image3
        ]

        self.image = self.idle_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)

    def update(self):
        self.animate()

        if self.hp <= 0:
            self.death = True
        if self.death:
            self.idle = False
            self.shooting = False

        if self.idle:
            self.pos_x -= self.speed
            self.rect.center = (self.pos_x,self.pos_y)
        if self.pos_x <= self.screen_width - 200:
            self.shooting = True
            self.idle = False
        if self.shooting:
            self.attack()
            self.speed = 1
            if self.down:
                self.pos_y += self.speed
                self.rect.center = (self.pos_x,self.pos_y)
                if self.pos_y >= self.screen_height - 100:
                    self.up = True
                    self.down = False
            if self.up:
                self.pos_y -= self.speed
                self.rect.center = (self.pos_x,self.pos_y)
                if self.pos_y <= 100:
                    self.down = True
                    self.up = False

    def animate(self):
        now = pg.time.get_ticks()
    
        if self.idle:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames)
                self.image = self.idle_frames[self.current_frame]
                self.rect = self.image.get_rect()
    
        if self.shooting:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.shooting_frames)
                self.image = self.shooting_frames[self.current_frame]
                self.rect = self.image.get_rect()
    
        if self.death:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.death_frames)
                self.image = self.death_frames[self.current_frame]
                self.rect = self.image.get_rect()
                self.death_counter += 1
                if self.death_counter >= 4:
                    self.kill()
    def attack(self):
        current_time = pg.time.get_ticks()
        if current_time - self.last_attack_time > self.attack_cooldown:
            # Pass player's position and current keys state to Ranged_attack constructor
            projectile = Gunner_attack(self)
            projectile.add(self.all_sprites)
            projectile.add(self.gunner_bullets_group)
            self.last_attack_time = current_time

class Bomber(Sprite):
    def __init__(self,hp,all_sprites,bomber_bombs_group):
        super().__init__()
        idle_image,idle_image1,idle_image2,idle_image3,death_image,death_image1,death_image2,death_image3 = load_bomber_images()
        self.screen_width = 960
        self.screen_height = 540
        self.speed = 1
        self.current_frame = 0
        self.last_update = 0
        self.death_counter = 0
        self.attack_cooldown = 4000
        self.last_attack_time = 0

        self.pos_x = self.screen_width + 100
        self.pos_y = 50
        self.hp = hp
        self.bomber_bombs_group = bomber_bombs_group
        self.all_sprites = all_sprites

        self.idle = True
        self.death = False

        self.idle_frames = [
            idle_image,idle_image1,idle_image2,idle_image3
        ]
        self.death_frames = [
            death_image,death_image1,death_image2,death_image3
        ]

        self.image = self.idle_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)

    def update(self):
        self.animate()
        self.attack()

        if self.idle:
            self.pos_x -= self.speed
            self.rect.center = (self.pos_x,self.pos_y)
        if self.death:
            self.rect.center = (self.pos_x,self.pos_y)

        if self.pos_x <= -250:
            self.kill()

        if self.hp <= 0:
            self.death = True
        if self.death:
            self.idle = False

    def animate(self):
        now = pg.time.get_ticks()
    
        if self.idle:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames)
                self.image = self.idle_frames[self.current_frame]
                self.rect = self.image.get_rect()

        if self.death:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.death_frames)
                self.image = self.death_frames[self.current_frame]
                self.rect = self.image.get_rect()
                self.death_counter += 1
                if self.death_counter >= 4:
                    self.kill()

    def attack(self):
        current_time = pg.time.get_ticks()
        if current_time - self.last_attack_time > self.attack_cooldown:
            projectile = Bomber_attack(self)
            projectile.add(self.all_sprites)
            projectile.add(self.bomber_bombs_group)
            self.last_attack_time = current_time
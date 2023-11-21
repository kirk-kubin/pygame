import pygame as pg
from pygame.sprite import Sprite
from classes.ranged_attack import Ranged_attack
from classes.flash import Flash
from resources import load_player_images

player_image, player_image1, player_image2, player_image3 = load_player_images()

class Player(Sprite):
    def __init__(self,all_sprites,font,reload_time=3000,max_bullets=6):
        super().__init__()
        self.dt = clock.tick(120) / 1000
        self.current_frame = 0
        self.last_update = 0
        self.image = player_image
        self.pos_x = 100
        self.pos_y = (100)
        self.rect = self.image.get_rect()
        self.speed = 3
        self.dtspeed = self.speed*self.dt
        self.hp = 100
        self.all_sprites = all_sprites
        self.attack_cooldown = 750
        self.last_attack_time = 0
        self.max_bullets = 6  # Maximum number of bullets in the magazine
        self.bullets = self.max_bullets  # Current number of bullets in the magazine
        self.is_reloading = False  # Flag to track if the player is currently reloading
        self.reload_time = 3000  # Time it takes to reload in milliseconds (adjust as needed)
        self.last_reload_time = 0
        self.font = font
        self.last_shot_time = 0
        self.shoot_cooldown = 350
        self.start_time = pg.time.get_ticks()
        self.reloading = False
        self.reload_start = 0
        self.layer = 1
        self.screen_width = 960
        self.screen_height = 540

        self.standing_frames = [
            player_image, player_image1, player_image2, player_image3
        ]

    def attack(self,keys,surface,x,y):
        if self.is_reloading or self.bullets <= 0:
            return
        current_time = pg.time.get_ticks()
        if current_time - self.last_attack_time > self.attack_cooldown:
            # Pass player's position and current keys state to Ranged_attack constructor
            projectile = Ranged_attack(self, keys)
            projectile.add(self.all_sprites)
            flash = Flash(self)
            flash.add(self.all_sprites)
            self.bullets -= 1  # Use one bullet from the magazine
            self.last_attack_time = current_time
            # Set is_reloading to True to prevent reloading immediately after shooting
            self.is_reloading = True

    def draw_bullet_count(self, surface, x, y, font, bullets):
        if not self.reloading == True:
            text = font.render("Bullets: {}".format(bullets), True, (255, 255, 255))
            surface.blit(text, (x, y))
        if self.reloading == True:
            text = font.render("Reloading...".format(bullets), True, (255, 255, 255))
            surface.blit(text, (x, y))

    def draw_ui(self, screen):
        # Draw the remaining bullet count on the screen
        bullet_text_x = 10  # X-coordinate of the bullet count text
        bullet_text_y = 10  # Y-coordinate of the bullet count text
        self.draw_bullet_count(screen, bullet_text_x, bullet_text_y, self.font, self.bullets)

    def reload(self):
        self.bullets = self.max_bullets
        print(self.bullets)
        self.reloading = False

    def update(self):

        keys = pg.key.get_pressed()
        if (keys[pg.K_w] or keys[pg.K_s]) and (keys[pg.K_d] or keys[pg.K_a]):
            self.speed = 2
        if keys[pg.K_w]:
            self.pos_y -= self.dtspeed
        if keys[pg.K_s]:
            self.pos_y += self.dtspeed
        if keys[pg.K_a]:
            self.pos_x -= self.dtspeed
        if keys[pg.K_d]:
            self.pos_x += self.dtspeed
        if keys[pg.K_r] and not self.reloading:
            self.reload_start = pg.time.get_ticks()
            self.reloading = True
            print("a")
        if keys[pg.K_ESCAPE]:
            pg.quit()
        if self.pos_x < 0:
            self.pos_x = 0
        if self.pos_x > self.screen_width - self.rect.width:
            self.pos_x = self.screen_width - self.rect.width
        if self.pos_y < 0:
            self.pos_y = 0
        if self.pos_y > self.screen_height - self.rect.height:
            self.pos_y = self.screen_height - self.rect.height

        self.animate_gun()
        
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

        if keys[pg.K_LSHIFT]:
            self.speed = 5
        else:
            self.speed = 3

        if self.reloading and pg.time.get_ticks() - self.reload_start >= 3000:
            print("b")
            self.reload()

        if pg.time.get_ticks() - self.last_attack_time > 350:
            self.is_reloading = False

    def animate_gun(self):
        now = pg.time.get_ticks()

        if self.is_reloading:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame +1) % len(self.standing_frames)
                self.image = self.standing_frames[self.current_frame]
                self.rect = self.image.get_rect()
import pygame as pg
import random
from pygame.sprite import Group

bullets = Group()

player_image = pg.image.load("bilder/gun.png")
player_image = pg.transform.scale(player_image, (player_image.get_width()+154.55, player_image.get_height()+100))
player_image1 = pg.image.load("bilder/gun1.png")
player_image1 = pg.transform.scale(player_image1, (player_image1.get_width()+154.55, player_image1.get_height()+100))
player_image2 = pg.image.load("bilder/gun2.png")
player_image2 = pg.transform.scale(player_image2, (player_image2.get_width()+154.55, player_image2.get_height()+100))
player_image3 = pg.image.load("bilder/gun3.png")
player_image3 = pg.transform.scale(player_image3, (player_image3.get_width()+154.55, player_image3.get_height()+100))
class Player(pg.sprite.Sprite):

    def __init__(self, all_sprites, font, reload_time=3000, max_bullets=6):
        pg.sprite.Sprite.__init__(self)
        self.current_frame = 0
        self.last_update = 0
        
        self.image = player_image
        self.rect = self.image.get_rect()
        self.pos_x = 100
        self.pos_y = random.randint(0, 100)
        self.speed = 3
        self.hp = 100
        self.all_sprites = all_sprites
        self.attack_cooldown = 750
        self.last_attack_time = 0
        self.max_bullets = 6  # Maximum number of bullets in the magazine
        self.bullets = self.max_bullets  # Current number of bullets in the magazine
        self.is_reloading = False  # Flag to track if the player is currently reloading
        self.reload_time = 3000  # Time it takes to reload in milliseconds (adjust as needed)
        self.last_reload_time = 0  # Time of the last reload
        self.energy = self.bullets
        self.font = font
        self.last_shot_time = 0
        self.shoot_cooldown = 350
        self.start_time = pg.time.get_ticks()
        self.reloading = False
        self.reload_start = 0
        self.layer = 1

        self.standing = True
        
        self.standing_frames = [player_image, player_image1, player_image2, player_image3]

    def attack(self):
        if self.is_reloading or self.bullets <= 0:
            return
        
        current_time = pg.time.get_ticks()
        if current_time - self.last_attack_time > self.attack_cooldown:
            # Pass player's position to Ranged_attack constructor
            projectile = Ranged_attack(self.pos_x, self.pos_y)
            projectile.add(self.all_sprites)
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
        if keys[pg.K_w]:
            self.pos_y -= self.speed
        if keys[pg.K_s]:
            self.pos_y += self.speed
        if keys[pg.K_a]:
            self.pos_x -= self.speed
        if keys[pg.K_d]:
            self.pos_x += self.speed
        if keys [pg.K_SPACE]:
            self.attack()
        if keys[pg.K_r] and not self.reloading:
            self.reload_start = pg.time.get_ticks()
            self.reloading = True
            print("a")
        if keys[pg.K_ESCAPE]:
            pg.quit()

        self.animate()
        
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

    def handle_shooting(self, all_sprites):
        # Check if enough time has passed since the last shot
        current_time = pg.time.get_ticks()
        if current_time - self.last_shot_time > self.shoot_cooldown:
            # Create a new bullet only when the space bar is pressed and cooldown has passed
            bullet = Ranged_attack(self.rect.x, self.rect.y)
            bullet.add(all_sprites)
            # Update the last shot time to the current time
            self.last_shot_time = current_time

    def animate(self):
        now = pg.time.get_ticks()

        if self.is_reloading:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame +1) % len(self.standing_frames)
                self.image = self.standing_frames[self.current_frame]
                self.rect = self.image.get_rect()

enemy_image = pg.image.load("bilder/boneman.png")
enemy_image = pg.transform.scale(enemy_image, (enemy_image.get_width()+1000, enemy_image.get_height()+1000))
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.pos_x = 500
        self.pos_y = random.randint(0, 100)
        self.speed = 3
        self.layer = 0

    def update(self):
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y

        self.pos_x -= self.speed

        if self.pos_x > -100:
            self.kill()

ranged_image = pg.image.load("bilder/bullet.png")
ranged_image = pg.transform.scale(ranged_image, (ranged_image.get_width()+23.333, ranged_image.get_height()+10))
class Ranged_attack(pg.sprite.Sprite):
    def __init__(self, player_x, player_y):
        pg.sprite.Sprite.__init__(self)
        self.image = ranged_image
        self.rect = self.image.get_rect()

        self.pos_x = player_x + 150  # Set the initial x-coordinate relative to the player's position
        self.pos_y = player_y + 15  # Set the initial y-coordinate relative to the player's position
        self.initial_x = self.pos_x  # Store the initial x-coordinate where the bullet was fired
        self.player_controlled_distance = 50  # Number of pixels the player can control the bullet
        self.speed = 10
        self.player_controlled = True

    def update(self):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

        if self.player_controlled:
            keys = pg.key.get_pressed()
            if keys[pg.K_w]:
                self.pos_y -= 3
            if keys[pg.K_a]:
                self.pos_x -= 3
            if keys[pg.K_d]:
                self.pos_x += 3
            if keys[pg.K_s]:
                self.pos_y += 3

            # Disable player control once the bullet has traveled the specified distance
            if abs(self.pos_x - self.initial_x) >= self.player_controlled_distance:
                self.player_controlled = False

        self.pos_x += self.speed

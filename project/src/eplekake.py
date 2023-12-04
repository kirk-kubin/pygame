import pygame as pg
import sys
from sprites import *
from resources import *

def game_loop():
    global bg_x,gunner,bomber,player
    clock.tick(120)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                return False

        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            player.attack(keys, screen, player.pos_x, player.pos_y)

    if len(gunner_group) < 1 and pg.time.get_ticks() % 200 == 0:
        new_gunner = Gunner(10,all_sprites,gunner_group)
        gunner_group.add(new_gunner)
        all_sprites.add(new_gunner)
    if len(bomber_group) < 1 and pg.time.get_ticks() % 100 == 0:
        new_bomber = Bomber(5,all_sprites,bomber_bombs_group)
        bomber_group.add(new_bomber)
        all_sprites.add(new_bomber)

    gunner_touch_player = pg.sprite.spritecollide(player,gunner_group,True)
    if gunner_touch_player:
        player.hp -= 10
    bomber_touch_player = pg.sprite.spritecollide(player,bomber_group,True)
    if bomber_touch_player:
        player.hp -= 25

    for bullet in gunner_bullets_group:
        hit_by_gunner = pg.sprite.spritecollide(player,gunner_bullets_group,None)
        if hit_by_gunner:
            player.hp -= 5
            bullet.kill()
    for bomb in bomber_bombs_group:
        hit_by_bomber = pg.sprite.spritecollide(player,bomber_bombs_group,None)
        if hit_by_bomber:
            player.hp -= 20
            bomb.kill()

    bullets_collide = pg.sprite.groupcollide(player_bullets_group,gunner_bullets_group,False,True)
    if bullets_collide:
        player.hp += 0
    bomb_collide = pg.sprite.groupcollide(player_bullets_group,bomber_bombs_group,False,True)
    if bomb_collide:
        player.hp += 0

    for bullet in player_bullets_group:
        gunner_hits = pg.sprite.spritecollide(bullet,gunner_group,None)
        for gunner in gunner_hits:
            gunner.hp -= 5
            bullet.kill()
        bomber_hits = pg.sprite.spritecollide(bullet,bomber_group,None)
        for bomber in bomber_hits:
            bomber.hp -= 5
            bullet.kill()

    screen.blit(bg_img, (bg_x, 0))
    screen.blit(bg_img, (bg_x - WIDTH * 2, 0))

    bg_x -= 1
    bg_x %= (WIDTH * 2)

    all_sprites.update()
    flash.update()

    all_sprites.draw(screen)
    player.draw_ui(screen)
    pg.display.flip()

    return True

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WIDTH = 960
HEIGHT = 540
bg_img = pg.image.load("project/images/background/bg3.png")
bg_img = pg.transform.scale(bg_img, (WIDTH * 2, HEIGHT))
pg.init()
bg_x = 0

keys = pg.key.get_pressed()

screen = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()

font_size = 36
font = pg.font.Font(None, font_size)

all_sprites = pg.sprite.LayeredUpdates()
gunner_bullets_group = pg.sprite.Group()
bomber_bombs_group = pg.sprite.Group()
gunner_group = pg.sprite.Group()
gunner = Gunner(10,all_sprites,gunner_bullets_group)
gunner_group.add(gunner)
bomber_group = pg.sprite.Group()
bomber = Bomber(5,all_sprites,bomber_bombs_group)
bomber_group.add(bomber)
player_bullets_group = pg.sprite.Group()
player = Player(all_sprites,font,player_bullets_group)
flash = pg.sprite.Group()

all_sprites.add(player_bullets_group)
all_sprites.add(gunner_bullets_group)
all_sprites.add(bomber_bombs_group)
all_sprites.add(gunner_group)
all_sprites.add(bomber_group)
all_sprites.add(player)
all_sprites.add(flash)

playing = True
while playing:
    playing = game_loop()

pg.quit()
sys.exit()
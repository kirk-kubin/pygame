import pygame as pg
import sys
from sprites import *
from resources import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WIDTH = 960
HEIGHT = 540
bg_img = pg.image.load("project/images/background/bg.png")
pg.init()
i = 0

def game_loop():
    global i
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False

        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            player.attack(keys, screen, player.pos_x, player.pos_y)

    screen.blit(bg_img,(i,0))
    screen.blit(bg_img,(WIDTH+i,0))
    if (i == -(WIDTH*3)):
        screen.blit(bg_img,(WIDTH+i,0))
        i = 0
    i -= 1

    all_sprites.update()
    flash.update()
    bullets.update()

    hits = pg.sprite.spritecollide(player, enemies, True)
    if hits:
        player.hp -= 100

    all_sprites.draw(screen)
    player.draw_ui(screen)
    pg.display.flip()

    return True

screen = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()

font_size = 36
font = pg.font.Font(None, font_size)

all_sprites = pg.sprite.LayeredUpdates()
enemies = pg.sprite.Group()
bullets = pg.sprite.Group()
player = Player(all_sprites, font)
flash = pg.sprite.Group()

all_sprites.add(player)
all_sprites.add(flash)

playing = True
while playing:
    playing = game_loop()

pg.quit()
sys.exit()
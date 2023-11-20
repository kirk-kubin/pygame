import pygame as pg
import sys
from sprites import *
from pygame.sprite import LayeredUpdates
pg.init()

IDLE = True
RUN = False

BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,255,255)
YELLOW = (255,255,0)
MAGENTA = (255,0,255)
CYAN = (0,255,255)

screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
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
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            player.attack(pg.key.get_pressed(), screen, player.pos_x, player.pos_y)

    screen.fill(BLACK)
    all_sprites.update()
    flash.update()
    bullets.update()

    hits = pg.sprite.spritecollide(player, enemies, True)
    if hits:
        player.hp -= 100

    all_sprites.draw(screen)
    player.draw_ui(screen)
    pg.display.flip()

    clock.tick(120)
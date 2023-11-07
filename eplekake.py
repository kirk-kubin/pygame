
import pygame as pg
from sprites import *
from pygame.sprite import LayeredUpdates
pg.init()

BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,255,255)
YELLOW = (255,255,0)
MAGENTA = (255,0,255)
CYAN = (0,255,255)

pos_x = 100
pos_y = 100

size_x = 50
size_y = 50

screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
clock = pg.time.Clock()
font_size = 36  # Choose the font size
font = pg.font.Font(None, font_size)  # Use None for the default system font or specify a font file path
all_sprites = pg.sprite.LayeredUpdates()  # Use LayeredUpdates for proper layering
enemies = pg.sprite.Group()
start_time = pg.time.get_ticks()  # Add parentheses to call the function
playing = True
bullet = Ranged_attack(pos_x, pos_y)
player = Player(all_sprites, font)
all_sprites.add(bullet)
all_sprites.add(player)

while playing:
    clock.tick(120)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
            pg.quit()

    bullets.update()

    if len(all_sprites) < 10:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    all_sprites.update()

    hits = pg.sprite.spritecollide(player, enemies, True)
    if hits:
        player.hp -= 100

    screen.fill(YELLOW)
    all_sprites.draw(screen)

    player_box = pg.Rect(pos_x, pos_y, size_x, size_y)
    player.draw_ui(screen)
    pg.display.flip()

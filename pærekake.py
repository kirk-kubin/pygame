import pygame as pg
import sys
from animate import *
from sprites import *
from pygame.sprite import LayeredUpdates

BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,255,255)
YELLOW = (255,255,0)
MAGENTA = (255,0,255)
CYAN = (0,255,255)

class Game():
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.FPS = 120
        self.clock = pg.time.Clock()

        font_size = 36
        self.font = pg.font.Font(None, font_size)

        self.new()

    def new(self):
        all_sprites = pg.sprite.LayeredUpdates()

        self.enemies = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.player = Player(all_sprites, self.font)
        self.flash = pg.sprite.Group()

        self.all_sprites.add(self.player)
        self.all_sprites.add(self.flash)

        self.idle_sheet_image = pg.image.load("bilder/idle.png").convert_alpha()
        self.idle_sheet = spritesheet.Spritesheet(self.idle_sheet_image)
        self.run_sheet_image = pg.image.load("bilder/run.png").convert_alpha()
        self.run_sheet = spritesheet.Spritesheet(self.run_sheet_image)

        self.animation_assets = {
            'idle_0': self.idle_sheet.get_image(0,20,26,3,i),
            'idle_1': self.idle_sheet.get_image(1,20,26,3,i),
            'idle_2': self.idle_sheet.get_image(2,20,26,3,i),
            'idle_3': self.idle_sheet.get_image(3,20,26,3,i),
            'idle_4': self.idle_sheet.get_image(4,20,26,3,i),
            'run_0': self.run_sheet.get_image(0,22,28,3,i),
            'run_1': self.run_sheet.get_image(1,22,28,3,i),
            'run_2': self.run_sheet.get_image(2,22,28,3,i),
            'run_3': self.run_sheet.get_image(3,22,28,3,i),
            'run_5': self.run_sheet.get_image(4,22,28,3,i)
        }

        self.idle_frames = [
            self.animation_assets['idle_0'],
            self.animation_assets['idle_1'],
            self.animation_assets['idle_2'],
            self.animation_assets['idle_3'],
            self.animation_assets['idle_4']
        ]
        self.run_frames = [
            self.animation_assets['run_0'],
            self.animation_assets['run_1'],
            self.animation_assets['run_2'],
            self.animation_assets['run_3'],
            self.animation_assets['run_4']
        ]
        idle_animation = Animation(self.idle_frames, 150, loop=True)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    self.playing = False
            

    def update(self):
        self.all_sprites(self)

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)

        pg.display.flip()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(self.FPS)
            self.events()
            self.update()
            self.draw()

g = Game()
import pygame as pg

class Animation():
    def __init__(self, frames, counter, loop):
        self.frames = list(frames)
        self.frame = frames[0]
        self.counter = counter
        self.loop = loop
        self.current_image = 0
        self.last_time = 0

    def update(self):
        now = pg.time.get_ticks()

        if now - self.last_time > self.counter:
            self.last_time = now
            self.current_image = (self.current_image + 1) % len(self.frames)
            self.frame = self.frames[self.current_image]
        
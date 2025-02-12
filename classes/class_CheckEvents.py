import pygame as pg
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE


class CheckEvents:
    def __init__(self, game=None):
        self.game = game

    def check_events(self):
        for event in pg.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                self.game.run = False


            self.game.player.handle_event(event)
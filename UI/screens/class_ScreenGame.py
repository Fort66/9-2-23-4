import pygame as pg
from pygame.display import set_mode, set_caption,set_icon, get_desktop_sizes
from pygame.locals import RESIZABLE, FULLSCREEN
from pygame.image import load

from dataclasses import dataclass

pg.init()

@dataclass
class ScreenGame:
    size: tuple = (0, 0)
    color: str| tuple = 'steelblue'
    icon: str = ''
    caption: str = 'Game'
    is_resizable: bool = False
    is_fullscreen: bool = False


    def __post_init__(self):
        if self.is_resizable:
            self.window = set_mode(self.size, RESIZABLE)
        elif self.is_fullscreen:
            self.curret_screen_resolution = get_desktop_sizes()[0]
            self.window = set_mode(self.curret_screen_resolution, FULLSCREEN)
        else:
            self.window = set_mode(self.size)

        if self.icon:
            self.icon = set_icon(load(self.icon))

        set_caption(self.caption)
        self.rect = self.window.get_rect()
        
    def update_caption(self, caption):
        self.caption = set_caption(caption)



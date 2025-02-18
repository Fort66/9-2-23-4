import numpy as np
from pygame.image import load
from pygame.transform import scale

from os import listdir
from time import time

class Animator:
    def __init__(self, dir_path=None, speef_frame=.05, obj_rect=None):
        
        self.dir_path = dir_path
        self.speef_frame = speef_frame
        self.obj_rect = obj_rect[2:]
        
        self.frames = 0
        self.frame = 0
        self.puased_time = 0
        self.loops = -1
        self.paused = False
        self.file_list = sorted(listdir(dir_path))
        self.__post_init__()
        
    def __post_init__(self):
        self.original_frames =  np.array([[scale(load(f'{self.dir_path}/{value}').convert_alpha(), self.obj_rect), self.speef_frame]for value in self.file_list])

        
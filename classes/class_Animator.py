import numpy as np
from pygame.image import load
from pygame.transform import scale, scale_by
from classes.class_SpriteGroups import SpriteGroups

from os import listdir
from time import time
from PIL import Image


class Animator:
    def __init__(
        self,
        dir_path=None,
        speed_frame=None,
        scale_value=None,
        loops=None,
        size=None
    ):
        self.sprite_groups = SpriteGroups()
        super().__init__(self.sprite_groups.camera_group)

        self.dir_path = dir_path
        self.speed_frame = speed_frame
        self.size = size

        self.frames = 0
        self.frame = 0
        self.frame_time = 0
        self.loops = loops

        self.file_list = listdir(dir_path)
        self.file_list.sort(key=lambda x: int(x.split('.')[0]))
        self.image_size = Image.open(f'{self.dir_path}/{self.file_list[0]}').size

        if self.size:
            self.scale_value = (self.size[0] / self.image_size[0] + .05, self.size[1] / self.image_size[1] + .05)
        else:
            self.scale_value = scale_value
        self.__post_init__()

    def __post_init__(self):
        self.original_frames = np.array(
            [
                [
                    scale_by(
                        load(f'{self.dir_path}/{value}').convert_alpha(),
                        self.scale_value,
                    ),
                    self.speed_frame,
                ]
                for value in self.file_list
            ]
        )

        self.frames = self.original_frames.copy()
        self.image_rotation = self.frames[self.frame][0]

    def animate(self):

        if self.frame_time == 0:
            self.frame_time = time()

        if time() - self.frame_time > self.frames[self.frame][1]:
            if self.loops == -1:
                self.frame = self.frame + 1 if self.frame < len(self.frames) - 1 else 0


            if self.loops > 0:
                self.frame = self.frame + 1 if self.frame < len(self.frames) - 1 else self.frames[-1] #TODO

                if self.frame == len(self.frames) - 1:
                    self.loops -= 1
            self.frame_time = time()




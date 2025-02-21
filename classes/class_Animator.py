import numpy as np
from pygame.image import load
from pygame.transform import scale, scale_by
from classes.class_SpriteGroups import SpriteGroups

from os import listdir
from time import time


class Animator:
    def __init__(
        self,
        dir_path=None,
        speed_frame=None,
        obj=None,
        obj_rect=None,
        scale_value=None,
        loops=None,
        pos=None,
    ):
        self.sprite_groups = SpriteGroups()
        super().__init__(self.sprite_groups.camera_group)

        self.dir_path = dir_path
        self.speed_frame = speed_frame
        self.obj = obj
        self.obj_rect = obj_rect
        self.scale_value = scale_value
        if self.obj_rect:
            self.size = (
                self.obj.rect.size[0] * self.scale_value[0],
                self.obj.rect.size[1] * self.scale_value[1],
            )

        self.frames = 0
        self.frame = 0
        self.frame_time = 0
        self.loops = loops
        self.paused = False
        self.pos = pos
        self.file_list = sorted(listdir(dir_path))
        self.__post_init__()

    def __post_init__(self):
        if self.obj_rect:
            self.original_frames = np.array(
                [
                    [
                        scale(
                            load(f"{self.dir_path}/{value}").convert_alpha(), self.size
                        ),
                        self.speed_frame,
                    ]
                    for value in self.file_list
                ]
            )
        else:
            self.original_frames = np.array(
                [
                    [
                        scale_by(
                            load(f"{self.dir_path}/{value}").convert_alpha(),
                            self.scale_value,
                        ),
                        self.speed_frame,
                    ]
                    for value in self.file_list
                ]
            )

        self.frames = self.original_frames.copy()
        self.image_rotation = self.frames[self.frame][0]
        self.rect = self.image_rotation.get_rect(center=self.obj.rect.center)

    def update(self):
        self.obj_rect = self.obj.rect
        if self.obj_rect:
            self.size = (
                self.obj.rect.size[0] * self.scale_value[0],
                self.obj.rect.size[1] * self.scale_value[1],
            )

        self.image_rotation = self.frames[self.frame][0]
        self.rect = self.image_rotation.get_rect(center=self.obj.rect.center)

        if self.frame_time == 0:
            self.frame_time = time()

        if time() - self.frame_time > self.frames[self.frame][1]:
            if self.loops == -1:
                self.frame = self.frame + 1 if self.frame < len(self.frames) - 1 else 0
                self.frame_time = time()
                self.update_frames()

            if self.loops > 0:
                self.frame = (
                    self.frame + 1
                    if self.frame < len(self.frames) - 1
                    else self.frames[-1]
                )
                self.frame_time = time()
                self.update_frames()
                if self.frame == len(self.frames) - 1:
                    self.loops -= 1

    def update_frames(self):
        if self.loops:
            self.frames[self.frame][0] = self.original_frames[self.frame][0].copy()

        if self.obj_rect:
            self.frames[self.frame][0] = scale(self.frames[self.frame][0], self.size)
        else:
            self.frames[self.frame][0] = scale_by(
                self.frames[self.frame][0], self.scale_value
            )

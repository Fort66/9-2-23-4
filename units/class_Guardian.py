from pygame.sprite import Sprite
from pygame.transform import rotozoom
from classes.class_Animator import Animator

from time import time

from functions.function_guards_collision import (
    plyayer_guard_collision,
    enemies_guard_collision,
    guards_collision
    )


class Guardian(Animator, Sprite):
    def __init__(
        self,
        dir_path=None,
        speed_frame=None,
        obj=None,
        guard_level=None,
        scale_value=None,
        loops=None,
        size=None,
        angle=None,
        owner=None
    ):
        super().__init__(
            dir_path=dir_path,
            speed_frame=speed_frame,
            scale_value=scale_value,
            loops=loops,
            size=size
        )

        self.guard_level = guard_level
        self.angle = angle
        self.obj = obj
        self.destruction_time = 0
        self.rect = self.image_rotation.get_rect(center=self.obj.rect.center)
        self.owner = owner

    def decrease_level(self, value):
        if self.guard_level > 0:
            self.guard_level -= value



    def update(self):
        plyayer_guard_collision()
        enemies_guard_collision()
        self.angle = self.obj.angle
        self.rect.center = self.obj.rect.center
        self.image_rotation = self.frames[self.frame][0]
        self.image_rotation = rotozoom(self.image_rotation, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)
        super().animate()

        if guards_collision():
            if self.destruction_time <= 0:
                self.destruction_time = time()

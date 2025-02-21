from pygame.sprite import Sprite
from classes.class_Animator import Animator

from functions.function_guards_collision import plyayer_guard_collision, enemies_guard_collision


class Guardian(Animator, Sprite):
    def __init__(
        self,
        dir_path=None,
        speed_frame=None,
        obj=None,
        obj_rect=None,
        guard_level=None,
        scale_value=None,
        loops=None,
        pos=None,
    ):
        super().__init__(
            dir_path=dir_path,
            speed_frame=speed_frame,
            obj=obj,
            obj_rect=obj_rect,
            scale_value=scale_value,
            loops=loops,
            pos=pos,
        )

        self.guard_level = guard_level

    def decrease_guard_level(self, value):
        if self.guard_level > 0:
            self.guard_level -= value



    def update(self):
        plyayer_guard_collision()
        enemies_guard_collision()
        super().update()
from classes.class_Animator import Animator


class Guardian(Animator):
    def __init__(
        self,
        dir_path=None,
        speed_frame=None,
        obj_rect=None,
        guard_level=None,
        scale_value=None,
        loops=None,
        pos=None,
    ):
        super().__init__(
            dir_path=dir_path,
            speed_frame=speed_frame,
            obj_rect=obj_rect,
            scale_value=scale_value,
            loops=loops,
            pos=pos,
        )

        self.guard_level = guard_level

    @property
    def decrease_guard_level(self):
        if self.guard_level > 0:
            self.guard_level -= 1
        else:
            del self

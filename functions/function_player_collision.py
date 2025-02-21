from pygame.sprite import groupcollide, spritecollide
from classes.class_SpriteGroups import SpriteGroups
from units.class_Explosion import Explosion

from icecream import ic


def guard_collision(obj):
    sprite_groups = SpriteGroups()
    object_collide = spritecollide(obj, sprite_groups.enemies_shot_group, dokill=True)

    # if object_collide:
    #     if hasattr(obj, "shield"):
    #         if obj.shield.guard_level > 0:
    #             obj.shield.decrease_guard_level
    #         else:
    #             delattr(obj, "shield")

        # obj.expl_enemies_rocket = Explosion(
        #     dir_path='images/explosion/rocket1_expl',
        #     speed_frame=.05,
        #     obj_rect=None,
        #     scale_value=1,
        #     loops=1,
        #     pos=obj.rect.center
        # )

        

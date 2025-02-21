from pygame.sprite import groupcollide, spritecollide
from classes.class_SpriteGroups import SpriteGroups

from icecream import ic


def guard_collision(obj):
    sprite_groups = SpriteGroups()
    object_collide = spritecollide(obj, sprite_groups.player_shot_group, dokill=False)

    # if object_collide:
    #     if hasattr(obj, "shield"):
    #         if obj.shield.guard_level > 0:
    #             obj.shield.decrease_guard_level
    #         else:
    #             delattr(obj, "shield")

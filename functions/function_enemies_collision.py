from pygame.sprite import groupcollide, spritecollide
from classes.class_SpriteGroups import SpriteGroups

from icecream import ic


def enemies_collision():
    sprite_groups = SpriteGroups()
    object_collide = groupcollide(
        sprite_groups.enemies_group,
        sprite_groups.player_shot_group,
        dokilla=False,
        dokillb=True
        )

    # if object_collide:
    #     if hasattr(obj, "shield"):
    #         if obj.shield.guard_level > 0:
    #             obj.shield.decrease_guard_level
    #         else:
    #             delattr(obj, "shield")

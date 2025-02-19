from pygame.sprite import groupcollide, spritecollide
from classes.class_SpriteGroups import SpriteGroups

from icecream import ic


def shots_collision(obj):
    sprite_groups = SpriteGroups()
    object_collide = groupcollide(sprite_groups.enemies_shot_group, sprite_groups.player_group, dokilla=False, dokillb=False)

    # if object_collide:
    #     ic('object_collide')
        
        
        
        # if hasattr(obj, "shield"):
        #     if obj.shield.guard_level > 0:
        #         obj.shield.decrease_guard_level
        #         return True
        #     else:
        #         delattr(obj, "shield")
        #         return False

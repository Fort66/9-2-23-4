from pygame.sprite import groupcollide, spritecollide
from classes.class_SpriteGroups import SpriteGroups

from icecream import ic

def guard_collision(obj):
    sprite_groups = SpriteGroups()
    object_collode = spritecollide(obj, sprite_groups.enemies_shot_group, dokill=True)
    
    if object_collode:
        if obj.guard_level <= 0:
            obj.kill()






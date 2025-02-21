from pygame.sprite import groupcollide
from classes.class_SpriteGroups import SpriteGroups

sprite_groups = SpriteGroups()

def plyayer_guard_collision():
    object_collide = groupcollide(sprite_groups.enemies_shot_group, sprite_groups.player_guard_group, dokilla=True, dokillb=False)
    if object_collide:
        lot_hits = len(list(object_collide.values()))
        hits = list(object_collide.keys())[0]
        if hits.guard_level > 0:
            hits.decrease_guard_level(lot_hits)

        if hits.guard_level == 0:
            hits.kill()
            

def enemies_guard_collision():
    object_collide = groupcollide(sprite_groups.player_shot_group, sprite_groups.enemies_guard_group, dokilla=True, dokillb=False)
    if object_collide:
        
        lot_hits = len(list(object_collide.values()))
        hits = list(object_collide.keys())[0]
        if hits.guard_level > 0:
            hits.decrease_guard_level(lot_hits)

        if hits.guard_level == 0:
            hits.kill()

from pygame.sprite import groupcollide, spritecollide
from classes.class_SpriteGroups import SpriteGroups
from units.class_Explosion import Explosion

from icecream import ic


def player_collision():
    sprite_groups = SpriteGroups()
    object_collide = groupcollide(
        sprite_groups.player_group,
        sprite_groups.enemies_shot_group,
        dokilla=False,
        dokillb=True
        )

    if object_collide:
        lot_hits = len(list(object_collide.values())[0])
        hits = list(object_collide.keys())[0]

        if hits.hp > 0:
            hits.decrease_hp(lot_hits)

        if hits.hp <= 0:
            explosion = Explosion(
            dir_path="images/explosion/ship1_expl",
            speed_frame=0.12,
            scale_value=(0.75, 0.75),
            loops=1,
            obj=hits,
            angle=hits.angle,
        )
            if not explosion:
                hits.kill()


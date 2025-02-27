from pygame.sprite import groupcollide, spritecollideany
from classes.class_SpriteGroups import SpriteGroups
from units.class_Explosion import Explosion

from icecream import ic

sprite_groups = SpriteGroups()


def player_guard_collision(self):
    if (
        spritecollideany(self, sprite_groups.player_guard_group)
        and self.owner not in sprite_groups.player_group
    ) or (
        spritecollideany(self, sprite_groups.player_group)
        and self.owner not in sprite_groups.player_group
    ):
        explosion = Explosion(
            dir_path="images/explosion/rocket1_expl",
            speed_frame=0.01,
            scale_value=(0.5, 0.5),
            loops=1,
            obj=self,
            angle=self.angle,
        )


def enemies_guard_collision(self):
    if (
        spritecollideany(self, sprite_groups.enemies_guard_group)
        and self.owner not in sprite_groups.enemies_group
    ) or (
        spritecollideany(self, sprite_groups.enemies_group)
        and self.owner not in sprite_groups.enemies_group
    ):
        explosion = Explosion(
            dir_path="images/explosion/pulsar",
            speed_frame=0.01,
            scale_value=(0.25, 0.25),
            loops=1,
            obj=self,
            angle=self.angle,
        )


def shots_collision():
    object_collision = groupcollide(
        sprite_groups.player_shot_group, sprite_groups.enemies_shot_group, True, True
    )

    if object_collision:
        hits = list(object_collision.values())[0]
        explosion = Explosion(
            dir_path="images/explosion/rocket1_expl",
            speed_frame=0.01,
            scale_value=(0.5, 0.5),
            loops=1,
            obj=hits[0],
            angle=hits[0].angle,
        )

def distance_collision(self):
    if self in sprite_groups.player_shot_group:
        explosion = Explosion(
            dir_path="images/explosion/pulsar",
            speed_frame=0.01,
            scale_value=(0.25, 0.25),
            loops=1,
            obj=self,
            angle=self.angle,
        )
    if self in sprite_groups.enemies_shot_group:
        explosion = Explosion(
            dir_path="images/explosion/rocket1_expl",
            speed_frame=0.01,
            scale_value=(0.5, 0.5),
            loops=1,
            obj=self,
            angle=self.angle,
        )
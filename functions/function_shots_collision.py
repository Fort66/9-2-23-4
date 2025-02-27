from pygame.sprite import groupcollide, spritecollideany
from classes.class_SpriteGroups import SpriteGroups
from units.class_Explosion import Explosion

from icecream import ic

sprite_groups = SpriteGroups()

def player_guard_collision(self):
    if spritecollideany(self, sprite_groups.player_guard_group) and self.owner not in sprite_groups.player_group:
        explosion = Explosion(
            dir_path='images/explosion/rocket1_expl',
            speed_frame=.01,
            scale_value=(.5, .5),
            loops=1,
            obj=self,
            angle=self.angle,
            )

def enemies_guard_collision(self):
    if spritecollideany(self, sprite_groups.enemies_guard_group) and self.owner not in sprite_groups.enemies_group:
        explosion = Explosion(
            dir_path='images/explosion/rocket1_expl',
            speed_frame=.01,
            scale_value=(.5, .5),
            loops=1,
            obj=self,
            angle=self.angle,
            )
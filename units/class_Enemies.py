from pygame.sprite import Sprite
from pygame.transform import scale_by, flip, rotozoom
from pygame.image import load
from pygame.locals import MOUSEWHEEL, MOUSEBUTTONDOWN, K_a, K_d, K_w, K_s
from pygame.math import Vector2
from pygame.key import get_pressed

from icecream import ic

from random import randint, choice, uniform
import math
from time import time

from units.class_Shots import Shots


from config.sources.enemies.source import ENEMIES
from classes.class_SpriteGroups import SpriteGroups
from config.create_Object import checks, weapons
from units.class_Guardian import Guardian
from functions.function_enemies_collision import enemies_collision

class Enemy(Sprite):
    def __init__(self, group=None, player=None):
        self.sprite_groups = SpriteGroups()
        super().__init__(self.sprite_groups.camera_group)
        self.sprite_groups.camera_group.add(self)
        self.sprite_groups.enemies_group.add(self)

        self.group = group
        self.player = player
        self.angle = 0
        self.random_value()
        self.change_direction()
        self.shots = False
        self.min_distance = 300
        self.shot_distance = 1500
        self.is_min_distance = False
        self.hp = 2
        self.shot_time = 0
        self.__post_init__()

    def __post_init__(self):
        self.image = ENEMIES[1]["angle"][0]["sprite"]
        self.image_rotation = self.image.copy()

        self.pos = (
            uniform(
                self.sprite_groups.camera_group.background_rect.left + 200,
                self.sprite_groups.camera_group.background_rect.right - 200,
            ),
            uniform(
                self.sprite_groups.camera_group.background_rect.top + 200,
                self.sprite_groups.camera_group.background_rect.bottom - 200,
            ),
        )

        self.rect = self.image_rotation.get_rect(center=self.pos)
        self.direction = Vector2(self.pos)

        self.sprite_groups.camera_group.add(shield := Guardian(
            dir_path="images/guards/guard2",
            speed_frame=0.09,
            scale_value=(1, 1),
            loops=-1,
            guard_level=randint(3, 10),
            obj=self,
            size=self.rect.size,
            angle=self.angle,
            owner=self
        ))
        self.sprite_groups.enemies_guard_group.add(shield)

        self.prepare_weapon(0)

    def random_value(self):
        self.direction_list = [0, 1, -1]
        self.speed = randint(0, 5)
        self.move_count = randint(0, 600)
        self.permission_shot = uniform(1, 3)

    def prepare_weapon(self, angle):
        weapons.load_weapons(obj=self, source=ENEMIES[1]["angle"][angle]["weapons"], angle=angle)

    def pos_weapon_rotation(self):
        return weapons.pos_rotation(obj=self, angle=self.angle)

    def rotation(self):
        rotateX = self.player.rect.centerx - self.rect.centerx
        rotateY = self.player.rect.centery - self.rect.centery
        angle_vector = -math.atan2(rotateY, rotateX) * 180 / math.pi

        if angle_vector > 0:
            self.angle = angle_vector
        else:
            self.angle = 360 + angle_vector

        for value in ENEMIES[1]["angle"]:
            if self.angle <= value:
                self.image = ENEMIES[1]["angle"][value]["sprite"]
                break

        self.image_rotation = self.image
        self.image_rotation = rotozoom(self.image, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)

    def check_position(self):
        checks.position(self, self.sprite_groups.camera_group.background_rect)
        if not checks.resolved_move:
            self.change_direction()
            checks.resolved_move = True

        if not self.is_min_distance:
            if (
                Vector2(self.rect.center).distance_to(self.player.rect.center)
            ) <= self.min_distance:
                self.is_min_distance = True
                self.moveX *= -1
                self.moveY *= -1
        if (
            Vector2(self.rect.center).distance_to(self.player.rect.center)
        ) > self.min_distance:
            self.is_min_distance = False

    def move(self):
        self.rect.move_ip(self.moveX * self.speed, self.moveY * self.speed)

    def change_direction(self):
        self.moveX = choice(self.direction_list)
        self.moveY = choice(self.direction_list)

    def shot(self):
        if (
            Vector2(self.rect.center).distance_to(self.player.rect.center)
            <= self.shot_distance
        ):
            if self.player.first_shot:
                if self.shot_time == 0:
                    self.shot_time = time()
                if time() - self.shot_time >= self.permission_shot:
                    value = self.pos_weapon_rotation()
                    for pos in value:
                        self.sprite_groups.camera_group.add(
                            shot := Shots(
                                pos=(pos),
                                speed=8,
                                angle=self.angle,
                                shoter=self,
                                kill_shot_distance=2000,
                                color="",
                                image="images/rockets/shot1.png",
                                scale_value=0.07,
                                owner=self
                            )
                        )
                        self.sprite_groups.enemies_shot_group.add(shot)
                        self.shot_time = time()

    def check_move_count(self):
        if self.move_count <= 0:
            self.random_value()
        else:
            self.move_count -= 1

    def decrease_hp(self, value):
        if self.hp > 0:
            self.hp -= value
        if self.hp <= 0:
            self.kill()

    def update(self):
        self.check_position()
        self.rotation()
        self.check_move_count()
        # self.move()
        self.shot()

        enemies_collision()

        weapons.update_weapons(obj=self, angle=self.angle)

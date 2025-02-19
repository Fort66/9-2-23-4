from pygame.sprite import Sprite
from pygame.transform import scale_by, flip, rotozoom
from pygame.image import load
from pygame.locals import MOUSEWHEEL, MOUSEBUTTONDOWN, K_a, K_d, K_w, K_s
from pygame.math import Vector2
from pygame.key import get_pressed

from units.class_Shots import Shots
from logic.class_FirstShot import FirstShot
import math

from config.sources.heroes.source import HEROES

from classes.class_SpriteGroups import SpriteGroups
from units.class_Guardian import Guardian


from icecream import ic


class Player(Sprite):
    def __init__(
        self,
        pos=None,
    ):
        self.sprite_groups = SpriteGroups()
        super().__init__(self.sprite_groups.camera_group)
        self.sprite_groups.camera_group.add(self)
        self.sprite_groups.player_group.add(self)

        self.pos = pos
        self.direction = Vector2(pos)
        self.angle = 0
        self.rotation_speed = HEROES[1]["rotation_speed"]
        self.speed = HEROES[1]["speed"]
        self.first_shot = False
        self.__post_init__()

    def __post_init__(self):
        self.image = HEROES[1]["angle"][0]["sprite"]
        self.image_rotation = self.image.copy()
        self.rect = self.image_rotation.get_rect(center=self.pos)
        
        self.shield = Guardian(
            
        )
        
        self.prepare_weapon(0)

    def handle_event(self, event):
        if event.type == MOUSEWHEEL:
            if event.y == -1:
                self.angle = (self.angle - self.rotation_speed) % 360
                self.rotation()
            elif event.y == 1:
                self.angle = (self.angle + self.rotation_speed) % 360
                self.rotation()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if not self.first_shot:
                    self.first_shot = not self.first_shot
                self.shot()

    def shot(self):
        for value in self.pos_weapon_rotation:
            self.sprite_groups.camera_group.add(
                shot := Shots(
                    pos=(value),
                    speed=10,
                    angle=self.angle,
                    shoter=self,
                    kill_shot_distance=2000,
                    image="images/rockets/shot3.png",
                    scale_value=0.15,
                )
            )
            self.sprite_groups.player_shot_group.add(shot)

    def prepare_weapon(self, angle):
        self.pos_weapons = []
        for value in HEROES[1]["angle"][angle]["weapons"]:
            self.pos_weapons.append(value)

    @property
    def pos_weapon_rotation(self):
        result = []
        for weapon in self.pos_weapons:
            newX, newY = self.vector_rotation(weapon, -self.angle / 180 * math.pi)
            result.append([self.rect.centerx + newX, self.rect.centery + newY])
        return result

    def vector_rotation(self, vector, angle):
        vector = Vector2(vector)
        return vector.rotate_rad(angle)

    def rotation(self):
        for value in HEROES[1]["angle"]:
            if self.angle <= value:
                self.image = HEROES[1]["angle"][value]["sprite"]
                self.prepare_weapon(value)
                break

        self.image_rotation = self.image
        self.image_rotation = rotozoom(self.image, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)

    def check_position(self):
        if self.rect.left <= self.sprite_groups.camera_group.background_rect.left:
            self.rect.left = self.sprite_groups.camera_group.background_rect.left
        if self.rect.right >= self.sprite_groups.camera_group.background_rect.right:
            self.rect.right = self.sprite_groups.camera_group.background_rect.right
        if self.rect.top <= self.sprite_groups.camera_group.background_rect.top:
            self.rect.top = self.sprite_groups.camera_group.background_rect.top
        if self.rect.bottom >= self.sprite_groups.camera_group.background_rect.bottom:
            self.rect.bottom = self.sprite_groups.camera_groupbackground_rect.bottom

    def move(self):
        keys = get_pressed()
        if keys[K_a]:
            self.rect.move_ip(-self.speed, 0)
        if keys[K_d]:
            self.rect.move_ip(self.speed, 0)
        if keys[K_w]:
            self.rect.move_ip(0, -self.speed)
        if keys[K_s]:
            self.rect.move_ip(0, self.speed)

    def update(self):
        self.check_position()
        self.move()

        for value in self.pos_weapon_rotation:
            value[0] += self.direction.x
            value[1] += self.direction.y

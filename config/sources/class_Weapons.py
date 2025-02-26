from pygame.math import Vector2
from math import pi

class Weapons:
    def load_weapons(self, obj, source, angle):
        obj.pos_weapons = []
        for value in source:
            obj.pos_weapons.append(value)

    def pos_rotation(self, obj, angle):
        result = []
        for weapon in obj.pos_weapons:
            newX, newY = self.vector_rotation(weapon, -angle / 180 * pi)
            result.append([obj.rect.centerx + newX, obj.rect.centery + newY])
        return result

    def vector_rotation(self, vector, angle):
        vector = Vector2(vector)
        return vector.rotate_rad(angle)

    def update_weapons(self, obj, angle):
        value = self.pos_rotation(obj, angle)
        for pos in value:
            pos[0] += obj.direction.x
            pos[1] += obj.direction.y

            return pos[0], pos[1]
from pygame.math import lerp


class LevelsGame:
    __instance = None

    __levels_dict = {
        "player_level": 1,
        "game_level": 1,
        "current_level": 1,
        "attack_min": 0,
        "attack_max": 2,
        "enemies_min": 6,
        "enemies_max": 15,
        "player_score": 0,
    }

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__dict__ = self.__levels_dict
        self.enemies_attack = round(
            lerp(self.enemies_min, self.enemies_max, self.attack_min / self.attack_max)
        )

    def update_levels(self):
        self.enemies_attack = round(
            lerp(self.enemies_min, self.enemies_max, self.attack_min / self.attack_max)
        )
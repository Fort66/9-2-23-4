from pygame.sprite import Group, GroupSingle

class SpriteGroups:
    __instance = None
    
    __groups_dict = {
        'player_group': GroupSingle(),
        'enemies_group': Group(),
        'player_shot_group': Group(),
        'enemies_shot_group': Group(),
        'player_guar_group': GroupSingle(),
        'enemies_guard_grop': Group(),
        'ally_group': Group(),
        'ally_shot_group': Group(),
        'ally_guar_group': Group(),
    }
    
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance
    
    
    def __init__(self):
        self.__dict__ = self.__groups_dict


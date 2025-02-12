from pygame.transform import flip, scale_by
from pygame.image import load

from icecream import ic

SCALE_VALUE = {
                1: .25,
                }

# WEAPONS_POSITION = {0: [[], []]}

HEROES = {
            1:
                {'angle':{
                            0: {
                                'sprite': scale_by(load('images/Heroes/Spaceship1/ship1.png').convert_alpha(), SCALE_VALUE[1]),
                                'weapons': [[50, 15], [50, 10]]
                                },
                            22: {
                                'sprite': scale_by(load('images/Heroes/Spaceship1/ship2.png').convert_alpha(), SCALE_VALUE[1]),
                                'weapons': [[50, 15], [50, -8]]
                                },
                            45: {
                                'sprite': scale_by(load('images/Heroes/Spaceship1/ship3.png').convert_alpha(), SCALE_VALUE[1]),
                                'weapons': [[50, 15], [50, -15]]
                                },
                            67: {
                                'sprite': scale_by(load('images/Heroes/Spaceship1/ship4.png').convert_alpha(), SCALE_VALUE[1]),
                                'weapons': [[50, 20], [50, -15]]
                                },
                            90: {
                                'sprite': scale_by(load('images/Heroes/Spaceship1/ship5.png').convert_alpha(), SCALE_VALUE[1]),
                                'weapons': [[50, 20], [50, -20]]
                                },
                            112: {
                                'sprite': flip(scale_by(load('images/Heroes/Spaceship1/ship4.png').convert_alpha(), SCALE_VALUE[1]), False, True),
                                'weapons': [[50, 20], [50, -15]]
                                },
                            135: {
                                'sprite': flip(scale_by(load('images/Heroes/Spaceship1/ship3.png').convert_alpha(), SCALE_VALUE[1]), False, True),
                                'weapons': [[50, 15], [50, -15]]
                                },
                            157: {
                                'sprite': flip(scale_by(load('images/Heroes/Spaceship1/ship2.png').convert_alpha(), SCALE_VALUE[1]), False, True),
                                'weapons': [[50, 15], [50, -8]]
                                },
                            180: {
                                'sprite': flip(scale_by(load('images/Heroes/Spaceship1/ship1.png').convert_alpha(), SCALE_VALUE[1]), False, True),
                                'weapons': [[50, -15], [50, -10]]
                                },
                            202: {'sprite': flip(scale_by(load('images/Heroes/Spaceship1/ship2.png').convert_alpha(), SCALE_VALUE[1]), False, True),
                                'weapons': [[50, -10], [50, 0]]
                                },
                            225: {
                                'sprite': flip(scale_by(load('images/Heroes/Spaceship1/ship3.png').convert_alpha(), SCALE_VALUE[1]), False, True),
                                'weapons': [[50, -15], [50, 10]]
                                },
                            247: {'sprite': flip(scale_by(load('images/Heroes/Spaceship1/ship4.png').convert_alpha(), SCALE_VALUE[1]), False, True),
                                'weapons': [[50, -10], [50, 10]]
                                },
                            270: {
                                'sprite': flip(scale_by(load('images/Heroes/Spaceship1/ship5.png').convert_alpha(), SCALE_VALUE[1]), False, True),
                                'weapons': [[50, 15], [50, -15]]
                                },
                            292: {
                                'sprite': flip(flip(scale_by(load('images/Heroes/Spaceship1/ship4.png').convert_alpha(), SCALE_VALUE[1]), False, True), False, True),
                                'weapons': [[50, 20], [50, -15]]
                                },
                            315: {
                                'sprite': flip(flip(scale_by(load('images/Heroes/Spaceship1/ship3.png').convert_alpha(), SCALE_VALUE[1]), False, True), False, True),
                                'weapons': [[50, 15], [50, -15]]
                                },
                            337: {
                                'sprite': flip(flip(scale_by(load('images/Heroes/Spaceship1/ship2.png').convert_alpha(), SCALE_VALUE[1]), False, True), False, True),
                                'weapons': [[50, 15], [50, -8]]
                                },
                            359: {
                                'sprite': flip(flip(scale_by(load('images/Heroes/Spaceship1/ship1.png').convert_alpha(), SCALE_VALUE[1]), False, True), False, True),
                                'weapons': [[50, 15], [50, -5]]
                                },
                        },
                'speed': 7,
                'rotation_speed': 10,
                }
        }


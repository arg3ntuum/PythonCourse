from _ping_pong.platform import Platform
from _ping_pong.ball import Ball

class ObjectsGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_platform(config, platform_name = 'left'):
        match platform_name:
            case 'left':
                return Platform(5, config.SCREEN_HEIGHT / 2 - config.PLATFORM_HEIGHT / 2,
                                config.PLATFORM_WIDTH, config.PLATFORM_HEIGHT, config.PLATFORM_SPEED)
            case 'right':
                return Platform(config.SCREEN_WIDTH - config.PLATFORM_WIDTH - 5,
                                config.SCREEN_HEIGHT / 2 - config.PLATFORM_HEIGHT / 2,
                                config.PLATFORM_WIDTH, config.PLATFORM_HEIGHT, config.PLATFORM_SPEED)
            case _:
                return None

    @staticmethod
    def generate_ball(config):
        return Ball(config.SCREEN_WIDTH / 2,
                    config.SCREEN_HEIGHT / 2,
                    config.BALL_RADIUS,
                    config.BALL_SPEED)
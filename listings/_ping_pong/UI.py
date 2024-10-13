import pygame
from _ping_pong.ball import Ball

class UI:
    def __init__(self):
        pass

    @staticmethod
    def draw_ball(ball:Ball, screen, color = 'White'):
        pygame.draw.circle(screen, pygame.Color(color), ball.rect.center, ball.radius)

    @staticmethod
    def draw_platform(platform, screen, color = 'White'):
        pygame.draw.rect(screen, pygame.Color(color), platform.rect)

    @staticmethod
    def draw(game, screen):
        screen.fill(game.config.BG_COLOR)
        UI.draw_platform(game.platform_left, screen)
        UI.draw_platform(game.platform_right, screen)
        UI.draw_ball(game.ball, screen)
        game.text_renderer.render(f'{game.point_left}', screen, (20, 20))
        game.text_renderer.render(f'{game.point_right}', screen, (game.config.SCREEN_WIDTH - 40, 20))
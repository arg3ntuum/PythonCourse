from email.generator import Generator

import pygame
import random
from _ping_pong.config import Config
from _ping_pong.text_renderer import TextRenderer
from _ping_pong.ball import Ball
from _ping_pong.platform import Platform
from _ping_pong.generators import ObjectsGenerator
from _ping_pong.UI import UI
from _ping_pong.engine import Engine

class Game:
    def __init__(self, config):
        self.config = config
        self.screen_size = (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
        self.platform_left = ObjectsGenerator.generate_platform(config, 'left')
        self.platform_right = ObjectsGenerator.generate_platform(config, 'right')
        self.ball = ObjectsGenerator.generate_ball(config)
        self.point_left = 0
        self.point_right = 0
        self.fps = config.FPS
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, config.FONT_SIZE)
        self.text_renderer = TextRenderer(self.font, config.FONT_COLOR)
        self.pause = False
        self.goal_time = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def update(self, screen, sound):
        self.ball.move()

        if (Engine.bounce(self.ball, self.config.SCREEN_HEIGHT)
                or Engine.collide(self.ball, self.platform_left)
                or Engine.collide(self.ball, self.platform_right)):
            pygame.mixer.Sound.play(sound)

        self.check_goal()
        UI.draw(self, screen)

        if self.pause:
            self.handle_pause()

        pygame.display.flip()
        self.clock.tick(self.fps)

    def check_goal(self):
        if self.ball.rect.centerx > self.config.SCREEN_WIDTH:
            self.point_left += 1
            self.reset_ball()
        elif self.ball.rect.centerx < 0:
            self.point_right += 1
            self.reset_ball()

    def reset_ball(self):
        self.ball.rect.x = self.config.SCREEN_WIDTH / 2 - self.ball.radius
        self.ball.rect.y = self.config.SCREEN_HEIGHT / 2 - self.ball.radius
        self.ball.dx = 0
        self.ball.dy = 0
        self.goal_time = pygame.time.get_ticks()
        self.pause = True

    def handle_pause(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.goal_time > 3000:
            self.ball.generate_new_direction()
            self.pause = False
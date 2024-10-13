import pygame
import random

from _ping_pong.config import Config
from _ping_pong.text_renderer import TextRenderer
from _ping_pong.ball import Ball
from _ping_pong.platform import Platform
from _ping_pong.game import Game
from _ping_pong.controller import Controller

if __name__ == '__main__':
    pygame.init()

    config = Config()
    game = Game(config)
    controller = Controller(game)

    screen = pygame.display.set_mode(game.screen_size)
    pygame.display.set_caption('Ping Pong')
    sound = pygame.mixer.Sound('sounds/ping.mp3')

    running = True
    while running:
        running = game.handle_events()

        keys = pygame.key.get_pressed()
        controller.do(keys)

        game.update(screen, sound)

    pygame.quit()
    exit()

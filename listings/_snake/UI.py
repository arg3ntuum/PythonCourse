import pygame

import _snake


class UI:
    SCORE_TEXT = 'SCORE: '
    GAME_OVER_TEXT = 'GAME OVER!'

    def __init__(self):
        pass

    @classmethod
    def draw_snake(cls,
                   snake_list: [[int, int]],
                   screen,
                   game_size: int,
                   snake_color='black'):

        for element in snake_list:
            pygame.draw.rect(screen,
                             pygame.Color(snake_color),
                             [element[0],
                              element[1],
                              game_size,
                              game_size])

    @classmethod
    def draw_circle(cls, screen, apple,
                    game_size: int, circle_color='red'):
        pygame.draw.circle(screen, pygame.Color(circle_color),
                           [apple.coordinates.x + game_size / 2,
                            apple.coordinates.y + game_size / 2],
                           game_size / 2)

    @classmethod
    def show_score(cls, score, screen,
                   font_name=None,
                   font_size=15,
                   text_color='white'):
        sc_font = pygame.font.SysFont(font_name, font_size)
        sc_text = sc_font.render(UI.SCORE_TEXT+ str(score), True, pygame.Color(text_color))
        screen.blit(sc_text, [5, 12])  # координати початок екрану

    @classmethod
    def game_over(cls, screen, screen_size,
                  font_name=None,
                  font_size=50,
                  text_color='white'):
        font = pygame.font.SysFont(font_name, font_size)
        text = font.render(UI.GAME_OVER_TEXT, True, pygame.Color(text_color))
        screen.blit(text, [screen_size.x / 3.2 , screen_size.y / 3])

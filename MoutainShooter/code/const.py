# C
import pygame

COLOR_PURPLE = (106, 90, 205)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 128)

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {'Level1BG0': 0,
                'Level1BG1': 1,
                'Level1BG2': 2,
                'Level1BG3': 3,
                'Level1BG4': 4,
                'Player1': 5,
                'Player1Shot': 2,
                'Player2': 5,
                'Player2Shot': 3,
                'Enemy1': 1,
                'Enemy1Shot': 2,
                'Enemy2': 1,
                'Enemy2Shot': 2,
                }
ENTITY_HEALTH = {'Level1BG0': 999,
                 'Level1BG1': 999,
                 'Level1BG2': 999,
                 'Level1BG3': 999,
                 'Level1BG4': 999,
                 'Player1': 300,
                 'Player1Shot': 1,
                 'Player2': 300,
                 'Player2Shot': 1,
                 'Enemy1': 200,
                 'Enemy1Shot': 1,
                 'Enemy2': 200,
                 'Enemy2Shot': 1,
                 }

ENTITY_SHOT_DELAY = {'Player1': 20,  # intervalo de criação de Player1Shot quando a tecla de tiro for pressionada
                     'Player2': 15,
                     'Enemy1': 100,
                     'Enemy2': 200,
                     }

PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}

PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}

PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}

PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}

PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

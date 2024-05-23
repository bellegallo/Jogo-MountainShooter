# C
import pygame

C_PURPLE = (106, 90, 205)  # Shift F6 muda o nome da variável em todos os documentos
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 128)
C_BLACK = (0, 0, 0)

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')
MENU_OPTION_SPACE = (175 + 25,
                     175 + 50,
                     175 + 75,
                     175 + 100,
                     175 + 125)
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SPEED = {
    'Level1BG0': 0,
    'Level1BG1': 1,
    'Level1BG2': 2,
    'Level1BG3': 3,
    'Level1BG4': 4,
    'Level2BG0': 0,
    'Level2BG1': 1,
    'Level2BG2': 2,
    'Level2BG3': 3,
    'Level2BG4': 4,
    'Player1': 5,
    'Player1Shot': 2,
    'Player2': 5,
    'Player2Shot': 3,
    'Enemy1': 1,
    'Enemy1Shot': 2,
    'Enemy2': 1,
    'Enemy2Shot': 2,
}

ENTITY_HEALTH = {
    'Level1BG0': 999,
    'Level1BG1': 999,
    'Level1BG2': 999,
    'Level1BG3': 999,
    'Level1BG4': 999,
    'Level2BG0': 999,
    'Level2BG1': 999,
    'Level2BG2': 999,
    'Level2BG3': 999,
    'Level2BG4': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}

ENTITY_DAMAGE = {
    'Level1BG0': 0,
    'Level1BG1': 0,
    'Level1BG2': 0,
    'Level1BG3': 0,
    'Level1BG4': 0,
    'Level2BG0': 0,
    'Level2BG1': 0,
    'Level2BG2': 0,
    'Level2BG3': 0,
    'Level2BG4': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
}

ENTITY_SCORE = {
    'Level1BG0': 0,
    'Level1BG1': 0,
    'Level1BG2': 0,
    'Level1BG3': 0,
    'Level1BG4': 0,
    'Level2BG0': 0,
    'Level2BG1': 0,
    'Level2BG2': 0,
    'Level2BG3': 0,
    'Level2BG4': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
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

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }

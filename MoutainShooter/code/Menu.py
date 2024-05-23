#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, C_PURPLE, MENU_OPTION, C_WHITE, C_YELLOW, MENU_OPTION_SPACE


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./asset/menuBG.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/menu.mp3')
        pygame.mixer_music.play(-1)
        menu_option = 0

        while True:
            # DESENHAR NA TELA
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", C_PURPLE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", C_PURPLE, ((WIN_WIDTH / 2), 120))
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), MENU_OPTION_SPACE[i]))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), MENU_OPTION_SPACE[i]))
            pygame.display.flip()

            # VERIFICAR EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # TESTAR SE ALGUMA TECLA FOI PRESSIONADA
                    if event.key == pygame.K_DOWN:  # SE A TECLA SETA PARA BAIXO FOI PRESSIONADA
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # SE A TECLA SETA PARA CIMA FOI PRESSIONADA
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

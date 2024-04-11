#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from msilib.schema import Font

import pygame.display
from pygame import Surface
from pygame import Surface, Rect

from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityMediator import EntityMediator
from code.Entityfactory import Entityfactory
from code.Player import Player
from code.const import MENU_OPTION, EVENT_ENEMY, COLOR_WHITE


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option  # OPÇÃO DO MENU
        self.entity_list: list[Entity] = []
        self.entity_list.extend(Entityfactory.get_entity('Level1BG'))
        self.entity_list.append(Entityfactory.get_entity('Player1'))
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(Entityfactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 4000)

    def run(self, ):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            # DESENHAR NA TELA
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # aqui é desenhado as entidades
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

            # texto a ser printado na tela
            self.level_text(14, f'fps:{clock.get_fps() :.0f}', COLOR_WHITE, (10, 10))
            self.level_text(14, f'entidades:{len(self.entity_list)}', COLOR_WHITE, (10, 25))
            # Atualizar tela
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos=tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

        # VERIFICAR RELACIONAMENTOS DE ENTIDADES
        EntityMediator.verify_collision(entity_list=self.entity_list)
        EntityMediator.verify_health(entity_list=self.entity_list)

        # CONFERIR EVENTOS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == EVENT_ENEMY:
                choice = random.choice(('Enemy1', 'Enemy2'))
                self.entity_list.append(Entityfactory.get_entity(choice))

    pass


def level_text(self, param, param1, COLOR_WHITE, param2):
    pass

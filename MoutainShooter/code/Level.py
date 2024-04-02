#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from random import random

import pygame.display
from pygame import Surface

from code.Entity import Entity
from code.Entityfactory import Entityfactory
from code.const import MENU_OPTION, EVENT_ENEMY


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
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(Entityfactory.get_entity('Enemy1'))
            pygame.display.flip()
        pass

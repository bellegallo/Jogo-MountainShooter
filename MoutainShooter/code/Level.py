#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.display
from pygame import Surface

from code.Entity import Entity
from code.Entityfactory import Entityfactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window :Surface = window
        self.name = name
        self.mode = menu_option  # OPÇÃO DO MENU
        self.entity_list: list[Entity] = []
        self.entity_list.extend(Entityfactory.get_entity('Level1BG'))

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass

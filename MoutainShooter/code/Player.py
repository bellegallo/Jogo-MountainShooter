#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Entity import Entity
from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_RIGHT, \
    PLAYER_KEY_LEFT


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:  # Se a tecla seta para cima for pressionada
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[
            PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:  # Se a tecla seta para baixo for pressionada
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[
            PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:  # Se a tecla seta para esquerda for pressionada
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_RIGHT[
            self.name]] and self.rect.right < WIN_WIDTH:  # Se a tecla seta para direita for pressionada
            self.rect.centerx += ENTITY_SPEED[self.name]

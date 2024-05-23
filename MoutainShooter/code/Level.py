#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
from msilib.schema import Font

import pygame.display
from pygame import Surface, Rect

from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityMediator import EntityMediator
from code.Entityfactory import Entityfactory
from code.Player import Player
from code.const import MENU_OPTION, EVENT_ENEMY, C_WHITE, WIN_HEIGHT, C_GREEN, C_CYAN, EVENT_TIMEOUT


class Level:
    def __init__(self, window: Surface, name: str, menu_option: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.mode = menu_option  # OPÇÃO DO MENU
        self.entity_list: list[Entity] = []
        self.entity_list.extend(Entityfactory.get_entity(self.name + 'BG'))
        player = Entityfactory.get_entity('Player1')
        player.score = player_score[0]  # score do player1
        self.entity_list.append(player)
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = Entityfactory.get_entity('Player2')
            player.score = player_score[1]  # score do player 2
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, 4000)
        self.timeout = 30000  # 30 segundos de fase
        pygame.time.set_timer(EVENT_TIMEOUT, 100)  # 100ms verifica a condição de vitória/derrota da fase

    def run(self, player_score: list[int]):
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

                if ent.name == 'Player1':
                    # noinspection PyTypeChecker
                    self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}', C_GREEN, (10, 25))
                if ent.name == 'Player2':
                    # noinspection PyTypeChecker
                    self.level_text(14, f'Player2 - Health: {ent.health} | Score: {ent.score}', C_CYAN, (10, 45))
            if self.timeout == 0:
                return True

            # texto a ser exibido na tela
            # noinspection PyTypeChecker
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s ', C_WHITE, (10, 5))
            # noinspection PyTypeChecker
            self.level_text(14, f'fps:{clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            # noinspection PyTypeChecker
            self.level_text(14, f'entidades:{len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            # Atualizar tela
            pygame.display.flip()

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

                if event.type == EVENT_TIMEOUT:  # acontece a cada 100ms
                    self.timeout -= 100  # timeout começa com 20000
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos=tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

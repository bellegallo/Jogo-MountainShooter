from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.PlayerShot import PlayerShot
from code.const import WIN_WIDTH


class EntityMediator:  # Essa clase vai ser responsável por mediar as colisões
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0  # faz a vida chegar a 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:  # percorra todas as entidades dentro da lista de entidades
            if ent.health <= 0:  # se a vida de uma delas for < = 0 será removida a entidade
                entity_list.remove(ent)

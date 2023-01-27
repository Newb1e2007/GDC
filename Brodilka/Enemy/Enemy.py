import pygame
import random
import math
from class_Point import *
from labirint_shortest_way import bfs


class Enemy:
    def __init__(self, entity_type, pos, speed=2, size=Point(30, 30), visual=(0, 0, 0), hp=None, follow=[True, 100], field=None, facing=Point(0, 1)):
        self.type = entity_type  # не несёт смысловой нагрузки
        self.hp = hp  # не реализовано

        self.alive = 1
        self.size = size  # как бы размер хитбокса
        self.pos = pos
        self.facing = facing  # не используется, должна показывать куда смотрит сущность
        self.vel = Point(speed, speed)  # величина пикселей на которую сущность передивгается за ход

        # пока не релизовано
        if isinstance(visual, tuple):
            self.textured = False   # обозначает есть ли текстуры у объекта или он просто цветной квадрат
            self.color = visual
        else:
            self.textured = True
            self.images = []
            for i in range(visual[2]):
                self.images.append(pygame.image.load(f'{visual[0]}{visual[1]}{i}.png').convert_alpha())  # добавляет в спимок изображений новое
                self.images[-1] = pygame.transform.scale(self.images[i], (self.size.x, self.size.y))  # делает изображение размнром с хитбокс
            self.animationCount = 0
            self.animationFrequency = visual[3]  # отвечает за частоту смены анимаци

        self.path_len = None
        self.pathCount = 0  # позиция в пути сущности
        self.path = []
        self.get_path(field)

        self.follow = follow[0]  # будет ли сущность следовать за кем-то в каком-то радиусе
        if self.follow:
            self.vision_span = follow[1]
        else:
            self.vision_span = None

    def get_path(self, field=None):
        self.pathCount = 0
        path = [Point()]
        if field is None:
            self.path_len = random.randint(5, 30)
            directions = self._get_directions(field)  # список возможных направлений, вынесено сюда чтобы не ругался
            new_dir = random.choice(directions)
            len_iter = 5
            for i in range(self.path_len):
                if i % len_iter == 0:
                    directions = self._get_directions(field)
                    new_dir = random.choice(directions)
                if new_dir == 1 and path[i - 1] != Point(-1, 0):
                    path.append(Point(1, 0))
                elif new_dir == 2 and path[i - 1] != Point(1, 0):
                    path.append(Point(-1, 0))
                elif new_dir == 3 and path[i - 1] != Point(0, -1):
                    path.append(Point(0, 1))
                elif new_dir == 4 and path[i - 1] != Point(0, 1):
                    path.append(Point(0, -1))
                else:
                    path.append(Point(0, 0))
        else:
            self.path_len = random.randint(10, 20)
            self.path_len *= 3
            i = 0
            new_dir = random.randint(0, 4)
            while len(path) < self.path_len:
                if i % 12 == 0:
                    new_dir = random.randint(0, 4)
                if new_dir == 1 and path[-1] != Point(-1, 0):
                    path.append(Point(1, 0))
                elif new_dir == 2 and path[-1] != Point(1, 0):
                    path.append(Point(-1, 0))
                elif new_dir == 3 and path[-1] != Point(0, -1):
                    path.append(Point(0, 1))
                elif new_dir == 4 and path[-1] != Point(0, 1):
                    path.append(Point(0, -1))
                else:
                    path.append(Point(0, 0))
                i += 1

#        paths = paths + [-i for i in paths[::-1]]  # чтобы сущность возвращалась в исходную точку
        self.path_len = len(path)
        self.path = path

    def _get_directions(self, field):
        directions = [0]  # по умолчанию сущность может остаться там, где была
        if field.is_allowed(Point(self.pos.x + self.vel.x, self.pos.y), self.size, False):
            directions.append(1)
        elif field.is_allowed(Point(self.pos.x - self.vel.x, self.pos.y), self.size, False):
            directions.append(2)
        elif field.is_allowed(Point(self.pos.x, self.pos.y + self.vel.y), self.size, False):
            directions.append(3)
        elif field.is_allowed(Point(self.pos.x, self.pos.y - self.vel.y), self.size, False):
            directions.append(4)
        return directions

    def pos_update(self, field=None, player_pos=None, entities=None):
        if self.follow and player_pos is not None:  # можем сделать follow=True, но при этом если ничего не задать,
            # то и следовать сущность не будет
            dx = self.pos.x + self.size.x//2 - player_pos.x
            dy = self.pos.y + self.size.y//2 - player_pos.y
            #print((dx*dx + dy*dy)**0.5)
            if (dx*dx + dy*dy)**0.5 <= self.vision_span:
                self.path = bfs(field, field.to_log(self.pos), field.to_log(player_pos), None, True)
                print(self.path)
                #self.vel = Point(field.size.x+field.size.y, field.size.x+field.size.y)
                #self.pathCount = 0
                pass
        if self.pathCount >= self.path_len:
            self.get_path(field)
        x = self.pos.x + self.path[self.pathCount].x * self.vel.x
        y = self.pos.y + self.path[self.pathCount].y * self.vel.y
        if field.is_allowed(Point(x, y), self.size):
            self.pos = Point(x, y)
        self.pathCount += 1

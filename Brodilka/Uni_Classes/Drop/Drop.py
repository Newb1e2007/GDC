import pygame
import random
from math import fabs
from class_Point import *


class Drop:
    def __init__(self, pos=Point(), hitbox_size=Point(20, 20), visual=(0, 0, 0), jumping=True, amount=1, random_spawn=False, field_size=None, field=None, player_pos=None):
        self.size = hitbox_size
        if not random_spawn:
            self.pos = pos
        else:
            # координата задаётся рандомно в пределах поля, если позиция игрока находится внутри хитбокса дропа,
            # то координата выбирается заново
            if field is None:
                x = random.randint(0, field_size.x - self.size.x)
                y = random.randint(0, field_size.y - self.size.y)
                while -self.size.x < x - player_pos.x < self.size.x or -self.size.y < y - player_pos.y < self.size.y:
                    x = random.randint(0, field_size.x - self.size.x)
                    y = random.randint(0, field_size.y - self.size.y)
            # координата задаётся рандомно в пределах координат поля, если данная позиция поля не разрешена,
            # то координата выбирается заново
            else:
                x = random.randint(0, field.size.x)
                y = random.randint(0, field.size.y)
                while not field.isalowed(Point(x, y)):
                    x = random.randint(0, field.size.x)
                    y = random.randint(0, field.size.y)
            self.pos = Point(x, y)

        self.flyDir = -1  # для реализации анимации подлетания - взлёт или наоборот
        if not jumping:
            self.flyDir = 0
        self.z = 0  # координата в 3-х мерном измерении, не влияет на координаты на поле, для красивой анимации

        self.amount = amount

        # в visual передаётся либо кортеж (по умолчанию) с цветом заливки (по умолчанию чёрный),
        # либо список из: пути, образца названия спрайта, количества изображений, частоты смены текстур
        # (по умолчанию 10, чем больше значение, тем реже меняется текстура)
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
            self.animationFrequency = visual[3]  # отвечает за частоту смены анимаций

    def draw(self, win):
        if self.z == 0 or self.z == 10:  # реализация анимации подлетания
            self.flyDir *= -1
        self.z += self.flyDir

        if not self.textured:
            pygame.draw.rect(win, self.color, (self.pos.x, self.pos.y+self.z, self.size.x, self.size.y))
        else:
            win.blit(self.images[self.animationCount//self.animationFrequency], (self.pos.x, self.pos.y+self.z))
            self.animationCount = (self.animationCount+1) % (len(self.images)*self.animationFrequency)
        pygame.display.update()

import pygame
import Player.Auxiliary_Classes.Inventory as Inventory
from CONFIG.CONST import *


class _slot:
    def __init__(self, x, y, width, height, images, num, surface, item=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image1 = images[0]
        self.image1 = pygame.transform.scale(self.image1, (self.width, self.height))
        self.image2 = images[1]
        self.image2 = pygame.transform.scale(self.image2, (self.width, self.height))
        self.image3 = images[2]
        self.image3 = pygame.transform.scale(self.image3, (self.width, self.height))
        self.rect = self.image1.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.surface = surface
        self.slot_surface = pygame.Surface((self.width, self.height))
        self.num = num
        self.item = item
        slots_lst.append(self)
        # добавить в файл

    # обрабатывание процесса нажатия/наведения и т.п., вызывается каждым кадром
    def process(self):
        pos = pygame.mouse.get_pos()  # получение позиции мыши

        if self.rect.collidepoint(pos):
            self.surface.blit(self.image2, (self.x, self.y))
            pygame.display.update(self.rect)
            if pygame.mouse.get_pressed(num_buttons=3)[0]:  # нажата левая кнопка мыши
                self.surface.blit(self.image3, (self.x, self.y))
                self.item.using_from_inv()
                pygame.display.update(self.rect)
        else:
            self.surface.blit(self.image1, (self.x, self.y))
            pygame.display.update(self.rect)

    def adding_item(self, item):
        self.item = item
        # изменить состояние в файле
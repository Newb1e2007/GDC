import pygame
from CONST import *
import Slot


class Inventory:
    def __init__(self, x, y, width, height, horizontal_indentation, vertical_indentation, margin, rows, col, hotkey, surface, background, slot_images, max_weight=10, items=None):
        self.rect = None
        # корды верхнего левого угла
        self.x = x
        self.y = y

        # размеры в пикселях
        self.width = width
        self.height = height

        # параметры инвентаря
        self.rows = rows
        self.col = col
        self.slots = rows*col
        self.hotkey = hotkey
        self.max_weight = max_weight  # 10 kg
        self.currentWright = 0
        self.slot_images = slot_images

        self.horizontal_indentation = horizontal_indentation
        self.vertical_indentation = vertical_indentation
        self.margin = margin
        self.slot_width = (self.width - self.horizontal_indentation * 2 - self.margin * (self.col - 1)) / self.col
        self.slot_height = (self.height - self.vertical_indentation * 2 - self.margin * (self.rows - 1)) / self.rows

        self.slot_x = self.horizontal_indentation
        self.slot_y = self.vertical_indentation

        # изображения
        self.bg = background
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

        # поверхности
        self.surface = surface  # предыдущая поверхность
        self.inventorySurface = pygame.Surface((self.width, self.height))

        # self.inventorySurface.blit(self.bg, (self.x, self.y))

        # слоты
        inventory_lst = [[0 for _ in range(self.rows)] for _ in range(self.col)]

    def opening(self):
        self.inventorySurface.blit(self.bg, (self.x, self.y))
        self.surface.blit(self.inventorySurface, (self.x, self.y))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self._drawing_slots()
        for slot in slots_lst:
            Slot._slot.process(slot)

    def put_in_the_inventory(self, item):
        for slot in slots_lst:
            if slot.item is not None:
                slot.item = item
                break

    def _drawing_slots(self):
        for i in range(self.slots):
            # item = что-то там из файла
            Slot._slot(self.slot_x, self.slot_y, self.slot_width, self.slot_height, self.slot_images, i, self.inventorySurface, item=None)
            self.slot_x += (self.margin + self.slot_width)
            self.slot_y += (self.margin + self.slot_height)

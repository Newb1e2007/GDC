import pygame
from CONST import *
import class_Point
import class_Inventory

# скины на игрока (мб сделать в константах)
evgenii = [pygame.image.load('images/oaoaoaoaoaoaoaooa.png').convert_alpha(),
           ]


class Player:
    def __init__(self, x, y, width, height, speed, damage, hp, armor, energy, inventory_parameters, name=None):
        # позиция игрока   потом доработать с классом Point
        self.x = x
        self.y = y

        # размеры хитбокса игрока
        self.width = width
        self.height = height

        # создание хитбокса игрока
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.surface = pygame.Surface((self.width, self.height))

        # статы игрока
        self.speed = speed  # скорость
        self.currentSpeed = speed
        self.damage = damage  # урон
        self.currentDamage = damage
        self.hp = hp  # здоровье
        self.currentHp = hp
        self.armor = armor  # броня
        self.currentArmor = armor
        self.energy = energy  # энергия(для подсчета зарядов/ударов)
        self.currentEnergy = energy

        # бабки
        self.cash = 0
        self.currentCash = 0
        self.coins = 0

        # инвентарь
        self.items = {}
        self.inventory = self._creating_inventory(inventory_parameters)

        # скин
        if name is None:
            name = evgenii
        self.setting_skin(name)

    def _creating_inventory(self, inv_par):
        return class_Inventory.Inventory(inv_par[0], inv_par[1], inv_par[2], inv_par[3], inv_par[4], inv_par[5], inv_par[6], inv_par[7], inv_par[8], inv_par[9], inv_par[10], inv_par[11], inv_par[12], inv_par[13], inv_par[14])

    def setting_skin(self, name):
        self.skin = name
        self.defaultPosition = name[0]
        self.defaultPosition = pygame.transform.scale(self.defaultPosition, (self.width, self.height))
        # self.surface.blit(self.defaultPosition, (self.x, self.y))

    def drawing_player_in_game(self, frame, mother_surface):
        self.skinImage = self.skin[frame]
        self.surface.blit(self.skinImage, (self.x, self.y))
        mother_surface.blit(self.surface, (self.x, self.y))



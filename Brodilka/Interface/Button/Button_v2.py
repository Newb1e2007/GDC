import pygame
from CONFIG.CONST import *


class Button:
    # тут будут создаваться кнопки6 задаваться их параметры и изображения, а так же функции их нажатия

    def __init__(self, x, y, width, height, images, onclickFunction, onePress, surface, name='defaultButton'):
        # x, y - корды верхней левой клетки; width, height - размеры клетки; image - изображение клетки;
        #    surface - поверхность клетки; onclickFunction - функция, выполняемая кнопкой; onePress - зажимная/нет
        # print(parameter_lst, len(parameter_lst))
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
        self.button_surface = pygame.Surface((self.width, self.height))
        self.surface.blit(self.button_surface, (self.x, self.y))

        self.name = name

        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.alreadyPressed = False
        self.button_surface.blit(self.image1, (self.x, self.y))
        self.surface.blit(self.button_surface, (self.x, self.y))
        buttons.append(self)
        print('True')

    # обрабатывание процесса нажатия/наведения и т.п., вызывается каждым кадром
    def process(self):
        pos = pygame.mouse.get_pos()  # получение позиции мыши

        # self.button_surface.fill((200, 200, 100))
        # проверка на нажатие/наводку
        if self.rect.collidepoint(pos):
            # self.button_surface.fill((200, 200, 0))
            # self.button_surface.blit(self.image2, (self.x, self.y))
            # self.surface.blit(self.button_surface, (self.x, self.y))
            self.surface.blit(self.image2, (self.x, self.y))
            pygame.display.update(self.rect)
            print(self.name, 'updated')
            # print('hower')
            if pygame.mouse.get_pressed(num_buttons=3)[0]:  # нажата левая кнопка мыши
                # self.button_surface.fill((200, 200, 0))
                # self.button_surface.blit(self.image3, (self.x, self.y))
                # self.surface.blit(self.button_surface, (self.x, self.y))
                self.surface.blit(self.image3, (self.x, self.y))
                pygame.display.update(self.rect)
                print(self.name, 'updated')
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        else:
            # self.button_surface.fill((200, 200, 0))
            # self.button_surface.blit(self.image1, (self.x, self.y))
            # self.surface.blit(self.button_surface, (self.x, self.y))
            self.surface.blit(self.image1, (self.x, self.y))
            pygame.display.update(self.rect)
            print(self.name, 'updated')

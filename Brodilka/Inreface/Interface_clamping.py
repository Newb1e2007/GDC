import pygame
from CONFIG.CONST import *
import Inreface.Button.Button_v2
import sys

# import Field

# мы будем прятать курсор мыши в игре, но если пользователь будет нажимать esc то мы будем его показывать вместе с меню
# для нажатия на кнопки
pygame.init()
fpsClock = pygame.time.Clock()
width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
# menu_surface = pygame.Surface((1000, 600))
# menu_surface.fill((200, 200, 100))
# screen.blit(menu_surface, (0, 0))
pygame.display.update()
font = pygame.font.SysFont('Arial', 15)

new_game_img = [pygame.image.load('images/new_game_button_1.png').convert_alpha(),
                pygame.image.load('images/new_game_button_2.png').convert_alpha(),
                pygame.image.load('images/new_game_button_3.png').convert_alpha()
                ]
exit_img = [pygame.image.load('images/exit_button_1.png').convert_alpha(),
            pygame.image.load('images/exit_button_2.png').convert_alpha(),
            pygame.image.load('images/exit_button_3.png').convert_alpha()
            ]
retry_img = [pygame.image.load('images/retry_button_1.png').convert_alpha(),
             pygame.image.load('images/retry_button_2.png').convert_alpha(),
             pygame.image.load('images/retry_button_3.png').convert_alpha()
             ]
shop_img = [pygame.image.load('images/shop_button_1.png').convert_alpha(),
            pygame.image.load('images/shop_button_2.png').convert_alpha(),
            pygame.image.load('images/shop_button_3.png').convert_alpha()
            ]
wallpaper_img = pygame.image.load('images/wallpaper.png').convert_alpha()


class new_menu:
    # ОЧЕНЬ ВАЖНО: объекты класса new_menu это не поверхности, это само меню, поверхность меню - атрибут класса

    def __init__(self, x, y, width, height, image, mother_screen, **kwargs):  # button1=(x, y, width, height, images, onklick_fun)
        # корды
        self.x = x
        self.y = y
        # размеры
        self.width = width
        self.height = height
        # изображение поверхности
        self.image = image
        # предыдущая по слою поверхность
        self.mother_screen = mother_screen
        # кнопки
        # print(kwargs)
        self.buttons_dict = kwargs
        self.buttons_lst = []
        # создание поверхности меню
        # self.newSurface = pygame.Surface((self.width, self.height))
        # self.newSurface.blit(self.image, (self.x, self.y))
        # self.mother_screen.blit(self.newSurface, (self.x, self.y))

        # создание поверхности меню
        self.menu_surface = pygame.Surface((self.width, self.height))
        self.menu_surface.blit(self.image, (self.x, self.y))
        self.mother_screen.blit(self.menu_surface, (self.x, self.y))
        # pygame.display.update()

    def adding_button(self, parameter_lst):
        parameter_lst.append(self.menu_surface)
        print(parameter_lst, len(parameter_lst))
        self.buttons_lst.append(Button_v2.Button(parameter_lst[0], parameter_lst[1], parameter_lst[2], parameter_lst[3], parameter_lst[4], parameter_lst[5], parameter_lst[6], parameter_lst[7]))

    def placing_buttons(self):
        for button in self.buttons_dict.keys():
            parameter_lst = self.buttons_dict[button]
            self.adding_button(parameter_lst)

        for button in self.buttons_lst:
            button.process()
        self.mother_screen.blit(self.menu_surface, (self.x, self.y))
        # pygame.display.update()


    # def set_button(self, button_name, x, y, width, height, images, onklick_fun):
    # Button.Button(x, y, width, height, images, self.surface, onklick_fun)


# функции, исполняемые кнопками
def new_game():
    print('start')
    # main()


def store():
    print('buy')
    # будет вызывать функцию для открытия магазина


def options():
    print('options')
    # будет вызывать функцию для открытия настроек


def exit():
    print('exit')
    pygame.quit()
    sys.exit()


def retry():
    print('retry')


# создание объектов класса кнопка
# new_game_button = Button_v2.Button([30, 150, 200, 60, new_game_img, menu_surface, new_game, False])
# exit_button = Button_v2.Button([260, 150, 200, 60, exit_img, menu_surface, exit, False])
# shop_button = Button_v2.Button([490, 150, 200, 60, shop_img, menu_surface, store, False])
# retry_button = Button_v2.Button([720, 150, 200, 60, retry_img, menu_surface, retry, False])
# pygame.display.update()
menu_mode = -1

while True:
    # screen.fill((200, 200, 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print('menu opened')
                if menu_mode == 1:
                    menu_mode = 0
                else:
                    menu_mode = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                print('manu closed')
                menu_mode = -1

    if menu_mode == 1:
        menu = new_menu(0, 0, 1000, 600, wallpaper_img, screen,
                        new_game_button=[30, 150, 200, 60, new_game_img, new_game, False],
                        exit_button=[260, 150, 200, 60, exit_img, exit, False],
                        shop_button=[490, 150, 200, 60, shop_img, store, False],
                        retry_button=[720, 150, 200, 60, retry_img, retry, False]
                        )
        menu.placing_buttons()
        # pygame.display.update()
        for button in buttons:
            button.process()
        screen.blit(menu.menu_surface, (0, 0))
        pygame.display.update()
    elif menu_mode == 0:
        for button in buttons:
            button.process()
        screen.blit(menu.menu_surface, (0, 0))
        pygame.display.update()
    if menu_mode == -1:
        screen.fill((200, 200, 100))
        pygame.display.update()

    fpsClock.tick(FPS)

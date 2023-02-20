import pygame as pg
import Interface.Button.Button_v2 as class_button_v2
import Interface.Button.Button_func.trail_menu_buttons as tmb
from CONFIG.CONST import *
import os


pg.init()
fpsClock = pg.time.Clock()
width, height = 1000, 600
screen = pg.display.set_mode((width, height))
pg.display.update()
font = pg.font.SysFont('Arial', 15)

os.chdir('/Users/user/Documents/GitHub/GDC/Brodilka')  # iMac-User/MacOS/Пользователи/User/Документы/GitHub/GDC/Brodilka
new_game_img = [pg.image.load('Images/Button_img/new_game_button_1.png').convert_alpha(),
                pg.image.load('Images/Button_img/new_game_button_2.png').convert_alpha(),
                pg.image.load('Images/Button_img/new_game_button_3.png').convert_alpha()
                ]
exit_img = [pg.image.load('Images/Button_img/exit_button_1.png').convert_alpha(),
            pg.image.load('Images/Button_img/exit_button_2.png').convert_alpha(),
            pg.image.load('Images/Button_img/exit_button_3.png').convert_alpha()
            ]
retry_img = [pg.image.load('Images/Button_img/retry_button_1.png').convert_alpha(),
             pg.image.load('Images/Button_img/retry_button_2.png').convert_alpha(),
             pg.image.load('Images/Button_img/retry_button_3.png').convert_alpha()
             ]
shop_img = [pg.image.load('Images/Button_img/shop_button_1.png').convert_alpha(),
            pg.image.load('Images/Button_img/shop_button_2.png').convert_alpha(),
            pg.image.load('Images/Button_img/shop_button_3.png').convert_alpha()
            ]
wallpaper_img = pg.image.load('Images/Interface_img/wallpaper.png').convert_alpha()
skin_img = pg.image.load('Images/Interface_img/skin.png').convert_alpha()


class Menu:
    def __init__(self, motherSurf, pos, size, image, any_other_img=False, any_buttons=False):
        # screen, (10, 10), (100, 60), surf_img, any_other_img=True, buttons=True)

        # предыдущая поверхность
        self.motherSurf = motherSurf

        # корды
        self.x = pos[0]
        self.y = pos[1]

        # размеры
        self.width = size[0]
        self.height = size[1]

        # изображение самой поверхности
        self.image = image
        self.image = pg.transform.scale(self.image, (self.width, self.height))

        # статы
        self.any_other_img = any_other_img
        self.any_buttons = any_buttons
        self.superimposed_img = None
        self.buttons = None
        self.buttons_lst = []

        # создание
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.menuSurf = pg.Surface((self.width, self.height))
        self.menuSurf.blit(self.image, (self.x, self.y))
        self.motherSurf.blit(self.menuSurf, (self.x, self.y))

    def add_img(self, *args):  # [pos, size, surf_img]
        self.any_other_img = True
        self.superimposed_img = args
        for img in self.superimposed_img:
            surf_img = img[2]
            pos = img[0]
            size = img[1]
            surf_img = pg.transform.scale(surf_img, size)
            self.menuSurf.blit(surf_img, pos)
        self.motherSurf.blit(self.menuSurf, (self.x, self.y))

    def add_button(self, *args):  # [pos, size, images, onclick_fun, onePress, name]
        # x, y, width, height, images, onclickFunction, onePress, surface, name='defaultButton' - параметры самой кнопки
        self.any_buttons = True
        self.buttons = args
        for button in self.buttons:
            self.buttons_lst.append(
                class_button_v2.Button(button[0][0], button[0][1], button[1][0], button[1][1], button[2], button[3],
                                       button[4], self.menuSurf, button[5]))

        self.motherSurf.blit(self.menuSurf, (self.x, self.y))


menu_lst = []
running = True
menu_mode = -1
esc_counter = 0

while running:
    screen.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                esc_counter += 1
                if esc_counter%2 == 0:
                    menu_mode = -1
                    print('menu closed')
                else:
                    if menu_mode == 1:
                        menu_mode = 0
                    else:
                        menu_mode = 1
                        print('menu opened')

    if menu_mode == 1 or menu_mode == 0:
        if menu_mode == 1:
            menu = Menu(screen, (20, 20), (700, 500), wallpaper_img)
            menu.add_img([(40, 40), (100, 50), skin_img])
            menu.add_button([(40, 500), (100, 40), new_game_img, tmb.new_game, False, 'new_game_button'],
                            [(200, 500), (100, 40), exit_img, tmb.exit, False, 'exit_button'],
                            [(360, 500), (100, 40), shop_img, tmb.store, False, 'shop_button'],
                            [(520, 500), (100, 40), retry_img, tmb.retry, False, 'retry_button']
                            )
            for button in menu.buttons_lst:
                menu.menuSurf.blit(button.button_surface, (button.x, button.y))
                pg.display.update(menu.rect)

            pg.display.update(menu.rect)

        for button in menu.buttons_lst:
            button.process()
        screen.blit(menu.menuSurf, (20, 20))
        pg.display.update(menu.rect)
    else:
        pg.display.update()

    fpsClock.tick(FPS)


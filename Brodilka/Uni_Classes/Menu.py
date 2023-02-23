import pygame as pg
import Interface.Button.Button_v2 as class_button_v2
import Interface.Button.Button_func.trail_menu_buttons as tmb
from CONFIG.CONST import *
import os  # импорт для изменения директории в будущем


pg.init()
fpsClock = pg.time.Clock()
width, height = 1000, 600
screen = pg.display.set_mode((width, height))
pg.display.update()
font = pg.font.SysFont('Arial', 15)

os.chdir('/Users/user/Documents/GitHub/GDC/Brodilka')  # изменение директории, тк нам надо уйти из Uni_Classes
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
# везде по 3 изображения - дефолт, наведение и зажатие
wallpaper_img = pg.image.load('Images/Interface_img/wallpaper.png').convert_alpha()
skin_img = pg.image.load('Images/Interface_img/skin.png').convert_alpha()  # просто тестовое изображение6 потом было бы на мой взгляд удобно добавлять какие-либо изображения(текст например) на поверхность нашего меню


class Menu:
    """'Этот класс создает настраиваемую поверхность, рассчитываемую под меню"""
    def __init__(self, motherSurf, pos, size, image, any_other_img=False, any_buttons=False):
        # screen, (10, 10), (100, 60), surf_img, any_other_img=True, buttons=True)

        # предыдущая поверхность(поверхность, на которой находится menuSurf)
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
        self.superimposed_img = None  # параметры картинок
        self.buttons = None  # параметры кнопок
        # self.buttons_lst = []  # сами ссылки на кнопки

        # создание
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.menuSurf = pg.Surface((self.width, self.height))
        self.menuSurf.blit(self.image, (self.x, self.y))
        self.motherSurf.blit(self.menuSurf, (self.x, self.y))

        # объекты для рендерига
        self.buttons_lst = []
        self.additional_img_lst = []

    def add_img(self, *args):  # [pos, size, surf_img]
        """Передавая в качестве аргументов n-ное кол-во списков параметров, вы создаете новое изображение на поверхности нашего меню"""
        self.any_other_img = True
        self.superimposed_img = args
        for img in self.superimposed_img:
            surf_img = img[2]
            self.additional_img_lst.append(surf_img)
            pos = img[0]
            size = img[1]
            surf_img = pg.transform.scale(surf_img, size)
            self.menuSurf.blit(surf_img, pos)
        self.motherSurf.blit(self.menuSurf, (self.x, self.y))

    def add_button(self, *args):  # [pos, size, images, onclick_fun, onePress, name]
        # x, y, width, height, images, onclickFunction, onePress, surface, name='defaultButton' - параметры самой кнопки
        """Передавая в качестве аргументов n-ное кол-во списков параметров, вы создаете новую кнопку на поверхности нашего меню"""
        self.any_buttons = True
        self.buttons = args
        for button_par in self.buttons:
            self.buttons_lst.append(
                class_button_v2.Button(button_par[0][0], button_par[0][1], button_par[1][0], button_par[1][1], button_par[2], button_par[3],
                                       button_par[4], self.menuSurf, button_par[5]))

        self.motherSurf.blit(self.menuSurf, (self.x, self.y))


menu_lst = []
running = True
menu_mode = -1  # -1 - меню не существует; 0 - существует, открыто; 1 - существует, закрыто => надо открыть
esc_counter = 0  # меню открывается по кнопке esc

# Понятно, что в самой игре все это будет реализованно по-другому, но тут я просто проверяю функциональность меню
# что бы открыть меню в этой программе вы должны нажать esc, и еще раз что бы закрыть. По идее все должно работать, но кнопки почему-то не появляются. Наверное ошибка очень простая и тупая, но мы не можем ее найти(

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
            menu_lst.append(menu)
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
            menu.menuSurf.blit(button.button_surface, (button.x, button.y))
            button.process()

        screen.blit(menu.menuSurf, (20, 20))
        pg.display.update(menu.rect)
    else:
        pg.display.update()

    fpsClock.tick(FPS)

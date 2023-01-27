# размеры объектов
DISPLAY_WIDTH = None  #
DISPLAY_HEIGHT = None  #

LEVEL_WIDTH = 360  #
LEVEL_HEIGHT = 480  #

cell_size = None  #
wall_size = None  #
rows = None  # в единицах поля
col = None  #

# фпс и др
FPS = 60

# игрок
PLAYER_CODE = {"player": [0, 0, 0, 0]}  # 

# уровни
level_list = []

# кнопки
buttons = []  # потом заменить мб на словарь, а пока что [0] = 'выход' и т.п.
buttons_cords = [(30, 30), (30, 230), (30, 430), (30, 630)]
# будет размеры кнопок

# слоты
slots_lst = []

# цвета -------------------------------------------------------------------------
bg_color = ()
menu_color = ()

# назначение клавиш -------------------------------------------------------------
gamekeys = {'go_up': 'W',
            'go_dawn': 'S',
            'go_left': 'A',
            'go_right': 'D',
            'use_menu': 'ESC',
            'use_inventory': 'TAB',
            'use_item': 'E',
            'shoot': 'SPACE',
            'drop': 'Q'
            }

# вес предметов -----------------------------------------------------------------
max_weight = 10
health_potion = 0.5
energy_potion = 0.5
armor = 3
sword = 2
crossbow = 3
arrow = 0.05
axe = 4


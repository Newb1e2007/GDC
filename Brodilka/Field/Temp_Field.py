import pygame
# from CONST import *
from Uni_Classes.Point import *

d1 = ('00', '10', '20', '30')  # должно быть в CONST
d2 = ('11', '21', '31')


class Field:
    def __init__(self, pos, cell_size, size, cells=('', [d1, d2], False, 0), visual=(False, (0, 255, 0), (255, 0, 0))):
        self.size = size
        self.fiz_size = Point()
        self.cell_size = cell_size

        self.start_pos = pos

        self.cells = []
        self._get_cells(cells)

        try:
            self.floor = cells[1][0]
            self.wall = cells[1][1]
        except:
            self.floor = {'00':(cell_size.x, cell_size.x), '10':(cell_size.x, cell_size.y), '20':(cell_size.y, cell_size.x), '30':(cell_size.y, cell_size.y)}
            self.wall = {'11':(cell_size.x, cell_size.y), '21':(cell_size.y, cell_size.x), '31':(cell_size.y, cell_size.y)}

        self._get_visual(visual)

    def _get_cells(self, cells):
        # cells = [file_name, keys=[(floor_id, ...), (wall_id, ...)], full=True/False, degree_of_crushing=1]
        try:
            full = cells[2]
        except:
            full = False
        try:
            degree_of_crushing = cells[3]
        except:
            degree_of_crushing = 0
        with open(f'{cells[0]}.txt', "r") as cells:
            for i in range(self.size.y):
                row = cells.readline().split()
                if not full:
                    f_row = []
                    for j in range(len(row)):
                        if j % 2 == 1 and degree_of_crushing > 0:
                            f_row.append(row[j])
                        f_row.append(row[j])
                    if i % 2 == 1 and degree_of_crushing > 0:
                        self.cells.append(f_row)
                    self.cells.append(f_row)
                else:
                    self.cells.append(row)
        self.fiz_size.x = len(self.cells[0])//2 * (self.cell_size.x + self.cell_size.y) + self.cell_size.y
        self.fiz_size.y = len(self.cells) // 2 * (self.cell_size.x + self.cell_size.y) + self.cell_size.y

    def draw(self, win):
        pos = Point(self.start_pos.x + self.fiz_size.x, self.start_pos.y)
        size = Point()
        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])-1, -1, -1):
                if self.cells[i][j] in self.floor:
                    if not self.textured:
                        color = self.floor_color
                    size = self.floor[self.cells[i][j]]
                else:
                    if not self.textured:
                        color = self.wall_color
                    size = self.wall[self.cells[i][j]]

                if not self.textured:
                    pygame.draw.rect(win, color, (pos.x - size[0], pos.y, size[0]-2, size[1]-2))
                else:
                    win.blit(self.textures[self.cells[i][j]], (pos.x - size[0], pos.y))
                pos = Point(pos.x - size[0], pos.y)
            pos = Point(self.start_pos.x + self.fiz_size.x, pos.y + size[1])

    def to_log(self, pos):
        pos = Point(pos.x - self.start_pos.x, pos.y - self.start_pos.y)
        a = self.cell_size.x + self.cell_size.y
        if 0 <= pos.x % a < self.cell_size.y:
            b = 0
        else:
            b = 1
        x = 2 * (pos.x // a) + b
        if 0 <= pos.y % a < self.cell_size.y:
            b = 0
        else:
            b = 1
        y = 2 * (pos.y // a) + b
        return Point(x, y)

    def to_fiz(self, pos):
        if pos.x % 2 == 0:
            a = 0
        else:
            a = self.cell_size.y
        x = self.start_pos.x + (pos.x//2)*(self.cell_size.x+self.cell_size.y) + a
        if pos.y % 2 == 0:
            a = 0
        else:
            a = self.cell_size.y
        y = self.start_pos.y + (pos.y // 2) * (self.cell_size.y + self.cell_size.y) + a
        return Point(x, y)

    def is_allowed(self, pos, size=None, log=False):
        if size is None:
            if pos.x < self.start_pos.x or pos.x > self.fiz_size.x:
                return False
            if pos.y < self.start_pos.y or pos.y > self.fiz_size.y:
                return False
            if not log:
                pos = self.to_log(pos)
            return self.cells[pos.y][pos.x] in self.floor
        else:
            check = self.is_allowed(pos) and self.is_allowed(Point(pos.x, pos.y + size.y)) and \
                self.is_allowed(Point(pos.x + size.x, pos.y)) and self.is_allowed(Point(pos.x + size.x, pos.y + size.y))
            if check:
                indent = Point(self.cell_size.y, self.cell_size.y)
                while indent.x < size.x:
                    check = check and self.is_allowed(Point(pos.x + indent.x, pos.y))
                    check = check and self.is_allowed(Point(pos.x + indent.x, pos.y + size.y))
                    indent.x += self.cell_size.y
                while indent.y < size.y:
                    check = check and self.is_allowed(Point(pos.x, pos.y + indent.y))
                    check = check and self.is_allowed(Point(pos.x + size.y, pos.y + indent.y))
                    indent.y += self.cell_size.y
            return check

    def redraw_el(self, pos_elem_from, elem_to):
        pass

    def _get_visual(self, visual):
        self.textured = visual[0]
        if not self.textured:
            self.floor_color = visual[1]
            self.wall_color = visual[2]
        else:
            self.textures = {}
            paths = visual[1]
            try:
                self.walls_high = visual[3]
            except:
                self.walls_high = 0 
            for el in self.floor:
                self.textures[el] = pygame.image.load(f'{paths}field_texture_{el}.png').convert_alpha()
                size = (self.floor[el][0] + self.walls_high, self.floor[el][1] + self.walls_high)
                self.textures[el] = pygame.transform.scale(self.textures[el], size)
            for el in self.wall:
                self.textures[el] = pygame.image.load(f'{paths}field_texture_{el}.png').convert_alpha()
                size = (self.wall[el][0] + self.walls_high, self.wall[el][1] + self.walls_high)
                self.textures[el] = pygame.transform.scale(self.textures[el], size)

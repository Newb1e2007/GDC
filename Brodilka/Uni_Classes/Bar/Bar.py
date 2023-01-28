import pygame
import random
from math import fabs
from Uni_Classes.Point import Point


class Bar:
    def __init__(self, pos, size, max_amount, color, bg_color=(127, 127, 127), full=True, rounded=True, name=None):
        self.pos = pos
        self.size = size
        self.max_amount = max_amount
        if full:
            self.amount = max_amount
        else:
            self.amount = 0
        self.color = color
        self.bg_color = bg_color
        self.name = name
        if self.name is not None:
            self._get_name(name)
        self.rounded = rounded  # отвечает за то, закруглённые ли края у бара или нет
        self.modification = Point(0, 0)

    def draw(self, win):
        self.check_amount()
        color = (fabs(self.bg_color[0] - 30), fabs(self.bg_color[0] - 30), fabs(self.bg_color[0] - 30))
        if not self.rounded:
            pygame.draw.rect(win, self.bg_color, (self.pos.x, self.pos.y, self.size.x, self.size.y))
            pygame.draw.rect(win, self.color, (self.pos.x, self.pos.y, self.size.x*(self.amount/self.max_amount), self.size.y))
            pygame.draw.rect(win, color, (self.pos.x-self.size.y//10, self.pos.y-self.size.y//10, self.size.x+2*self.size.y//10, self.size.y+2*self.size.y//10), self.size.y//10)
        else:
            self._draw_rounded_frame(win, color)
            self._draw_rounded_bg(win)
            self._draw_rounded_bar(win, color)
        if self.name is not None:
            win.blit(self.name, (self.name_pos.x, self.name_pos.y))
        pygame.display.update()

    def check_amount(self):
        if self.amount < 0:
            self.amount = 0
        if self.amount > self.max_amount:
            self.amount = self.max_amount

    def _draw_rounded_frame(self, win, color):
        fix = self.size.y//10
        pygame.draw.circle(win, color, (self.pos.x+self.size.y//2, self.pos.y+self.size.y//2), self.size.y//2+fix, self.size.y//10)
        pygame.draw.circle(win, color, (self.pos.x+self.size.x-self.size.y//2, self.pos.y+self.size.y//2), self.size.y//2+fix, self.size.y//10)
        pygame.draw.rect(win, color, (self.pos.x+self.size.y//2-fix, self.pos.y-fix, self.size.x-self.size.y+2*fix, self.size.y+2*fix), self.size.y//10)

    def _draw_rounded_bg(self, win):
        pygame.draw.circle(win, self.bg_color, (self.pos.x+self.size.y//2, self.pos.y+self.size.y//2), self.size.y//2)
        pygame.draw.circle(win, self.bg_color, (self.pos.x+self.size.x-self.size.y//2, self.pos.y+self.size.y//2), self.size.y//2)
        pygame.draw.rect(win, self.bg_color, (self.pos.x+self.size.y//2, self.pos.y, self.size.x-self.size.y, self.size.y))

    def _draw_rounded_bar(self, win, color):
        size = self.size.x*(self.amount/self.max_amount)
        if size >= self.size.y:
            pygame.draw.circle(win, self.color, (self.pos.x+self.size.y//2, self.pos.y+self.size.y//2), self.size.y//2)
            pygame.draw.circle(win, self.color, (self.pos.x+size-self.size.y//2, self.pos.y+self.size.y//2), self.size.y//2)
            pygame.draw.rect(win, self.color, (self.pos.x+self.size.y//2, self.pos.y, size-self.size.y, self.size.y))
        elif self.amount != 0:
            y_size = (self.size.y*self.size.y//4 - (self.size.y-size)*(self.size.y-size)//4)**0.5
            pygame.draw.ellipse(win, self.color, (self.pos.x, self.pos.y+self.size.y//2-y_size*(100//90), size, y_size*2*(90//50)))
            fix = self.size.y // 10
            pi = 3.14159265359
            pygame.draw.arc(win, color, (self.pos.x-fix+1, self.pos.y-fix, self.size.y+2*fix-1, self.size.y+2*fix), pi/2, 3*pi/2, self.size.y//10-1)

    def _get_name(self, name):
        if isinstance(name, str):
            name = [name, 1]
        self.name_pos_logical = name[1]  # позиции отображения имени относительно бара
        #  0
        #  ======= 1
        #  2
        if self.name_pos_logical == 2:
            self.name_pos = Point(self.pos.x, self.pos.y + self.size.y + self.size.y // 10)
        elif self.name_pos_logical == 1:
            self.name_pos = Point(self.pos.x+self.size.x+self.size.y//5, self.pos.y+self.size.y//8)
        else:
            self.name_pos = Point(self.pos.x, self.pos.y - self.size.y - self.size.y // 10)

        for_render = [False, (127, 127, 127), None]
        try:
            font = pygame.font.SysFont(name[2], name[3])
        except:
            font = pygame.font.Font(None, 30)
        try:
            for_render[0] = name[4]
            for_render[1] = name[5]
            for_render[2] = name[6]
        except:
            pass

        self.name = font.render(name[0], for_render[0], for_render[1], for_render[2])

    def _name_pos_update(self):
        if self.name_pos_logical == 2:
            self.name_pos = Point(self.pos.x, self.pos.y + self.size.y + self.size.y // 10)
        elif self.name_pos_logical == 1:
            self.name_pos = Point(self.pos.x+self.size.x+self.size.y//5, self.pos.y+self.size.y//8)
        else:
            self.name_pos = Point(self.pos.x, self.pos.y - self.size.y - self.size.y // 10)

    def pos_update(self, obj, modification=Point(0, 0)):
        if modification != Point():
            self.modification = modification
        if isinstance(obj, Point):
            self.pos = Point(obj.x + self.modification.x, obj.y + self.modification.y)
        elif isinstance(obj, tuple):
            if len(obj) == 2:
                self.pos = Point(obj[0] + self.modification.x, obj[1] + self.modification.y)
            else:
                self.pos += Point(obj[0] + self.modification.x, obj[1] + self.modification.y)
        else:
            try:
                x = obj.pos.x
                y = obj.pos.y
            except:
                x = obj.x
                y = obj.y
            try:
                y += obj.z
            except:
                pass
            self.pos = Point(x + self.modification.x, y + self.modification.y)

        if self.name is not None:
            self._name_pos_update()

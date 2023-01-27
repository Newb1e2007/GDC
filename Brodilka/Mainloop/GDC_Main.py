import pygame
# import class_player
# import class_reward
import Entity
import Field
import Enemy
from random import randint
from CONST import *
from class_Point import Point


def main():
    pygame.init()

    clock = pygame.time.Clock()

    HEIGHT = 1000
    WEIGHT = 700
    win = pygame.display.set_mode((HEIGHT, WEIGHT))

    field = Field.Field(Point(20, 20), Point(60, 15), Point(24, 15), ['labirint_0'], [True, 'field_img/'])
    # , [True, 'field_img/']

    enemy = Enemy.Enemy(None, Point(335, 335), 5, Point(30, 30), (randint(10, 245), randint(10, 245), randint(10, 245)), None, [True, 100], field)

    run = True
    while run:
        clock.tick(30)

        win.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

#        field = Field.Field(Point(24, 15), Point(60, 15), Point(20, 20), ['labirint_0'])
        field.draw(win)

        pos = pygame.mouse.get_pos()
        pos = Point(pos[0], pos[1])

        enemy.pos_update(field, pos)
        pygame.draw.rect(win, enemy.color, (enemy.pos.x, enemy.pos.y, enemy.size.x, enemy.size.y))

        pygame.display.update()


main()

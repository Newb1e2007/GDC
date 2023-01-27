import pygame
import CONST


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# screen = pygame.display.set_mode(pygame.RESIZABLE)
surface = pygame.display.get_surface()
CONST.DISPLAY_WIDTH, CONST.DISPLAY_HEIGHT = surface.get_width(), surface.get_height()


while True:
    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()
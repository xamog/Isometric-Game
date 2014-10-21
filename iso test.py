##########################################
# A pair of functions to convert the memory representation
# to an isometrically drawn representation.
#
##########################################

GRID_WIDTH, GRID_HEIGHT = 32, 16
X_RES, Y_RES = 600, 400 #size of the screen.
SCROLL_SPEED = 2

import pygame
pygame.init()
window = pygame.display.set_mode ((X_RES, Y_RES))

screen_x, screen_y = 0, 0 #coordinates of the top left corner of the screen.

def to_cartesian (grid_x, grid_y):
    """Convert map coordinates to onscreen coordinates,
    i.e. where on the screen it should be drawn."""
    return (grid_x - grid_y) * GRID_WIDTH / 2 - screen_x, (grid_x + grid_y) * GRID_HEIGHT / 2 - screen_y

def to_grid (cart_x, cart_y):
    """Convert onscreen coordinates to map coordinates"""
    return (cart_x + cart_y + screen_x) / GRID_WIDTH, (cart_y - cart_x + screen_y) / GRID_HEIGHT

if __name__ == '__main__':
    grid = [[0 for y in range (10)] for x in range (20)]

    main_surface = pygame.Surface ((X_RES, Y_RES))

    while (True):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN:
                #handle events that trigger once when the key is pressed and aren't affected by holding the key.
                if e.key == pygame.K_SPACE:
                    screen_x, screen_y = 0, 0
            else:
                pass
        keys = pygame.key.get_pressed()
        if keys [pygame.K_LEFT]:
            screen_x -= SCROLL_SPEED
        if keys [pygame.K_RIGHT]:
            screen_x += SCROLL_SPEED
        if keys [pygame.K_UP]:
            screen_y -= SCROLL_SPEED
        if keys [pygame.K_DOWN]:
            screen_y += SCROLL_SPEED


        for y, row in enumerate (grid):
            for x, cell in enumerate (row):
                pygame.draw.polygon (main_surface, 0x00FF00, tuple (to_cartesian (*points) for points in ((x, y), (x + 1, y), (x + 1, y + 1), (x, y + 1))))
                pygame.draw.polygon (main_surface, 0x000000, tuple (to_cartesian (*points) for points in ((x, y), (x + 1, y), (x + 1, y + 1), (x, y + 1))), 2)

        window.blit(main_surface, (0, 0))
        pygame.display.flip()

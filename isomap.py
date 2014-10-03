from map import Map
from tile import Tile

import pygame

##def to_cartesian (grid_x, grid_y):
##    """Convert map coordinates to onscreen coordinates,
##    i.e. where on the screen it should be drawn."""
##    return (grid_x - grid_y) * grid_width / 2 - screen_x, (grid_x + grid_y) * grid_height / 2 - screen_y
##
##def to_grid (cart_x, cart_y):
##    """Convert onscreen coordinates to map coordinates"""
##    return (cart_x + cart_y + screen_x) / grid_width, (cart_y - cart_x + screen_y) / grid_height

class IsoMap (Map):
    def __init__ (self, map_width, map_height, grid_width, grid_height):
        super().__init__(map_width, map_height)
        
        self.screen_x, self.screen_y = 0, 0 #set the initial parameters of the map
        self.grid_width, self.grid_height = grid_width, grid_height
        self.SCROLL_SPEED = self.grid_width // 16
        
        for tile in self:
            tile.iso_coords = tuple (self.to_cartesian (tile.x + corner[0], tile.y + corner[1]) for corner in ((0, 0), (0, 1), (1, 1), (1, 0)))
        
    def to_cartesian (self, grid_x, grid_y):
        """Convert map coordinates to onscreen coordinates,
        i.e. where on the screen it should be drawn."""
        return ((grid_x - grid_y) * self.grid_width // 2 - self.screen_x, (grid_x + grid_y) * self.grid_height // 2 - self.screen_y)

    def to_grid (self, cart_x, cart_y):
        """Convert onscreen coordinates to map coordinates"""
        return (int ((cart_y + self.screen_y) / self.grid_height + (cart_x + self.screen_x) / self.grid_width), 
            int ((cart_y + self.screen_y) / self.grid_height - (cart_x + self.screen_x) / self.grid_width))

    @staticmethod
    def _vector_add (vect1, vect2):
        """Returns vect1 + vect2, interpreting both as vectors"""
        return [i + j for i, j in zip (vect1, vect2)]
        
    def offset_points(self, points):
        """Offset all points in a vector of them by screen_x, screen_y"""
        return tuple ((point[0] - self.screen_x, point[1] - self.screen_y) for point in points)
            
    def draw (self, surface):
        """Draws all of the tiles for the map"""
        surface_height, surface_width = surface.get_size()
        
        for x in range (max (0, self.to_grid (0, 0) [0]), min (self.width, self.to_grid (surface_width, surface_height) [0] + 1)):
            for y in range (max (0, self.to_grid (surface_width, 0) [1]), min (self.height, self.to_grid (0, surface_height) [1])):
                pygame.draw.polygon (surface, self[x,y].colour, self.offset_points(self[x,y].iso_coords)) 
                pygame.draw.polygon (surface, 0x000000, self.offset_points(self[x,y].iso_coords), 2)
                
    def draw_units (self, surface, units):
        for unit in units:
            pygame.draw.circle (surface, 0xFF0000, IsoMap._vector_add (self.to_cartesian (unit.x, unit.y), (0, self.grid_height // 2)), 10) #-self.grid_width // 4
            
    def transform_tile (self, x, y, new_tile):
        self[x,y] = new_tile
        cartesian_coords = tuple(self.to_cartesian (x + corner[0], y + corner[1]) for corner in ((0, 0), (0, 1), (1, 1), (1, 0)))
        self[x,y].iso_coords = tuple (tuple ((point[0] + self.screen_x, point[1] + self.screen_y)) for point in cartesian_coords)

    def handle_key_events (self, key_events):
        """Move the map around if keys are pressed.
        Pass the result of pygame.key.get_pressed() to this function.
        """
        if key_events [pygame.K_LEFT] or key_events [pygame.K_a]:
            self.screen_x -= self.SCROLL_SPEED
        if key_events [pygame.K_RIGHT] or key_events [pygame.K_d]:
            self.screen_x += self.SCROLL_SPEED
        if key_events [pygame.K_UP] or key_events [pygame.K_w]:
            self.screen_y -= self.SCROLL_SPEED
        if key_events [pygame.K_DOWN] or key_events [pygame.K_s]:
            self.screen_y += self.SCROLL_SPEED

if __name__ == "__main__":
    print ("===TESTING ISOMAP===") 
    pygame.init()
    window = pygame.display.set_mode((600, 400))   
    surface = pygame.Surface ((600, 400))
    
    m = IsoMap(20, 10, 64, 32)
    m.transform_tile(2, 3, Tile(2, 3, Tile.OCEAN))
    
    while True:
        #Enter drawing loop
        m.draw(surface)
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            else:
                pass
        m.handle_key_events (pygame.key.get_pressed())
        
        window.blit(surface, (0, 0))
        pygame.display.flip()
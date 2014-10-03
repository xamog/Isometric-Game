#######
#The game class. 
######
import pygame

from isomap import IsoMap
from city import City
from citytile import CityTile

class Game():    
    cities = []
    units = []
    
    def __init__ (self, map_width, map_height):
        self.map = IsoMap(map_width, map_height, 64, 32)

    def end_turn (self, player_ID):
        "Ends a player's turn"
        for city in Game.cities:
            if city.allegiance == player_ID:
                u = city.next_turn()
                if u != None:
                    self.units.append (u)

    def build_city (self, name, allegiance, x, y):
        "Build a city"
        #because building cities from command line is easy.
        self.cities.append (City (name, allegiance, x, y))
        self.map.transform_tile (x, y, self.cities[-1])
        
    def enter_drawing_loop(self, surface, window):
        ##import cProfile
        ##profiler = cProfile.Profile()
        ##profiler.enable()
    
        #Drawing loop
        while (True):
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit()
                elif e.type == pygame.KEYDOWN:
                    #trigger keyboard events
                    pass
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    print (self.map.to_grid(*e.pos))
                else:
                    #because pygame is stupid and crashes regularly
                    pass

            self.map.handle_key_events (pygame.key.get_pressed())
            self.map.draw(surface)
            self.map.draw_units(surface, self.units)

            window.blit(surface, (0, 0))
            pygame.display.flip()
            
        ##profiler.disable()
        ##profiler.print_stats()
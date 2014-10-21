#######
## The game class. 
######
import pygame

from isomap import IsoMap
from city import City
from citytile import CityTile

class Game():    
    """
    This class holds everything necessary to run the game and handles all user interaction with it.
    """
    
    cities = []
    units = []

    selected_cell = None
    newly_selected_cell = True  # flag to raise when selecting a new cell: tells game to redraw the full tile menu.
    
    def __init__ (self, map_width, map_height):
        self.map = IsoMap(map_width, map_height, 64, 32)
        #self.end_turn(0)

    def end_turn (self, player_ID):
        """
        Ends a player's turn
        
        player_ID - an int between 0 and num_players indicating the player whose turn to end.
        """
        
        for city in Game.cities:
            if city.allegiance == player_ID:
                u = city.next_turn()
                if u != None:
                    self.units.append (u)

    def build_city (self, name, allegiance, x, y):
        """
        Build a city
        
        name - a string containing the name of the city
        allegiance - an int from 0 to num_players indicating the team of the city
        x - x coords of the city
        y - y coords of the city
        """
        #because building cities from command line is easy.
        self.cities.append (City (name, allegiance, x, y))
        self.map.transform_tile (x, y, self.cities[-1])
        
    def enter_drawing_loop(self, window):
        """
        Draw all of the items onto surface. 
        
        window- instance of pygame.Surface to which images are blitted
        """
        map_surface = pygame.Surface((window.get_size()[0] - 200, window.get_size()[1]))  # surface that holds the map
        descrip_surface = pygame.Surface((200, 200))                                      # holds description text
        menu_surface = pygame.Surface((200, window.get_size()[1] - 300))                  # holds action menus
        general_menu_surface = pygame.Surface((200, 100))                                 # for other buttons e.g. trade

        #Drawing loop
        while (True):
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit()
                elif e.type == pygame.KEYDOWN:
                    #trigger keyboard events
                    selected_cell = None
                    newly_selected_cell = True
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    selected_cell = self.map[self.map.to_grid(*e.pos)]
                    newly_selected_cell = True
                    print ("Clicked on cell ", self.map.to_grid(*e.pos))
                else:
                    #because pygame is stupid and crashes regularly
                    pass

            self.map.handle_key_events (pygame.key.get_pressed())
            self.map.draw(map_surface)
            self.map.draw_units(map_surface, self.units)

            window.blit(map_surface, (0, 0))
            pygame.display.flip()
            
        ##profiler.disable()
        ##profiler.print_stats()
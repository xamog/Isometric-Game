class Tile():
    #Tile ID constants. Refer to them by reference because they will change.
    OCEAN = -2
    WATER = -1
    PLAIN = 1
    HILL = 2
    MOUNTAIN = 3
    TERRAIN_SYMBOLS = {OCEAN:'##', WATER:'~~', PLAIN:'__', HILL:'@@', MOUNTAIN:'/\\'}
    TERRAIN_COLOURS = {OCEAN:0x000088, WATER:0x0000FF, PLAIN:0x00FF44, HILL:0x00FF00, MOUNTAIN:0x777777}

    def __init__ (self, x, y, terrain_type):
        self.x = x
        self.y = y 
        
        self.terrain_type = terrain_type
        self._neighbours = []
        self.colour = Tile.TERRAIN_COLOURS [self.terrain_type]

    def set_neighbours (self, north, east, south, west):
        self.north, self.east, self.south, south.west = north, east, south, west
        self._neighbours = [north, east, south, west]

    @property
    def neighbours(self):
        return self._neighbours

    def to_tile (self):
        return Tile.TERRAIN_SYMBOLS [self.terrain_type]

if __name__ == "__main__":
    print ("Running tiles")
    
    tiles = [Tile (0, 0, Tile.OCEAN), Tile (Tile.PLAIN), Tile (Tile.HILL), Tile (Tile.MOUNTAIN)]
    t = Tile (0, 0, Tile.WATER)
    t.set_neighbours (*tiles)

    for i in t.neighbours:
        print (i.terrain_type)

from tile import Tile

class Map():
    def __init__(self, map_width, map_height):
        self.tiles = [[Tile(x, y, Tile.PLAIN) for y in range (map_height)] for x in range (map_width)]
        self.width = map_width
        self.height = map_height        

    #Overloading get, set, iter and next to allow its use as a 2d iterable. 
    def __getitem__ (self, key):
        """Get the tile at given coordinates. Key is a x,y pair."""
        return self.tiles [key[0]] [key[1]]
    def __setitem__ (self, key, value):
        """Set the tile at the given coordinates. Key is an x,y pair"""
        self.tiles [key[0]] [key[1]] = value
    def __iter__ (self):
        self._iter_counter = -1
        return self
    def __next__ (self):
        if self._iter_counter >= self.width * self.height - 1:
            raise StopIteration
        else:
            self._iter_counter += 1
            return self.tiles [self._iter_counter % self.width] [self._iter_counter // self.width]
 
    def __str__ (self):
        res = ""
        for x in range (self.width):
            for y in range (self.height):
                res += self.tiles [x][y].to_tile() + ' '
            res += '\n'
        return res        

if __name__ == '__main__':
    print ("==TESTING MAP CLASS==")
    m = Map(5, 10)
    m[4, 2].terrain_type = Tile.WATER #accessing cell
    
    a = 0
    for i in m: #iterate through every cell
        print (i.x, i.y)
        a += 1
        
    print ("number of cells iterated through: ", a)

    print (m)
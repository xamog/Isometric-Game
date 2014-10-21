from tile import Tile

class IsoTile(Tile):
    def __init__ (self, terrain_type, iso_coords):
        super().__init__(terrain_type)
        self.iso_coords = iso_coords
        
    def offset(self, x, y):
        """Returns this tile's coordinates translated by x, y"""
        return tuple ((point[0] - x, point[1] - y) for point in self.iso_coords)
        
     
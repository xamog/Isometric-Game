class Tile():
	#Tile ID constants. Refer to them by reference because they will change.
	OCEAN = -2
	WATER = -1
	PLAIN = 1
	HILL = 2
	MOUNTAIN = 3
	TERRAIN_SYMBOLS = {OCEAN:'##', WATER:'~~', PLAIN:'__', HILL:'∩∩', MOUNTAIN:'/\\'}
	
	def __init__ (self, terrain_type):
		self.terrain_type = terrain_type
		
	def to_tile (self):
		return Tile.TERRAIN_SYMBOLS [self.terrain_type]
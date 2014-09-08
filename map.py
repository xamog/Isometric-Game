from tile import Tile

class Map():
	def __init__(self, map_width, map_height):
		self.tiles = [[Tile(Tile.PLAIN) for i in range (map_width)] for j in range (map_height)]
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
		if self._iter_counter >= self.width * self.height:
			raise StopIteration
		else:
			self._iter_counter += 1
			return self.tiles [self._iter_counter // self.height] [self._iter_counter % self.width]
 
	def __str__ (self):
		res = ""
		for i in range (self.height):
			for j in range (self.width):
				res += self.tiles [i][j].to_tile() + ' '
			res += '\n'
		return res
			

if __name__ == '__main__':
	print ("==Testing map class==")
	m = Map(5, 10)
	m[4, 2].terrain_type = Tile.WATER #accessing cells
	
	for i in m: #iterate through every cell
		pass

	print (m)
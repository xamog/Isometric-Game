#######
#The main class. It is static so that its fields can be accessed from all other files
######

from map import Map
from city import City
from citytile import CityTile

class Game():	
	cities = []
	units = []
	
	def __init__ (self, map_width, map_height):
		self.map = Map(map_width, map_height)

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
		self.map [x, y] = self.cities [-1]
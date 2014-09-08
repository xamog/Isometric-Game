from tile import Tile

class CityTile(Tile):
	team_names = ["A team", "B team", "C team"]

	def __init__(self, city):
		self.city = city
	
	def __str__ (self):
		return 	"⌂{:1}".format(CityTile.team_names[self.city.allegiance])
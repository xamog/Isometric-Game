from product import Product
from unit import Unit

team_names = ["A team", "B team", "C team"] #make sure the version in main stays current too. 

class City():
	def __init__ (self, name, allegiance, x, y):
		self.name = name
		self.allegiance = allegiance
		self.x = x
		self.y = y
		self.city_improvements = []
		self.current_product = Product.NOTHING
		self.current_progress = 0

		#values that will change based on the terrain, but I'm setting them as constant for now
		self.productivity = 3
		
	def set_product (self, product):
		"Begin producing something"
		self.current_product = product
		#decrease current_progress because building walls doesn't help you train units,
		#but remember the previous production if they switch and switch back

	def next_turn(self):
		"Reset the city for the next turn"
		if self.current_progress >= Product.cost [self.current_product]:
			self.current_progress -= Product.cost [self.current_product]
			if Product.isUnit(self.current_product):
				print ("{:s} has produced product id {:s}".format (self.name, self.current_product))
				return Unit (self.x, self.y, self.current_product)
			elif Product.isBuilding(self.current_product):
				self.city_improvements.append (self.current_product)
				self.current_product = Product.NONE
		self.current_progress += self.productivity
		return None

	def __repr__ (self):
		return "{:10s} ({:4}, {:4})".format(self.name, self.x, self.y)

	def to_tile (self):
		return "⌂{:1}".format (team_names [self.allegiance])
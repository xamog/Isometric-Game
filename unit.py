from product import Product

class Unit():
	unit_types = {
		#name, attack, defence, max health, range, speed
		Product.ARCHER: ("Archer", 10, 1, 50, 4, 2),
		Product.CAVALRY: ("Cavalry", 8, 5, 150, 1, 2),
		}
	
	def __init__ (self, x, y, unit_type):
		self.x = x 
		self.y = y
		self.name, self.attack, self.defence, self.max_health, self.range, self.speed = Unit.unit_types [unit_type]
		
	def __str__ (self):
		return "{name} @ {x},{y}".format (x=self.x, y=self.y, name=self.name)
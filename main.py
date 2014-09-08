from game import Game

city_names = ["Algiers", "Beirut", "Cairo", "Dresden", "Edinburgh", "Funafuti", "Gibraltar", "Havana", "Iol Caesarea"]
team_names = ["A team", "B team", "C team"] #make sure the version in city stays current too. This will not be in the final build, don't worry. 

orders = """
city 4 6 1 
make 4 6 unit:archer
end
end
end
move 4 6 2 8
end
end 
"""

if __name__ == "__main__":
	turn_number = 0

	current_player = 0
	num_players = 2
	game = Game(20, 10) 
	
	#main game loop
	for order in orders.split ('\n'): 	#while (True): #for the interactive version 
		print ("Turn: {}, Team: {}".format (turn_number, team_names [current_player] [0]))
	
		print ("==Map==")
		print (game.map)
		
		print ("==Cities==")
		if len (game.cities) == 0:
			print ("None")
		for city in game.cities:
			print (city)
		print ("==Units==")
		if len (game.units) == 0:
			print ("None")
		for unit in game.units:
			print (unit)
		
		print ("==Notifications==")
		s = order.split()	#input("Submit your command >>> ").split() #for the interactive version
		if order == '':
			pass
		elif s[0] == 'city':
			x, y, ally = [int (i) for i in s[1:4]]
			game.build_city (city_names.pop(0), ally, x, y)
		elif s[0] == 'make':
			x, y = [int (i) for i in s[1:3]]
			productID = s[3]
			game.map[x, y].current_product = productID
		elif s[0] == 'end':
			pass
		elif s[0] == 'move':
			x, y, x1, y1 = [int (i) for i in s[1:]]
			for unit in game.units:
				if unit.x == x and unit.y == y:
					unit.x, unit.y = x1, y1
		else:
			print ("Unknown command")
		
		game.end_turn(current_player)
		current_player = (current_player + 1) % num_players
		if current_player == 0:
			turn_number += 1
		
		print ("\n")
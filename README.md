README

==PROGRAM INSTRUCTIONS==
Save everything in one directory. Run "main.py"

==A BRIEF DESCRIPTION==
Each player takes a turn one after another. They may build cities, 
make and move units and then end their turn. 


==INSTRUCTIONS FOR INTERACTING WITH MAIN.PY==
Commands: 
- 'city' x y ally                builds a city at $x, $y with allegiance to $ally
- 'make' x y productID            sets production of city at x y to productID
- 'end'                             ends current player's turn.
- 'move x y x1 y1                 moves the first unit found at (x, y) to (x1, y1)

==DATA STRUCTURE (so far)==
Higher things inherit from lower ones.

        main 
         |
        game
       /  |   \
    city unit  map
          |     |
      product  tile
      

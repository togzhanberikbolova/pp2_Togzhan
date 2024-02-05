def solve( numheads, numlegs ):
    if numheads > numlegs or numheads == 0 or numlegs == 0 or numlegs % 2 != 0:
        print( "ERROR" )
    else:
        rabbits = (numlegs - (numheads * 2)) / 2
        chickens = numheads - rabbits
        print( int ( rabbits ), int ( chickens ) )
        
solve ( 35, 94 )
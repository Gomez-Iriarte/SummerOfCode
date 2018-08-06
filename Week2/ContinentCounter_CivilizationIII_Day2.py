# Things to try
#
#2.  Write a function that generates an n x n sized board
# with either land or water chosen randomly.
M = 'land'
o = 'water'
World1 =[[o,o,o,o,o,o,o,o,o,o,o],
 		[o,o,o,o,M,M,o,o,o,o,o],
 		[o,o,o,o,o,o,o,o,M,M,o],
 		[o,o,o,M,o,o,o,o,o,M,o],
 		[o,o,o,M,o,M,M,o,o,o,o],
 		[o,o,o,o,M,M,M,M,o,o,o],
 		[o,o,o,M,M,M,M,M,M,M,o],
 		[o,o,o,M,M,o,M,M,M,o,o],
 		[o,o,o,o,o,o,M,M,o,o,o],
 		[o,M,o,o,o,M,o,o,o,o,o],
 		[o,o,o,o,o,o,o,o,o,o,o]]

# These are just to make the map easier for us to read.​


#def World_CivilizationIII(world):
#	for x in range(0,len(world)):
#	  	print(world[x])

#World_CivilizationIII(World1)
#There is one small bug in the continent counter above. 
#Can you find it and fix it? 
#(Hint: change the world so that the continent borders the edge)

def continent_counter(world, x, y):
	if world[y][x] != 'land':  # the bug was in missing the character ":" in the conditional if 
		return 0
	size = 1 # out of if, and define the variable size
	world[y][x]= 'counted land'
	# ...then we count all of the neighboring eight tiles​
	# (and, of course, their neighbors by way of the recursion).​
	size = size + continent_counter(world, x-1, y-1)
	size = size + continent_counter(world, x , y-1)
	size = size + continent_counter(world, x+1, y-1)
	size = size + continent_counter(world, x-1, y )
	size = size + continent_counter(world, x+1, y )
	size = size + continent_counter(world, x-1, y+1)
	size = size + continent_counter(world, x , y+1)
	size = size + continent_counter(world, x+1, y+1)
	return size

print(continent_counter(World1, 5, 5))
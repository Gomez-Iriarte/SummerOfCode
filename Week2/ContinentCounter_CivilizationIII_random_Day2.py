# Things to try
#
#2.  Write a function that generates an n x n sized board
# with either land or water chosen randomly.

import random
n= input('Write the value of n x n sized board: ')
world2 = [[random.randint(0,1) for x in range(0,int(n))] for x in range(0,int(n))]
# 1  is land 
# 0  is water
# 4  countend land
print('*************')
for i in range(0,int(n)):
	#for j in range(0,3):
  	 print(world2[i])

def continent_counter(world, x, y):
	#print(x)
	#print(y)
	#print('****')
	if  x<0 or y<0 or (x>(int(n)-1)) or (y> (int(n)-1)): # this is for avoid a bug in the list range
		return 0

	elif world[x][y] != 1: # If tiles is diferents of land 
		return 0
	size = 1 # out of if, and define the variable size
	world[x][y]= 4  #  with this value the land is labeled like 'counted land'
	# ...then we count all of the neighboring eight tiles​
	# (and, of course, their neighbors by way of the recursion).​
	size = size + continent_counter(world, x-1, y-1) # All these sentences are counting by the recursion
	size = size + continent_counter(world, x , y-1)  # Recursion the fuction calling itself, if doesn't go the next until the recursion in the first line is finished
	size = size + continent_counter(world, x+1, y-1)
	size = size + continent_counter(world, x-1, y )
	size = size + continent_counter(world, x+1, y )
	size = size + continent_counter(world, x-1, y+1)
	size = size + continent_counter(world, x , y+1)
	size = size + continent_counter(world, x+1, y+1)
	return size

if world2[int(n)//2][int(n)//2] == 0:  # Defining the center of board like tile of land
	world2[int(n)//2][int(n)//2] = 1 # Defining the center of board like tile of land
#Some island are not counted if it is far away of continent (there are not conectionts with the neighbohrs)
print('The size of continent in random units is: ')  	 
print(continent_counter(world2, int(n)//2, int(n)//2))

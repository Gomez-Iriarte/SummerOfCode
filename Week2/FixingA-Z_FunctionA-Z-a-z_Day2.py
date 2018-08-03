# -*- coding: utf-8 -*-    
#for i in range(65,65+2*26):
#    print(i, " stands for ", chr(i)) # print o chracter ascii desde 65 ate 116
#print(chr(135)) # en teoria deberia imprimir la c dilha y no lo hace
#print(chr(162))  # en teoria deberia imprimir la o o la a acentuada.      
#
#
#There is something small that needs fixing.
#Can you spot it and fix it? (Hint, we only want A-Z and a-z)
#
#Yes, between char 91 and 96 there are character especials no letter
#
#
# Fixing for get only letters from A-Z and  a- z.
print ('****** Fixing for A-z and a-z ******')
for i in range(65,123):
	if i <91 or i >96:
		print(i, " stands for ", chr(i))
#
#
#Make a function that prints A-Z and a-z
#
#
def printabc():
	for i in range(65,123):
		if i <91 or i >96:
			print(i, " stands for ", chr(i))

print("Testing a Abc function, calling without argument")
printabc()
#
#

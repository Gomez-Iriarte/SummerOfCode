#Writing  program that prints the lyris of "99 bottles of beer on the wall"
#"99 bottles of beer on the wall, 99 bottles of beer.Take one down, pass it around, 98 bottles of beer on the wall..."
b=99
for x in range(1,100):
 	print (str(b) + " bottles of beer on the wall, "+str(b)+ " bottles of beer.")
 	print ('Take one down, pass it around, '+str(b-1)+ ' bottles of beer on the wall...')
 	print("***")
 	b=b-1
 	if b == 0:
 	 print"No more bottles of beer on the wall, no more bottles of beer."
 	 print"We've taken them down and passed them around; now we're drunk and passed out!"

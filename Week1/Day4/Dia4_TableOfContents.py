# tABLE of contents
#Write a table of contents program here. Start the program with a list #
#holding all of the information for your table of contents (chapter names,
#page numbers, and so on). Then print out the information from the list in a
#beautifully formatted table of contents. Use string formatting such as left
#align, right align, center.
print('Table of Contents'.center(40))
print('')
lis_chap=[['Introduction',4], ['Mammals',10],['Reptils',8],['Birds',6],['Conclusions',3]]
#print(lis_chap)
# i=0
# for x in xrange(0,5):
# 	for i in xrange(0,2):
# 		print(lis_chap[x][i])

#center, ljust, and rjust
#print(len(lis_chap[0][0])- len(lis_chap[4][0]))
for x in xrange(0,5):
	if x == 0:
		print(''.ljust(5)+str(lis_chap[x][0])+ str(lis_chap[x][1]).rjust(25))
		print(' ')
	elif x == 4: 
		print(''.ljust(5)+str(lis_chap[x][0])+ str(lis_chap[x][1]).rjust(27))
		print(' ')
	else:
		print(''.ljust(5)+'Chapter '+ str(x)+ ": "+str(lis_chap[x][0].ljust(4)) + str(lis_chap[x][1]).rjust(20))
		print (" ")


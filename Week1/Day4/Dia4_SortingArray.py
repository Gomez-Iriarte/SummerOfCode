print'*** Sorting Array ***'
#print "Please write words until we get bored: "

list1=[raw_input("Please write words until we get bored: ") for x in xrange(1,5)]
# list1=[]
# for x in xrange(1,4):
#  	list1[x]=[raw_input("Please write words until we get bored: ")]
# 	if list1[x] == None:
#  		list1[x].pop()
#  		print("Write something please, don't leave empthy space: ")
#  		list1[x]=[raw_input()]


#	list1[i]=raw_input()
print("Enough!! We're bored!!")
print('This is your original list:')
print(list1)
print('This is your list with a alphabetical order: ')
print(sorted(list1))
print('Esta es la lista agregandole elementos: ')
print(list1.append("a")) # imprime none
print(list1)             # despues de agregar imprime la lista junto con la letra a
print(list1.append("b"))
print(list1)
print(list1[0])
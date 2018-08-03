#Make a function that asks the user for a message, 
#and turns it into a list of numbers. (It's a cypher ;))
#"I LOVE YOU" [ 73, , 76, ...]
def changeLetterToNumbers():
	print('Write a phrase: ')
	listNumbers=[]
	text=input()
	for x in range(0,len(text)):
		for i in range(65,123):
			if text[x]== chr(i) and (i <91 or i >96):
					listNumbers.append(i)
		if text[x]== ' ' and (i <91 or i >96):
				listNumbers.append(' ') 
	print("")
	print('The letters in "'+text +'" have their respective numbers ascii: ')
	print("")
	print(listNumbers)


changeLetterToNumbers()
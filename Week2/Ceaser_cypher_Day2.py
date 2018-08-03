 #Write a function that does a ceaser cypher (Google), ask the user a number,
 #and shift their message by that number.
 # Ceaser_Cypher base is En(x)= x+n
import string
def ceaser_cypher():
	n=input('Give the number n for ceaser cypher: ')
	plainText=list(string.ascii_uppercase) 
	cypherText=''
	print("Write the message:")
	text=input().upper()
	for y in range(0,len(text)):
		for x in range(0,len(plainText)):
			if text[y] == plainText[x]:
				cypherText = cypherText + plainText[x-int(n)]
		if text[y] == ' ':
			cypherText = cypherText + ' '
	print('Original message is: '+ text)
	print('  Cypher message is: '+ cypherText)
print('Basic Ceaser Cypher')
ceaser_cypher()
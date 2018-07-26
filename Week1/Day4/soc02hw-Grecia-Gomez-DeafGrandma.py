#Deaf grandma. 
#Whatever you say to Grandma (whatever you type in), 
#she should respond with this: HUH?! SPEAK UP, GIRL! until you scream in uppercase
import random
text = raw_input()
while text != text.upper():
	print("HUH?! SPEAK UP GIRL")
	print("Did you say "+ str(random.randint(1930, 1950))+ '?')
	text = raw_input("What did you say young lady? ")
	if text == text.upper():
	  print('Ah!! Now I understood')
	elif text == 'bye':
		break
		

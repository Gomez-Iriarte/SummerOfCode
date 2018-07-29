#Deaf grandma. 
#Whatever you say to Grandma (whatever you type in), 
#she should respond with this: HUH?! SPEAK UP, GIRL! until you scream in uppercase
import random
text = raw_input()
while text != text.upper() and text != "BYE BYE BYE":
	print("HUH?! SPEAK UP GIRL")
	print("Did you say "+ str(random.randint(1930, 1950))+ '?')
	text = raw_input("What did you say young lady? ")
	if text == text.upper() and text!= "BYE BYE BYE" and text!= "BYE":
	  print("NO, NOT SINCE 1938!")
	  print('Ah!! Now I understood. What happen my girl?')
	elif text == "BYE":
		print ("What did you say young lady? Do you want a slide of cake?")
		text = raw_input()
	elif text == "BYE BYE BYE":
		break
		

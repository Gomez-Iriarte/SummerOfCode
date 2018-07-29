#homework Week 1 Summer of Code by Grecia Alejandra Gomez Iriarte
#These code are writed in python 2.7, I hope that is not demantory use python 3.7
######  Day 1 #####
#
#       Hour in a year
print "Hours in a Year"
print(365*24)
print "Minutes in a decade"
print(10*365*24*60)
print"My age in seconds"
print (33*365*24*60*60)  # una vieja joven vale!!! jajaja
print"Age in years from Andrea Visanoiu"
print(48618000/(3600*365*24))
#
### Accurate Birthday 
import datetime
import time
print"My Accurated age "
print "Current Date and time :" , datetime.datetime.now()
datenow=datetime.datetime.now()
datebirth=datetime.datetime(1984,10,19,4,30,20,463233)
print "My birthday date and time: "
print (datebirth)
age=datenow-datebirth
print "my age are:"
#print "mi edad es:", age.year
print(age/365) # I had problems to express in years and month 
#
#
######  Day 3 #####
#    Full name greeting
print('Hello..Give your full name')
name=raw_input('Your name: ')
middle=raw_input('Your middle name: ')
last=raw_input('Your last name: ')
print('Nice to meet you so much ' + name + ' '+ middle + ' '+ last)
#
#Bigger, better favorite number
#
print "Bigger, better favorite number"
number=raw_input('Give me your favorite number from 1 to 100: ')
bigger=int(number)+1
print('This number '+ str(bigger)+ ' is bigger and better that youuur :P')
#
## Angry Boss
print'Angry Boss'
print'Boss: What do you want?'
me=raw_input('me:')
print("Boss: WHADDAYA MEAN \""+ me + "\"?!? YOU'RE FIRED!!")
#
#
######  Day 4 #####
#"99 bottles of beer on the wall"
b=99
for x in range(1,100):
 	print (str(b) + " bottles of beer on the wall, "+str(b)+ " bottles of beer.")
 	print ('Take one down, pass it around, '+str(b-1)+ ' bottles of beer on the wall...')
 	print("***")
 	b=b-1
 	if b == 0:
 	 print"No more bottles of beer on the wall, no more bottles of beer."
 	 print"We've taken them down and passed them around; now we're drunk and passed out!"
#
#
#  Deaf grandma. 
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
#
#  DEAF GRANDMA EXTENDED   . 
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
#
#       LEAP YEARS
##
import random
print ('**** Leap Years ****')
year1 = raw_input("Write the initial year: ")
year2 = raw_input("Write the ending year: ")
n=0
if int(year1)%4 != 0 :
	#print (year1 + ' inicial no me sirve para el loop')
	yearaux=int(year1)
	while yearaux %4 != 0 :
		yearaux=yearaux+1
		#print('estou aumentando el ano a '+str(yearaux))
	for x in xrange(int(yearaux),(int(year2)+1),4):
		if int(x)%4 == 0 and int(x)%100 != 0 :
			n=n+1
			#print(str(x) + ' I am leap corregido')
		if int(x)%4 == 0 and int(x)%400 == 0 and int(x)%100 == 0 :
			n=n+1
			#print(str(x) + ' I am weirdo leap year like 1600 and 2000 corrigiendo ano inicial')
else:
	for x in xrange(int(year1),(int(year2)+1),4):
		if int(x)%4 == 0 and int(x)%100 != 0 :
			n=n+1
			#print(str(x) + ' I am leap')
		if int(x)%4 == 0 and int(x)%400 == 0 and int(x)%100 == 0 :
			n=n+1
			#print(str(x) + ' I am weirdo leap year like 1600 and 2000')

print ('The number of leap years between ' + year1 + ' and ' + year2 +' (including them in the countingo) are:' + str(n))
#
#
#          SORTING ARRAY
#
3
print'*** Sorting Array ***'
list1=[raw_input("Please write words until we get bored: ") for x in xrange(1,4)]
print("Enough!! We're bored!!")
print('This is your original list:')
print(list1)
print('This is your list with a alphabetical order: ')
print(sorted(list1))
#
#
#          TABLE OF CONTENTS
## tABLE of contents
print('Table of Contents'.center(40))
print('')
lis_chap=[['Introduction',4], ['Mammals',10],['Reptils',8],['Birds',6],['Conclusions',3]]
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
#
#
#        	YEARS in OLD ROMANS NUMBERS  
#
print '***  Years in old numeral romans  ***'
num=raw_input('Please, give a year between 1 and 3000: ')
#  Setting functions
def romanM(roman_mil):   #Funtion for calculate old roman of thousand number "M"
	nromanM=""
	i=1
	while  i<= roman_mil:
		nromanM = nromanM + 'M'
		i=i+1
	return nromanM
#
#
def romanD(roman_qui):	#Funtion for calculate old roman above of five hundred "D"
	nromanD="D"
	if roman_qui>5 and roman_qui<= 9:
		i=6
		while  i<= roman_qui:
			nromanD = nromanD + 'C'
			i=i+1
		return nromanD
	else:
		if roman_qui == 5:
			return nromanD
#
#
def romanC(roman_hund):  #Funtion for calculate old roman of hundred number until 400
	nromanC=""
	i=1
	while  i<= roman_hund:
		nromanC = nromanC + 'C'
		i=i+1
	return nromanC
#
#	
def romanL(roman_fif):  #Funtion for calculate old roman above of fifty "L"
	nromanL="L"
	if roman_fif>5 and roman_fif<= 9:
		i=6
		while  i<= roman_fif:
			nromanL = nromanL + 'X'
			i=i+1
		return nromanL
	else:
		if roman_fif == 5:
			return nromanL
#
#
def romanX(roman_ten): #Funtion for calculate old roman of decene number until 40
	nromanX=""
	i=1
	while  i<= roman_ten:
		nromanX = nromanX + 'X'
		i=i+1
	return nromanX
#
#
def romanV(roman_five): #Funtion for calculate old roman above of five "V"
	nromanV="V"
	if roman_five>5 and roman_five<= 9:
		i=6
		while  i<= roman_five:
			nromanV = nromanV + 'I'
			i=i+1
		return nromanV
	else:
		if roman_five == 5:
			return nromanV
#
#
def romanI(roman_one): #Funtion for calculate old roman until 4
	nromanI=""
	i=1
	while  i<= roman_one:
		nromanI = nromanI + 'I'
		i=i+1
	return nromanI
#
#
size=int(len(num)) # calculating the numbers of digits in the string num and make him integer
if size == 4:     # I am working with a number in thousands
	power = 10**3 
	div= (int(num)/1000)  # calculating the division between num and 1000
	mod=(int(num)%1000) # calculating the modulus between num and 1 thousand and a modulus
if size == 3:
	power =10**2
	div= (int(num)/100)  # calculating the division between num and 100 and a modulus
	mod=(int(num)%100)
if size == 2 :
	power = 10
	div= (int(num)/10)  # calculating the division between num and 10 and a modulus
	mod=(int(num)%10)
if size == 1:
	power = 1
	div=int(num)
	mod=0
#
nroman0="" 			# Define the string where I write my roman number
for x in xrange(0,size):
	# working with the digits in thousands
	if power == 1000:  
		if div >=5 and div <= 9:
			print "We are working with until year until 3000, let's wait util we get this age"
		elif div >= 1 and div <= 4:
				nroman0=nroman0+romanM(div)
	# working with the digits in hundreds
	if power == 100:
		if div >=5 and div <= 9:
			nroman0=nroman0+romanD(div)
		elif div >= 1 and div <= 4:
				nroman0=nroman0+romanC(div)
	# working with the digits in tens
	if power == 10:
		if div >= 5  and div <= 9:
			nroman0=nroman0+romanL(div)
		elif div >=1 and div <= 4:
				nroman0=nroman0+romanX(div)
	# working with the digits 0-9
	if power == 1: 
		if div >= 5 and div <= 9:
			nroman0=nroman0+romanV(div)
		elif div < 5:	
        		nroman0=nroman0+romanI(div)
	divaux=mod #variable for keep the mod value before change, because it is necessary for the new value in variable div  
	power= power/10
	if divaux == 0 and power == 0 and mod == 0:
		break
	elif mod == 0:
		break
	else:
		div = divaux/power	
		mod= divaux%power
#
print('The year ' + str(num) + ' in old roman numbers is: '+ nroman0)
#
#
#***  MODERN NUMERALS ROMANS  ***'
# 
#
print '***  Years in Modern numeral romans  ***'
num=raw_input('Please, give a year between 1 and 3000: ')
#  Setting functions
def romanM(roman_mil):   #Funtion for calculate modern roman of thousand number "M"
	nromanM=""
	i=1
	while  i<= roman_mil:
		nromanM = nromanM + 'M'
		i=i+1
	return nromanM
#
#
def romanD(roman_qui):	#Funtion for calculate modern roman above of five hundred "D"
	nromanD="D"
	if roman_qui>5 and roman_qui< 9:
		i=6
		while  i<= roman_qui:
			nromanD = nromanD + 'C'
			i=i+1
		return nromanD
	elif roman_qui == 9:
			nromanD = 'CM'
			return nromanD
	else:
		if roman_qui == 5:
			return nromanD
#
#
def romanC(roman_hund):  #Funtion for calculate modern roman of hundred number until 400
	nromanC=""
	i=1
	if roman_hund < 4:
		while  i<= roman_hund:
			nromanC = nromanC + 'C'
			i=i+1
	elif roman_hund == 4:
			nromanC ='CD'
	return nromanC
#
#	
def romanL(roman_fif):  #Funtion for calculate modern roman above of fifty "L"
	nromanL="L"
	if roman_fif>5 and roman_fif< 9:
		i=6
		while  i<= roman_fif:
			nromanL = nromanL + 'X'
			i=i+1
		return nromanL
	elif roman_fif == 9: 
			nromanL='XC'
			return nromanL
	else:
		if roman_fif == 5:
			return nromanL
#
#
def romanX(roman_ten): #Funtion for calculate modern roman of decene number until 40
	nromanX=""
	i=1
	if roman_ten < 4:
		while  i<= roman_ten:
			nromanX = nromanX + 'X'
			i=i+1
	elif roman_ten == 4:
			nromanX = nromanX + 'XL'
	return nromanX
#
#
def romanV(roman_five): #Funtion for calculate modern roman above of five "V"
	nromanV="V"
	if roman_five>5 and roman_five<9:
		i=6
		while  i<= roman_five:
			nromanV = nromanV + 'I'
			i=i+1
		return nromanV
	elif roman_five == 9:
			nromanV = 'IX'
			return nromanV
	else:
		if roman_five == 5:
			return nromanV
#
#
def romanI(roman_one): #Funtion for calculate modern roman until 4
	nromanI=""
	i=1
	if roman_one < 4:
		while  i<= roman_one:
			nromanI = nromanI + 'I'
			i=i+1
	elif roman_one == 4:
			nromanI = nromanI + 'IV'
	return nromanI
#
#
size=int(len(num)) # calculating the numbers of digits in the string num and make him integer
if size == 4:     # I am working with a number in thousands
	power = 10**3 
	div= (int(num)/1000)  # calculating the division between num and 1000
	mod=(int(num)%1000) # calculating the modulus between num and 1 thousand and a modulus
if size == 3:
	power =10**2
	div= (int(num)/100)  # calculating the division between num and 100 and a modulus
	mod=(int(num)%100)
if size == 2 :
	power = 10
	div= (int(num)/10)  # calculating the division between num and 10 and a modulus
	mod=(int(num)%10)
if size == 1:
	power = 1
	div=int(num)
	mod=0
#
nroman0="" 			# Define the string where I write my roman number
for x in xrange(0,size):
	# working with the digits in thousands
	if power == 1000:  
		if div >=5 and div <= 9:
			print "We are working it until year until 3000, let's wait util we get this age"
		elif div >= 1 and div <= 4:
				nroman0=nroman0+romanM(div)
	# working with the digits in hundreds
	if power == 100:
		if div >=5 and div <= 9:
			nroman0=nroman0+romanD(div)
		elif div >= 1 and div <= 4:
				nroman0=nroman0+romanC(div)
	# working with the digits in tens
	if power == 10:
		if div >= 5  and div <= 9:
			nroman0=nroman0+romanL(div)
		elif div >=1 and div <= 4:
				nroman0=nroman0+romanX(div)
	# working with the digits 0-9
	if power == 1: 
		if div >= 5 and div <= 9:
			nroman0=nroman0+romanV(div)
		elif div < 5:	
        		nroman0=nroman0+romanI(div)
	divaux=mod #variable for keep the mod value before change, because it is necessary for the new value in variable div  
	power= power/10
	if divaux == 0 and power == 0 and mod == 0:
		break
	elif mod == 0:
		break
	else:
		div = divaux/power	
		mod= divaux%power
#
print('The year ' + str(num) + ' in modern roman numbers is: '+ nroman0)
#by Grecia Gomez Iriarte















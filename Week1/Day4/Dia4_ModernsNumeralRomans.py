#***  MODERN NUMERALS ROMANS  ***'
#Eventually, someone thought it would be terribly clever if putting a smaller 
#number before a larger one meant you had to subtract the smaller one. 
#As a result of this development, you must now suffer. 
#Rewrite your previous method to return the new-style Roman numerals so when 
#someone calls roman_numeral 4, it should return 'IV', 90 should be 'XC' etc.

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

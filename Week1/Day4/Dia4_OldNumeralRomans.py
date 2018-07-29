### Old numeral romans
#Write a method that when passed an integer between 1 and 3000 (or so) 
#returns a string containing the proper old-school Roman numeral. In other 
#words, old_roman_numeral 4 should return 'IIII'. Make sure to test your
#method on a bunch of different numbers.

print '***  Years in old numeral romans  ***'

num=raw_input('Please, give a year between 1 and 3000: ')

def romanM(roman_mil):   #Funtion for calculate old roman of thousand number "M"
	nromanM=""
	i=1
	while  i<= roman_mil:
		nromanM = nromanM + 'M'
		i=i+1
	#print('entre en la funcion imprimo '+ nromanM)
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
	#print('entre en la funcion imprimo '+ nromanD)

def romanC(roman_hund):  #Funtion for calculate old roman of hundred number until 400
	nromanC=""
	i=1
	while  i<= roman_hund:
		nromanC = nromanC + 'C'
		i=i+1
	#print('entre en la funcion imprimo '+ nromanC)
	return nromanC
	
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
	#print('entre en la funcion imprimo '+ nromanL)

def romanX(roman_ten): #Funtion for calculate old roman of decene number until 40
	nromanX=""
	i=1
	while  i<= roman_ten:
		nromanX = nromanX + 'X'
		i=i+1
	#print('entre en la funcion imprimo '+ nromanX)
	return nromanX

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
	#print('entre en la funcion imprimo '+ nromanV)

def romanI(roman_one): #Funtion for calculate old roman until 4
	nromanI=""
	i=1
	while  i<= roman_one:
		nromanI = nromanI + 'I'
		i=i+1
	#print('entre en la funcion imprimo '+ nromanI)
	return nromanI


size=int(len(num)) # calculating the numbers of digits in the string num and make him integer
if size == 4:     # I am working with a number in thousands
	power = 10**3 
	div= (int(num)/1000)  # calculating the division between num and 1 thousand
	mod=(int(num)%1000) # calculating the modulus between num and 1 thousand
if size == 3:
	power =10**2
	div= (int(num)/100)  # calculating the division between num and 1 thousand
	mod=(int(num)%100)
if size == 2 :
	power = 10
	div= (int(num)/10)  # calculating the division between num and 1 thousand
	mod=(int(num)%10)
if size == 1:
	power = 1
	div=int(num)
	mod=0
#
nroman0=""
for x in xrange(0,size):
	if power == 1000:
		if div >=5 and div <= 9:
			print "We are working it until year until 3000, let's wait util we get this age"
			#nroman0=nroman0+romanM(div)
			#print('comprobando ' + nroman0)
			#print('print div vale ahora '+ str(div))
		elif div >= 1 and div <= 4:
				nroman0=nroman0+romanM(div)
				#print('comprobando ' + nroman0)
				#print('print div vale ahora '+ str(div))
				#print('print power vale ahora '+ str(power))
	if power == 100:
		if div >=5 and div <= 9:
			nroman0=nroman0+romanD(div)
			#print('comprobando ' + nroman0)
			#print('print div vale ahora '+ str(div))
		elif div >= 1 and div <= 4:
				nroman0=nroman0+romanC(div)
				#print('comprobando ' + nroman0)
				#print('print div vale ahora '+ str(div))
				#print('print power vale ahora '+ str(power))
	if power == 10:
		#print 'Entre en las decenass'
		#print(div)
		if div >= 5  and div <= 9:
			nroman0=nroman0+romanL(div)
			#print('comprobando ' + nroman0)
			#print('print div vale ahora '+ str(div))
		elif div >=1 and div <= 4:
				#print 'entre en las decenas menores que 5'
				nroman0=nroman0+romanX(div)
				#print('comprobando ' + nroman0)
				#print('print div vale ahora '+ str(div))
				#print('print power vale ahora '+ str(power))
	if power == 1: 
		#print('entre en power 1')
		if div >= 5 and div <= 9:
			nroman0=nroman0+romanV(div)
			#print('comprobando ' + nroman0)
		elif div < 5:	
        		nroman0=nroman0+romanI(div)
        		#print('comprobando ' + nroman0)
	#div = mod/10
	divaux=mod   #variable for keep the mod value before change, because it is necesario for the new value of div
	#divaux= div
	power= power/10
	#divaux=div
	#div = divaux/power
	#print('**  1 **')
	#print('The number ' + str(num) + ' in old roman numbers is: '+ nroman0)
	if divaux == 0 and power == 0 and mod == 0:
		break
	elif mod == 0:
		break
	else:
		div = divaux/power	
		mod= divaux%power
	#div = mod/10
	#print('print div vale ahora al final '+ str(div))
	#print('print power vale ahora al final '+ str(power))
	#print('print modulo vale ahora al final '+ str(mod))
	#print('*')
	#print('print div vale ahora al final '+ str(div))
	#print('print power vale ahora al final '+ str(power))
	#print('print modulo vale ahora al final '+ str(mod))
	#print('comprobando de nuevo despues del if ' + nroman0)
	#print('Terminando ciclo: '+str(x))
	#print('*********')

print('The number ' + str(num) + ' in old roman numbers is: '+ nroman0)


		

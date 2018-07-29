#Leap years. Write a program that asks for a starting year and an ending 
#year and then puts all the leap years between them (and including them,
#if they are also leap years). 
#Leap years are years divisible by 4 (like 1984 and 2004). 
#However, years divisible by 100 are not leap years (such as 1800 and 1900) 
#unless they are also divisible by 400 (such as 1600 and 2000,
# which were in fact leap years). What a mess!
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


# if int(year1)%4 == 0 or int(year1)%400 == 0 and int(year1)%100 != 0 :
#    print (year1 + ' it is leap year')
#    for x in xrange(int(year1),(int(year2)+1),4):
# 	if int(x)%4 == 0 or int(x)%400 == 0 and int(x)%100 != 0 :
# 		n=n+1
# 		print(str(x) + ' I am leap')
# else:
# 	print (year1 + ' are no leap years')
# 	yearaux=int(year1)
# 	while yearaux %4 != 0 or yearaux %400 != 0 and yearaux %100 == 0 :
# 		yearaux=yearaux+1
# 		print('estou aumentando el ano a '+str(yearaux))
# 	for x in xrange(yearaux,(int(year2)+1),4):
# 		if int(x)%4 == 0 and int(x)%400 == 0 and int(x)%100 != 0 :
# 			n=n+1
# 			print( str(x) + ' I am leap')

print ('The number of leap years between ' + year1 + ' and ' + year2 +' (including them in the countingo) are:' + str(n))



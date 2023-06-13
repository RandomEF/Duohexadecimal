import math
from Base62Switch import *

power = 0

def DigRequ(num):
	'''
 	For a given decimal input, this will calculate how many digits of Base62 is required to hold the number
	'''
	global power
	power = 0
	searching = True
	while searching:
		if ((math.pow(62, power) - 1) >= num):
			searching = False
			#print(f"Digits required: {power}")
			return power
		else:
			power += 1

def To62(num):
	'''
 	Converts a number to Base62
	'''
	DigRequ(num)
	result = ''
	remainder = num
	for i in range(power - 1, -1, -1): # Finds the value for each of the digits
		for j in range(0, 62, 1):
			#print("j: " + str(j))
			subtractor = j * math.pow(62, i)
			if remainder < 0:
				raise Exception('Remainder is negative')
			elif remainder < ((j+1) * math.pow(62, i)):
				#print("subtractor: ", subtractor)
				#print('works ' + str(i))
				remainder = remainder - subtractor
				#print("remainder: ", remainder)
				result += (STo62(j))
				break
			else:
				j += 1
	print(f"{num} in duohexadecimal is {result}.")

def To10(num):
	'''
	Converts a Base62 number to decimal
	'''
	result = 0
	power = 0
	num = str(num)
	for i in range(len(num)):
		i += 1
		val = num[-i]
		valConv = STo10(val)
		result += int(math.pow(62, power) * valConv)
		power += 1
	result = str(result)
	print(f"{num} in denary is {result}.")

def Menu():
	pass
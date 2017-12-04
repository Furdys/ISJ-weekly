#!/usr/bin/env python3

# [ISJ] Project 5
# Author: Jiri Furda (xfurda00)

import re
import bisect

NONE = object() # Empty object for checking optional parameters

class Polynomial:
	"Polynomial class represented as list"





	def __init__(self, *params1, **params2):
		self.values = [] 																														# Create empty list for base values

		if len(params1) == 1 and len(params2) == 0 and isinstance(params1, tuple): 	# Check for first type of parameters
			paramlist = params1[0]
		elif len(params1) > 0 and len(params2) == 0: 																# Check for second type of parameters
			paramlist = list(params1)
		elif len(params1) == 0 and len(params2) > 0:  															# Check for third type of parameters	
			exp = []   																																# Create empty list for exponents
			base = [] 																																# Create empty list for base values
			for dic in params2.items(): 																							# Cycle for every parameter
				if isinstance(dic[0], str) == 0 or re.search(r'^x[0-9]+$',dic[0]) == 0 or isinstance(dic[1], int) == 0: # Check for correct form
					raise ValueError()
				else:
					exp.append(dic[0][1:]) 																								# Add exponent to end of list
					base.append(dic[1]) 																									# Add base to end of list
				
			exp, base = (list(t) for t in zip(*sorted(zip(exp, base)))) 							# Sort base and exponent based on exponent value			
	
			paramlist = [] 																														# Create empty list for parameters
			i = 0 																																		# Counter for going through every exponent
			e = 0 																																		# Counter for going through original list of base
			while i <= int(exp[-1]):  																								# Cycle for every exponent
				if i == int(exp[e]):																										# If this exponent was in original list
					paramlist.append(int(base[e])) 																				# Add exponent to end of the list
					e +=1
				else:
					paramlist.append(0) 																									# Add zero to end of the list 
				i += 1
		
		for param in paramlist: 																										# For every paramater in new parametrs ist
			if isinstance(param, int) == False:  																			# Check for correct type of parameter 
				raise ValueError()
		
		self.values = paramlist 																										# Save list of parameters to instance of class



	def __str__(self):
		res = ""   															# Create empty variable for result
		
		index = len(self.values)-1 							# Max value of index (= exponent) 
		for base in self.values[::-1]: 					# Backward cycle for every base 
		
			if base == 0: 												# Don't write if base is zero
				index -= 1
				continue   													# Skip to next base
			
			if base == -1 and index != 0: 				# Don't write 1 if it's -1
				base = " - "
			elif base == 1 and index != 0: 				# Don't write number if it's +1
				base = " + "
			elif base < 0: 												# If number is negative
				base = " - {:d}".format(abs(base))
			else: 																# If number is positive
				base = " + {:d}".format(base)
			
			if index == 0: 												# If exponent is 0 then x^0=1 -> exp part is empty
				exp = ""
			elif index == 1: 											# If exponent is 1 then x^1=x
				exp = "x"
			else: 																# Use normal form for every other exponent
				exp = "x^{:d}".format(index)
			
			res += "{:s}{:s}".format(base,exp)  	# Add current part of polynomial	
			index -= 1

		if res[:2] == " +":											# If first number is postitive
			return res[3:] 												# Cut first three characters
		if res[:2] == " -": 										# If first number is negative
			return res[1:] 												# Cut first two characters
		if res == "": 													# If there are nothing to print
			return "0" 														# Return zero
		
		return res															# Return result
	
			
			
	def __add__(self, other):
		if len(self.values) > len(other.values): # Findout which polynom has biggest exponent
			big = self.values[:]
			small = other.values[:]
		else:
			big = other.values[:]
			small = self.values[:]		
			
		i = 0		
		while i < len(small): 		# Cycle for every part in shorter polynom 
			big[i] += small[i] 			# Add value of shorter polynom to longer  
			i += 1
		return Polynomial(big) 		# Return longer polynom
				
				
				
	def __eq__(self, other):
		if str(self) == str(other): 	# If printed polynom is same as the second one
			return True
		else:
			return False
			
			
			
	def derivative(self):
		i = 0
		res = [0]*(len(self.values)-1) 	# Create empty list for result
		
		if res == []: 									# If there is only first exponent
			return 0
		
		for value in self.values: 			# For every base in polynom
			res[i-1] = value*i 						# Count derivated value
			i += 1
		return Polynomial(res) 					# Return derivated polynom
		
		
		
	def at_value(self, val1, val2=NONE):
		
		if isinstance(val1, int) == 0 and isinstance(val1, float) == 0: # Check if first parameter is in correct form
			raise ValueError()
			
		res1 = 0  										# Variable for first result
		res2 = 0 											# Variable for second result
		exp = 0 											# Counter for exponent
		
		for base in self.values: 			# For every base in polynom
			res1 += base*(val1**exp) 		# Count value of this part of polynom
			exp += 1
			
			
		if val2 == NONE: 							# If there is not second parameter
			return res1 								# Return first result
		else: 
			
			if isinstance(val2, int) == 0 and isinstance(val2, float) == 0: # Check if second parameter is in correct form
				raise ValueError()
			
			exp = 0	
			for base in self.values: 		# For every base in polynom
				res2 += base*(val2**exp) 	# Count value of this part of polynom
				exp += 1
			return res2-res1 						# Return difference between first result and second result




	def __pow__(self, power):
		tmp = self.values[:] 					# Copy base list

		if power < 0: 								# Check if power dont have wrong value
			raise ValueError()
					
		if power == 1: 								# Check if power is one
			return self 								# Don't change anything
		if power == 0: 								# Check if power is zero
			return Polynomial([1]) 			# Return zero
		
		i = 1
		while i < power: 							# Cycle for every iterration
			a = 0
			b = 0
			res = [0]*(len(tmp)+1) 			# Create empty list for result
			
			while a < len(self.values):
				while b < len(tmp):
					res[a+b] += self.values[a] * tmp[b] # Count temporary calculation 
					b += 1
				a += 1
				b = 0
				
			tmp = res 									# Save result to temporary variable
			i += 1
			
		return Polynomial(res) 				# Return result

def test():
    assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
    assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1,x1=1)
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2,x1=3,x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2,3,4,-5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
    pol5 = Polynomial([1,0,-2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1,3.6) == -23.92
    assert pol5.at_value(-1,3.6) == -23.92

if __name__ == '__main__':
    test()

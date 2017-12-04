#!/usr/bin/env python3

# [ISJ] Project 5
# Author: Jiri Furda (xfurda00)

def first_nonrepeating(input):
	"Returns first nonrepeating character"
	for char in input:
		if input.count(char) == 1:
			return char
			
			
def combine4(numbers,result):
	"Return list of solutions for matematics puzzle with specified numbers and result"
	if type(numbers) != list or type(result) != int:
		raise ValueError()
	
	# Number combinations generator
	numComb = []
	x = 4
	a = 0
	while a < x:
		tmpListA = numbers[:]
		tmpListA.remove(numbers[a])
		b = 0
		
		while b < 3:
			tmpListB = tmpListA[:]
			tmpListB.remove(tmpListB[b])
			
			sublist = [numbers[a],tmpListA[b],tmpListB[0],tmpListB[1]]
			if sublist not in numComb:
				numComb.append(sublist)
			
			sublist = [numbers[a],tmpListA[b],tmpListB[1],tmpListB[0]]
			if sublist not in numComb:
				numComb.append(sublist)
			b += 1
		
		a += 1
	
	# Operation combinations generator
	operations = ['+', '-', '*', '/']
	opComb = []
	
	for x in operations:
		for y in operations:
			for z in operations:
				opComb.append([x, y, z])
	
	# Brackets combinations			
	braComb = [
	'{:d}{:s}{:d}{:s}{:d}{:s}{:d}',
	'({:d}{:s}{:d}){:s}{:d}{:s}{:d}',
	'{:d}{:s}({:d}{:s}{:d}){:s}{:d}',
	'{:d}{:s}{:d}{:s}({:d}{:s}{:d})',
	'({:d}{:s}{:d}){:s}({:d}{:s}{:d})',
	'({:d}{:s}{:d}{:s}{:d}){:s}{:d}',
	'{:d}{:s}({:d}{:s}{:d}{:s}{:d})',
	'(({:d}{:s}{:d}){:s}{:d}){:s}{:d}',
	'({:d}{:s}({:d}{:s}{:d})){:s}{:d}',
	'{:d}{:s}(({:d}{:s}{:d}){:s}{:d})',
	'{:d}{:s}({:d}{:s}({:d}{:s}{:d}))']

	# Result test for combiantions
	resList = []
	for nums in numComb:
		for ops in opComb:
			for bras in braComb:
				tmpNums = nums[:]
				tmpOps = ops[:]
				formatList = []
				formatList.append(tmpNums.pop(0))
				for num in tmpNums:
					formatList.append(tmpOps.pop(0))
					formatList.append(num)				

				form = bras.format(*formatList)
				try:
					formRes = eval(form)
				except ZeroDivisionError:
					pass
				else:
					if formRes == result:
						resList.append(form)
	return resList

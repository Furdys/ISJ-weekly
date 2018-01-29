#!/usr/bin/env python3

""" 
[ISJ] Project 4 (2017-03-30)
Author: Jiri Furda (xfurda00)
""" 

import re
import string
import itertools

def balanced_paren(parenstr):
	"This function check if there are correctly used brackets in the string parameter"
	brackets = re.findall(r'[\(\)\[\]{}<>]', parenstr)	# Find all brackets in parenstr
	
	lBrackets = ['[', '(', '{', '<']	# List of left brackets
	rBrackets = [']', ')', '}', '>']	# List of right brackets
	stack = []	# List for stacking left brackets with no pair yet
	
	if brackets:	# Check if there is any bracket in parenstr
		lookfor = ""	# Variable for searched bracket
		
		for bracket in brackets:	# Cycle for every bracket in parenstr
			if re.match(r'[\[\({<]',bracket):	# Check if it is an opening bracket
				index = lBrackets.index(bracket)	# Get index of bracket (relative to lBrackets)
				stack.append(index)	# Add the index to stack for later checking
				lookfor = rBrackets[index]	# Save searched right bracket
				continue	# Skip to next bracket
				
			if bracket == lookfor:	# Check if the bracket is the searched one
				stack.pop()	# Remove last bracket from the stack
				if len(stack) > 0:	# Check if stack is not empty
					lookfor = rBrackets[stack[-1]]	# Set searched right bracket to previous one if it not empty
				else:
					lookfor = ""	# Set searched right bracket to none if it is empty
				continue	# Skip to next bracket 
				
			return False	# Return false if there is incorrectly used bracket
	
	if len(stack) == 0:	# Check if stack is empty
		return True	# Return true if yes
	else: 
		return False	# Return false if not
	
NONE = object()	# Create empty object to check for optional parameter
	
def caesar_list(word, key=NONE):
	"This function uses Caesar cipher to encode string in first parameter using list of keys in optional second parameter"
	if re.search(r'[^a-z]',word):	# Check if there is any non-allowed character
		raise ValueError('Wrong input (Use only lowercase English alphabet)')	# Print error
		
	if key == NONE:	# Check if there is any key defined
		key = [1,2,3]	# Use the default one if not
		
	alphabet = list(string.ascii_lowercase)	# List of every lowercase character in English alphabet
	keylen = len(key)	# Save length of the key
	res = ""	# Create variable for result
	i = 0	# Create index to navigate trough the key
	
	for letter in word:	# Cycle for every letter in 'word'
		res += alphabet[(alphabet.index(letter) + key[i]) % 26]	# Add encoded character to the end of 'res'
		i = (i + 1) % keylen	#	Set index to next one in the key
	
	return res
		
def caesar_varnumkey(word, *key):
	"This function uses Caesar cipher to encode string in first parameter using keys in every other optional parameter"
	newkey = []	# List for keys
	for arg in key:	# Cycle for every parameter except 'word'
		newkey.append(arg)	# Add key to end of list
	if newkey == []:	# Check if there were none key parameters
			return caesar_list(word)	# Use function 'caesar_list' without key parameter to encode
	return caesar_list(word, newkey)	# Use function 'caesar_list' to encode

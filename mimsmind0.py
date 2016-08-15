#mimsmind0_SH.py

#!/usr/bin/python3

#import functions to be used
import sys
import random

#check command line for digit length
#if length of argument is greater than 1, try to store it as an int
if len(sys.argv) > 1: 
	try:
		digit_count = int(sys.argv[1])
	except Exception, e:
		#quit with error if len is not a number
		print("Invalid command line input", e)
		sys.exit(1)
	else:
		#quit with error if len is zero or negative
		if len(sys.argv) <= 0:
			print ("Invalid command line input")
			sys.exit(1)
else:
	#if nothing given, then set digit_count to 1
	digit_count = 1

#set variables
count_tries = 0
max_number = 10**digit_count - 1
answer = random.randint(0, max_number)
prompt = "Guess a %d-digit number:" %digit_count

#welcome message
print("Let's play the mimsmind game")

while True:
	#ask the user to make a guess, input func takes input as string
	guess_string = input(prompt)

	#check to see if guess_string is an int
	try: 
		guess_int = int(guess_string)
	except ValueError: 
		input_valid = False
	else:
		input_valid = (guess_int >= 0 and guess_int <= max_number)

	if not input_valid:
		print("Invalid input. Looking for a number between 1 and %d" %max_number)
	else:
		count_tries += 1

		#if guess matches answer, congratulate
		if guess_int == answer:
			print ("Congratulations. You guessed the correct number in %d tries." % count_tries)
			sys.exit(0)
		#if not, try again
		print ("Try again.")
		
		if guess_int < answer:
			prompt = "Guess a higher number: "
		else:
			prompt = "Guess a lower number: "


















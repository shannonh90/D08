#mimsmind1_SH

#import
import sys
import random

#check command line for digit length
#if length of argument is great than 1, try to store it as an int
	#if its < 1, raise an exception
	#if its not an integer, ask for another 
if len(sys.argv) > 1:
	try: 
		digit_count = int(sys.argv[1])
	except ValueError:   
		print("Invalid command line input.")
		sys.exit(1)
	else:
		if len(sys.argv) <= 0:
			print ("Invalid command line input")
			sys.exit(1)
else:
	digit_count = 3

#set variables
prompt = "Guess a %d-digit number: " %digit_count
max_rounds = 2**(digit_count) + digit_count
count_tries = 0
max_number = 10**digit_count - 1
answer = random.randint(0, max_number)
answer_string = str(answer).zfill(digit_count)  #need zfill to pad for 3 digits

#welcome message
print("Let's play the mimsmind1 game. You have %d guesses." %max_rounds)
while True:
	guess_string = input(prompt)

#make sure input is valid, if yes, make sure in range
#if no, take away a try, and have them guess again
	try:
		guess_int = int(guess_string)
	except:
		input_valid = False
	else:
		input_valid = (guess_int >= 0 and guess_int <= max_number)

	if not input_valid:
		print("Invalid input. Try again: ")
	else:
		count_tries += 1

		if guess_int == answer:
			print("Congratulations. You guessed the correct number in %d tries." %count_tries)
			sys.exit(0)

		#Next is the bulls + cows, first set variables.
		count_bulls = 0
		count_cows = 0
		position = 0
		for digit in answer_string:
			find_result = guess_string.find(digit, position, position+1)
			if find_result > -1:
				count_bulls += 1
			else:
				find_result = guess_string.find(digit)
				if find_result > -1:
					count_cows += 1
			position += 1

		prompt = "%d bull(s), % d cow(s). Try again: " %(count_bulls, count_cows)
print("Sorry. You did not guess the number in %d tries. The correct number is %s." %(max_rounds, answer_string))






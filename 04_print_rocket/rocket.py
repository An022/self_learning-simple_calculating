"""
File: rocket.py
Name:An Lee
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
	"""
	Pre-condition:
	It's totally nothing here.
	User can input different constant into the SIZE to determine the rocket size.

	Post-condition:
	Print out a pretty rocket which size is determined by the user's input constant.
	"""
	build_rocket()


def build_rocket():
	# The rocket is composed of the head, the belt, the upper and the lower.
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def lower():
	# The parts of rocket's lower included : "|" , ".", "/" and "\".
	for i in range(SIZE):
		# Each row of rocket's upper always started with a part "|".
		print('|', end="")
		# At the started row, the number of "." is equal to 0.
		# With each row increases, the number of "." increases 1 more time than previous row.
		for j in range(i):
			print('.', end="")
		# At the started row, the number of "\" and "/" are both equal to SIZE(the total number of row).
		# With each row increases, the number of "\" and "/" are both decrease 1 more time than previous row.
		for k in range(SIZE-i):
			print('\\', end="")
			print('/', end="")
		# At the started row, the number of "." is equal to 0.
		# With each row increases, the number of "." increases 1 more time than previous row.
		for h in range(i):
			print('.', end="")
		# Each row of rocket's upper always ended with a part "|".
		print('|')


def upper():
	# The parts of rocket's upper included : "|" , ".", "/" and "\".
	for i in range(SIZE):
		# Each row of rocket's upper always started with a part "|".
		print('|', end="")
		# At the started row, the number of "." is equal to the number of SIZE-1.
		# With each row increases, the number of "." decreases 1 more time than previous row.
		for j in range(SIZE-1-i):
			print('.', end="")
		# At the started row, the number of "/" and "\" are both equal to 1.
		# With each row increases, the number of "/" and "\" are both increase 1 more time than previous row.
		for k in range(1 + i):
			print('/', end="")
			print('\\', end="")
		# At the started row, the number of "." is equal to the number of SIZE-1.
		# With each row increases, the number of "." decreases 1 more time than previous row.
		for h in range(SIZE-1-i):
			print('.', end="")
		# Each row of rocket's upper always ended with a part "|".
		print('|')


def belt():
	# The parts of rocket's belt included : "+" and "=" .
	# The belt always started with a part "+".
	print('+', end="")
	# The number of "=" is equal to double SIZE.
	for i in range(SIZE*2):
		print('=', end="")
	# The belt always ended with a part "+".
	print('+')


def head():
	# The parts of rocket's head included : " ", "/" and "\".
	for i in range(SIZE):
		# At the started row, the number of "space" is equal to SIZE(the total number of row).
		# With each row increases, the number of "space" decreases 1 more time than previous row.
		for j in range(SIZE-i):
			print(' ', end="")
		# At the started row, the number of "/" is equal to 1.
		# With each row increases, the number of "/" increases 1 more time than previous row.
		for k in range(i+1):
			print('/', end="")
		# At the started row, the number of "\" is equal to 1.
		# With each row increases, the number of "\" increases 1 more time than previous row.
		for h in range(i+1):
			print('\\', end="")
		# This is the end of each row, let's go to the next row.
		print("")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
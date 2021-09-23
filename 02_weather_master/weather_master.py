"""
File: weather_master.py
Name: An Lee
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This number controls when to quit the program.
EXIT = -100


def main():
	"""
	User put in data of temperature, then program will calculate and show information including:
	highest temperature, lowest temperature, average and cold day(s).
	pre-condition: Inform user to put data.
	post-condition: Show the calculating result of highest temperature, lowest temperature, average and cold day(s).
	"""
	print('stanCode "Weather Master 4.0"')
	data = int(input('Next Temperature : (or -100 to quit)?'))
	# check we should keep calculating or quit.
	if data == EXIT:
		print('No Temperatures were entered.')
	else:
		# If the number is not -100(quot), we have to start calculating.
		maximum = data
		minimum = data
		numerator = data
		denominator = 1
		average = numerator / denominator
		cold_days = 0
		while True:
			data = int(input('Next Temperature : (or -100 to quit)?'))
			# check we should keep calculating or quit.
			if data == EXIT:
				break
			# keep update the maximum data.
			if maximum < data:
				maximum = data
			# keep update the minimum data.
			if minimum > data:
				minimum = data
			# update numerator and denominator for average
			numerator += data
			denominator += 1
			average = numerator / denominator
			# update the accumulated cold days(if any temperature <16 is a cold day).
			if data < 16:
				cold_days += 1
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(average))
		print(str(cold_days) + ' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()

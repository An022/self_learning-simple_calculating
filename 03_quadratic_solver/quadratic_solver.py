"""
File: quadratic_solver.py
Name: An Lee
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math
import time

def main():
	"""
	If user give the constant a, b and C, we can find roots of quadratic equation: a^2x+bx+c=0.
	pre-condition:
	Inform user put the constant(a,b and c) data in order to find root(s) of quadratic equation: a^2x+bx+c=0.
	post-condition:
	Show user the root(s) of the quadratic equation: a^2x+bx+c=0 with the given input constant of a, b and c.
	"""
	print('stanCode Quadratic Solver:')

	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	start = time.time()
	discriminant = b*b-4*a*c

	# check discriminant is >0, ==0 or <0, then calculate the roots.
	if discriminant > 0:
		root_discriminant = math.sqrt(discriminant)
		ans1 = (-b + root_discriminant) / 2 * a
		ans2 = (-b - root_discriminant) / 2 * a
		print('Two roots: '+str(ans1)+' , '+str(ans2))
	elif discriminant == 0:
		root_discriminant = math.sqrt(discriminant)
		ans1 = (-b + root_discriminant) / 2 * a
		print('One root: ' + str(ans1))
	else:
		print('No real roots.')
	end = time.time()
	print("The time of execution of above program is :", end - start)







###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
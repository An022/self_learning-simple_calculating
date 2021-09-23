"""
File: hailstone.py
Name: An Lee
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

FINAL = 1
import time

def main():
    """
    User enter a number, and this program will compute Hailstone sequences.
    Hailstone Sequences follow rules:
    If a number is odd, multiply it by 3 and add 1.
    If a number is even, divide it by 2
    pre-condition: Waiting user to input a number.
    post-condition: Show user how many the steps are took to reach 1.
    """
    print('This program computes Hailstone sequences.')
    data = int(input('Enter a number: '))
    start = time.time()
    n = data
    steps = 0
    # Check if the number is 1 or not.
    if n == FINAL:
        print('It took ' + str(steps) + ' steps to reach 1.')
    # If the number is not 1, we have to start calculating until it reach 1.
    else:
        while True:
            # Every time, check if the number is 1(stop) or not.
            if n == FINAL:
                break
            # If a number is odd, multiply it by 3 and add 1.
            if data % 2 == 1:
                n = 3*n+1
                print(str(data) + ' is odd, so I make 3n+1: ' + str(n))
            # If a number is even, divide it by 2.
            if data % 2 == 0:
                n = n//2
                print(str(data) + ' is even, so I take half: ' + str(n))
            data = n
            steps += 1
        print('It took ' + str(steps) + ' steps to reach 1.')
        end = time.time()
    print("The time of execution of above program is :", end - start)

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()

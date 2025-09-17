#! /usr/bin/env python3

position = input('Enter the position in the Fibonacci sequence: ')

# initiate our Fibonacci sequence
a, b = 0, 1

# find the requested number
for i in range(int(position)):
	a,b = b,a+b

fibonacci_number = a

print(f"The Fibonacci number for {position} is {fibonacci_number}")
#! /usr/bin/env python3

import argparse

# import the command line arguments

# create an argument parser object
parser = argparse.ArgumentParser(description = "This script \
	calculates the number in the Fibonacci sequence")

# add our required (positional) argument
parser.add_argument("position", help = "position in the Fibonacci sequence", type = int)

# add optional arguments
# if 'store_true', this means assign 'True' if the argument is specified
# in the command line, so the default for 'store_true' is false
parser.add_argument("-v", "--verbose", 
	help = "whether to print verbose output, default = false", 
	action = 'store_true')


# parse the argument line
args = parser.parse_args()

# position = input('Enter the position in the Fibonacci sequence: ')

# initiate our Fibonacci sequence
a, b = 0, 1

# find the requested number
for i in range(int(args.position)):
	a,b = b,a+b

fibonacci_number = a

if args.verbose:
	print(f"The Fibonacci number for {args.position} is {fibonacci_number}")
else:
	print(fibonacci_number)

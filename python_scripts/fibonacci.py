#! /usr/bin/env python3

import argparse

# import the command line arguments

# create an argument parser object
parser = argparse.ArgumentParser(description = "This script \
	calculates the number in the Fibonacci sequence")

# add our required (positional) argument
parser.add_argument("position", help = "position in the Fibonacci sequence", type = int)

# parse the argument line
args = parser.parse_args()

# position = input('Enter the position in the Fibonacci sequence: ')

# initiate our Fibonacci sequence
a, b = 0, 1

# find the requested number
for i in range(int(args.position)):
	a,b = b,a+b

fibonacci_number = a

print(f"The Fibonacci number for {args.position} is {fibonacci_number}")


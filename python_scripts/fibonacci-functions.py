#! /usr/bin/env python3

import argparse

# get input
def get_args():
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

	args = parser.parse_args()

	return args


# calculate the fibonacci number
def calc_fib(fib_position):
	# initiate our Fibonacci sequence
	a, b = 0, 1

	# find the requested number
	for i in range(fib_position):
		a,b = b,a+b

	fibonacci_number = a

	return fibonacci_number


# print the results
def print_output(fib_number, fib_position):
	if args.verbose:
		print(f"The Fibonacci number for {fib_position} is {fib_number}")
	else:
		print(fib_number)

# main
def main():
	fib_num = calc_fib(args.position)

	print_output(fib_num, args.position)


# parse the argument line
args = get_args()

# set the environment for this script
# is it main (is it a standalone script), or is this a module being called by another script
if __name__ == '__main__':
	main()

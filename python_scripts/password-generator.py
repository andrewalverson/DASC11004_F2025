#! /usr/bin/env python3

# pip or pip3 to install packages

import random
import string
import argparse

# create an arugment parser object
parser = argparse.ArgumentParser(description = "This script \
	generates a secure password of the desired length")

# add the required (positional) argument, i.e., the password length
parser.add_argument("pw_length", help = "Desired password length (integer)", type = int)

# parse the arguments
args = parser.parse_args()

# create a variable to hold the password
password = ''


# a single string with all the possible password characters
# lowercase are included twice so we get more of those
characters = string.ascii_letters + string.ascii_lowercase + string.digits + string.punctuation

for i in range(args.pw_length):
	password += random.choice(characters)

print(password)


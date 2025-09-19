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

# ensure there is at least one digit and one punctuation character
password  = random.choice(string.punctuation)
password += random.choice(string.digits)


# loop over the desired pw length, but subtract 2 because above we already
# added 2 characters, 1 digit and 1 punctuation character
for i in range(args.pw_length - 2):
	password += random.choice(characters)

# randomize the password so the first two characters are less determinant

print(f"before: {password}")

# first convert it to a list
char_list = list(password)
random.shuffle(char_list)
shuffled_password = ''.join(char_list)

print(f"after: {shuffled_password}")


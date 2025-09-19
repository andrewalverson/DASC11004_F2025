#! /usr/bin/env python3

# pip or pip3 to install packages

import random
import string

# create a variable to hold the password
password = ''

pw_length = input("Enter the password length: ")
pw_length = int(pw_length)

# a single string with all the possible password characters
# lowercase are included twice so we get more of those
characters = string.ascii_letters + string.ascii_lowercase + string.digits + string.punctuation

for i in range(pw_length):
	password += random.choice(characters)

print(password)


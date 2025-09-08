#!/usr/bin/env python3

# get the input values
bill = input('Enter the bill amount (float): ')
tip = input('Enter the tip percentage (integer): ')

# convert input to float and int
bill = float(bill)
tip = int(tip)

# calculate tip amount
tip_amount = bill*(tip/100)
total = bill + tip_amount

# print out the receipt
print()
print(f'Bill: ${bill}')
print(f'Tip: ({tip}%): ${tip_amount:.2f}')
print('----------------')
print(f'Total: ${total:.2f}')
print()


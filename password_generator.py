
#Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cap_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '>', '<', '?', '*', '+', '-', '=', '~', '`']

print("Welcome to the PythonPassword Generator!")

nr_cap_letters = int(input("How many Capital letters would you like in your password?\n"))
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#empty lists to store the items to make up password
cap_letter = []
letter = []
number = []
symbol = []

# loops to select the amount of random letters, numbers and symbols wanted, that were selected by user 
for cap_letter in range(nr_cap_letters):
  cap_letter = random.sample(cap_letters, nr_cap_letters)

for letter in range(nr_letters):
  letter = random.sample(letters, nr_letters)
  

for number in range(nr_numbers):
  number = random.sample(numbers, nr_numbers)
  
for symbol in range(nr_symbols):
  symbol = random.sample(symbols, nr_symbols)

#concatinate into one string
password = cap_letter + letter + number + symbol

# take the numbers, letters, symbols and shuffle into random order
random.shuffle(password)

# form into one string
password = ''.join(password)

#print new single string password to User
print(f"Here is your new secure password: {password}")


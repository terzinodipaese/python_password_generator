import random

capital_letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

lowercase_letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [
    '!', '#', '$', '%', '&', '(', ')', '*', '+', '\\', '/', '@', '=',
    '.', ':', '^', '[', ']', '{', '}', '-', '\'', '"', '£', "|", "?"
]

print("\t***\tPython Password Generator\t***")

# some data quality checks
nr_capital_letters_contains_digits = False
while(nr_capital_letters_contains_digits == False):
    nr_capital_letters = input("How many capital letters would you like in your password?\n")
    nr_capital_letters_contains_digits = nr_capital_letters.isdigit()
    if(nr_capital_letters_contains_digits == True):
        nr_capital_letters = int(nr_capital_letters)
        break
    else:
        print("You typed non digit characters. Please try again xP")


nr_lowercase_letters_contains_digits = False
while(nr_lowercase_letters_contains_digits == False):
    nr_lowercase_letters = input("How many lowercase letters would you like in your password?\n")
    nr_lowercase_letters_contains_digits = nr_lowercase_letters.isdigit()
    if(nr_lowercase_letters_contains_digits == True):
        nr_lowercase_letters = int(nr_lowercase_letters)
        break
    else:
        print("You typed non digit characters. Please try again xP")


nr_symbols_contains_digits = False
while(nr_symbols_contains_digits == False):
    nr_symbols = input("How many symbols would you like in your password?\n")
    nr_symbols_contains_digits = nr_symbols.isdigit()
    if(nr_symbols_contains_digits == True):
        nr_symbols = int(nr_symbols)
        break
    else:
        print("You typed non digit characters. Please try again xP")


nr_numbers_contains_digits = False
while(nr_numbers_contains_digits == False):
    nr_numbers = input("How many digits would you like in your password?\n")
    nr_numbers_contains_digits = nr_numbers.isdigit()
    if(nr_numbers_contains_digits == True):
        nr_numbers = int(nr_numbers)
        break
    else:
        print("You typed non digit characters. Please try again xP")

password_list = []

for char in range(1, nr_capital_letters + 1):
    password_list.append(random.choice(capital_letters))

for char in range(1, nr_lowercase_letters + 1):
    password_list.append(random.choice(lowercase_letters))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
# another shuffling LOL
random.shuffle(password_list)

# convert list to string for printing
pwd = "".join(password_list)
print(f"Your random password to use is: {pwd}")
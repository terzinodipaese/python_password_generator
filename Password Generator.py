import sys
import random

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789|!"£$%&/()=?^+*§°#<>;.-_,\{}[]'
length = input('Choose password length    <<<')
length = int(length)
password = ''

for c in range(length):
    password += random.choice(chars)

print(password)

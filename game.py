"""A number-guessing game."""

# Put your code here

import random

hello = "hello whats your name"
name = " "
greeting = hello + " " + name
print(greeting)

my_name = input(" ")
greeting = my_name + " " "Im thinking of a number between 1 and 100 try to guess my number"
print(greeting)

num = random.randint(1, 100)
while True:

    guess = input()
    i = int(guess)
    if i == num:
        print('You won!!!')
        break
    elif i < num:
        print('Try Higher')
    elif i > num:
        print('Try Lower')

print('if you got it in less than 9 tries you won')

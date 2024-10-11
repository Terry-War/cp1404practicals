"""CP1404 Practical 4 - List Exercise"""

# Write a program that prompts the user for 5
# numbers and then stores each of these in a list
# called numbers.
# The program should then output information about
# these numbers, as in the output below.
# You can use the functions min, max, sum and len,
# and you can use the append method to add a number
# to a list.
#
# expected results
#    Number: 5
#    Number: 20
#    Number: 1
#    Number: 2
#    Number: 3
#    The first number is 5
#    The last number is 3
#    The smallest number is 1
#    The largest number is 20
#    The average of the numbers is 6.2

# 1. Numbers
numbers = []
# Prompting user for 5 numbers
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

# Displaying information about the numbers
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

# 2. Security checker
# Woefully inadequate security checker
# Please use the same file, list_exercises.py
#
# Copy the following list of usernames:
#    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
#    'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
#    'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
# Ask the user for their username. If the username is in the above list of authorised users,
# print "Access granted", otherwise print "Access denied".

usernames = [
    'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
    'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
    'Command', 'ExecState', 'InteractiveConsole',
    'InterpreterInterface', 'StartServer', 'bob']

user_input = input("Enter your username: ")

if user_input in usernames:
    print("Access granted")
else:
    print("Access denied")

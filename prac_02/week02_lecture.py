from random import randint

low_number = int(input("Enter lowest number: "))
high_number = int(input("Enter highest number: "))
while low_number >= high_number:
    print("Please enter a higher number then the lower number.")
    low_number = int(input("Enter lowest number: "))
    high_number = int(input("Enter highest number: "))
smiley_number = randint(low_number, high_number)
print(":) " * smiley_number)

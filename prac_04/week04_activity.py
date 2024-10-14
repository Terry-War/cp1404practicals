"""
Seminar 4 - Lists
Given a list of names, prompt the user to remove names
until they enter an empty string.
Ensure the program does not crash when the name is not in the list.
"""

names = ["Ada", "Alan", "Bill", "John"]
print(", ".join(names))
name_to_remove = input("Who do you want to remove? ").title()
while name_to_remove != "":
    try:
        names.remove(name_to_remove)
    except ValueError:
        pass
        name_to_remove = input("Who do you want to remove? ").title()
    print(", ".join(names))

# numbers
# number_of_people
# age
# data_points
# is_mutant
# i


# change the total to a float(number) and put the total outside and at the start of the with statement
# input_file can be shortened to in_file
# sum_of_numbers can be shortened to total
# the print should be outside the with statement
# numbers is a bad name for this task, use line instead
# could be better to use for line in file rather than readlines.etc


"""CP1404 Prac 06 - programming language
estimated time :
Started at:
finished at:
"""
"""Define the following methods:

__init__ - like most init functions, create the fields and set them to the parameters passed in.

is_dynamic() - which returns True/False if the programming language is dynamically typed or not.

[IMPORTANT] Please understand that this function will take no parameters other than self. The data is already inside the object, so you don't need to tell the object its own data.

This function's purpose is to encapsulate the functionality that would make the class more helpful.
See how the function name starts with is, like isupper(), isnumeric(), etc.?
So, it returns a Boolean.

Create a simple program in languages.py

Import the class, then copy these lines into your new program:

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
Now add the __str__ method to the class (not the client code), which should return a string like:

Python, Dynamic Typing, Reflection=True, First appeared in 1991

See if your __str__ function is working properly by running the program to check that printing works as expected.

Now create a new list that contains these three existing ProgrammingLanguage objects.

Do this next part on paper first, then copy it into PyCharm to see how you went.
Remember that writing code on paper (or a whiteboard) can help you learn better (since you can't depend on the IDE's help), and encourages you to be consistent and clear with syntax, indenting, etc.

Loop through and print the names of all the languages with dynamic typing (make sure you use your new is_dynamic method!), which should produce output like:

The dynamically typed languages are:
Python
Ruby"""
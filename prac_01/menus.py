"""CP1404 - Practicals 5 - Menus

Pseudocode for sales bonus
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
MENU_STRING = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")
print(MENU_STRING)
choice = input(">>> ").lower()
while choice != "q":
    if choice == "h":
        print("Hello", name)
    elif choice == "g":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print(MENU_STRING)
    choice = input(">>> ").lower()
print("Finished.")

"""CP1404 Practical 2. Password Stars."""

def main():
    min_length = 8  # Set minimum length for the password

    # Function to get a valid password from the user
    password = input(f"Enter a password with {min_length} characters: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input("Enter a password: ")

    # Print asterisks equal to the length of the password
    print("*" * len(password))


main()
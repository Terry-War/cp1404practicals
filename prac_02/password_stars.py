"""CP1404 Practical 2. Password Stars."""

def main():
    min_length = 8
    password = input(f"Enter a password with {min_length} characters: ")
    password = get_password(min_length, password)
    print_asterisks(password)

def get_password(min_length, password):
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input("Enter a password: ")
    return password

def print_asterisks(password):
    print("*" * len(password))
main()

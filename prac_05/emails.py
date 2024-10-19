"""CP1404 practical 5 - emails
estimated time : ~30 mins
Started at: 17:00
finished at: 17:20
"""


def main():
    """Create dictionary of emails to names"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract name from dictionary of emails provided"""
    return " ".join(email.split('@')[0].split('.')).title()


main()

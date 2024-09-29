"""
CP1404 - Practical 2 - score menu from scratch
"""

def main():
    score = 0
    choice = ''
    while choice != 'Q':
        print("\nMenu:\n(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")
        # I didn't like how in your lecture videos for the demo with function the menu didn't print, so I added the menu style from prac 01
        choice = input("> ").upper()
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Goodbye!")
        else:
            print("Invalid choice. Please choose again.")


def determine_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent score"
    elif score >= 50:
        return "Passable score"
    else:
        return "Bad score"


def get_valid_score():
    score = int(input("Enter a valid score (0-100): "))
    if score < 0 or score > 100:
        print("Invalid score, must be between 0 and 100.")
        score = get_valid_score()
    return score


def print_result(score):
    result = determine_score(score)
    print(f"The result for score {score} is: {result}")


def show_stars(number_of_stars):
    """ Print as many stars as the score. """
    for i in range(number_of_stars):
        print('*', end=' ')
    print()


main()

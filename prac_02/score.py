"""
CP1404 - Practical 2 - refactoring program to determine score status
"""

def main():
    score = float(input("Enter score: "))
    print(determine_score(score))

def determine_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent score"
    elif score >= 50:
        return "Passable score"
    else:
        return "Bad score"


main()

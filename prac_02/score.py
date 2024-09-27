"""
CP1404 - Practical 2 - debugging
Broken program to determine score status
"""


# original code
# score = float(input("Enter score: "))
# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#     print("Excellent")
# if score < 50:
#     print("Bad")

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

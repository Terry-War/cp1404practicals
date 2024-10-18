"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATES = {"QLD": "Queensland",
          "NSW": "New South Wales",
          "NT": "Northern Territory",
          "WA": "Western Australia",
          "ACT": "Australian Capital Territory",
          "VIC": "Victoria",
          "TAS": "Tasmania"}

print("State Names, hit enter to show all states")
state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(f"{state_code} is {STATES[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

# Print all states and their names neatly lined up
for state_code, state_name in STATES.items():
    print(f"{state_code:3} is {state_name}")
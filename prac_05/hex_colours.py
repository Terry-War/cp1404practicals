"""CP1404 Practical 5 - Hex Colours"""

COLOUR_CODES = {"aliceblue": "#f0f8ff",
                "antiquewhite": "#faebd7",
                "aqua": "#00ffff",
                "aquamarine": "#7fffd4",
                "azure": "#f0ffff",
                "beige": "#f5f5dc",
                "bisque": "#ffe4c4",
                "black": "#000000",
                "blue": "#0000ff",
                "coral": "#ff7f50"}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    try:
        print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    except KeyError:
        print("Invalid short state")
    colour_name = input("Enter a colour name: ").lower()

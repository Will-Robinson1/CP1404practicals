"""
CP1404/CP5632 Practical
Colours in a dictionary
"""


CODE_TO_COLOUR = {"#0048ba": "Absolute Zero", "#b0bf1a": "Acid Green", "#f0f8ff": "AliceBlue",
                  "#e32636": "Alizarin crimson", "#e52b50": "Amaranth", "#ffbf00": "Amber", "#9966cc": "Amethyst",
                  "#faebd7": "AntiqueWhite", "#ffefdb": "AntiqueWhite1", "#eedfcc": "AntiqueWhite2"}
print(CODE_TO_COLOUR)

def main():
    colour_code = input("Enter colour code: ")
    while colour_code != "":
        if colour_code in CODE_TO_COLOUR:
            print(colour_code, "is", CODE_TO_COLOUR[colour_code])
        else:
            print("Invalid colour code")
        colour_code = input("Enter colour code: ")

main()
"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""
MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""

def main():

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = fahrenheit_calculations(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = celsius_calculations(celsius, fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_calculations(celsius: float, fahrenheit: float) -> float:
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def fahrenheit_calculations(celsius: float) -> float:
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
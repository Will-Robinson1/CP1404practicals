"""
CP1404 Practical 06 - Guitars program
Estimate: 30 minutes
Start time: 6pm
Actual: 33 minutes
"""

from guitar import Guitar

def main():
    print("My guitars!")

    guitars: list[Guitar] = []

    # For faster testing, comment these input lines and uncomment the sample data below.
    name = input("Name: ").strip()
    while name:
        year = _read_int("Year: ")
        cost = _read_float("Cost: $")
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ").strip()

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

def _read_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input; enter a valid integer.")

def _read_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input; enter a valid number.")

if __name__ == "__main__":
    main()
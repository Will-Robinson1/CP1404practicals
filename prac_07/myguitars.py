"""
CP1404/CP5632 Practical
Read and write Guitar objects from/to a CSV file.
Demonstrates file handling, sorting, and object use.
"""

from guitar import Guitar


def main():
    """Read guitars from file, allow adding new ones, then save updated list."""
    filename = "guitars.csv"

    # Load existing guitars from file
    guitars = load_guitars(filename)
    print("These are the guitars in the file:")
    display_guitars(guitars)

    # Allow user to add new guitars
    add_new_guitars(guitars)

    # Sort and display all guitars
    guitars.sort()
    print("\nGuitars sorted by year (oldest to newest):")
    display_guitars(guitars)

    # Save updated list back to file
    save_guitars(filename, guitars)
    print(f"\nAll guitars have been saved to {filename}")


def load_guitars(filename):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue  # Skip malformed lines
            name = parts[0].strip()
            year = int(parts[1].strip())
            cost = float(parts[2].strip())
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    """Display a list of guitars nicely formatted."""
    for i, guitar in enumerate(guitars, 1):
        print(f"{i}. {guitar}")


def add_new_guitars(guitars):
    """Prompt the user to enter new guitars until they leave the name blank."""
    print("\nAdd new guitars:")
    name = input("Name: ").strip()
    while name != "":
        year = get_valid_int("Year: ")
        cost = get_valid_float("Cost: $")
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.")
        name = input("Name: ").strip()


def save_guitars(filename, guitars):
    """Write all guitars to a CSV file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def get_valid_int(prompt):
    """Get a valid integer from user input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input; enter a valid number.")


def get_valid_float(prompt):
    """Get a valid floating-point number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input; enter a valid number.")


if __name__ == "__main__":
    main()

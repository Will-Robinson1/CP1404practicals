"""
CP1404/CP5632 Practical
File reading, object creation, and sorting demonstration using Guitar class.
"""

from guitar import Guitar


def main():
    """Read guitars from file, display them, sort them, and display sorted list."""
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    print("These are the guitars in the file:")
    display_guitars(guitars)

    # Sort guitars by year (thanks to __lt__)
    guitars.sort()

    print("\nGuitars sorted by year (oldest to newest):")
    display_guitars(guitars)


def load_guitars(filename):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r', encoding='utf-8') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0].strip()
            year = int(parts[1].strip())
            cost = float(parts[2].strip())
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    """Display a list of guitars nicely formatted."""
    for guitar in guitars:
        print(guitar)


if __name__ == '__main__':
    main()
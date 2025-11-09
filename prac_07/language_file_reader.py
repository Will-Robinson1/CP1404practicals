"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class.
Updated to include Pointer Arithmetic field.
"""

import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []

    # Open the file for reading
    with open('languages.csv', 'r', newline='') as in_file:
        # File format is: Name,Typing,Reflection,Year,PointerArithmetic
        in_file.readline()  # Skip the header line

        for line in in_file:
            parts = line.strip().split(',')
            # Expecting: name, typing, reflection, year, pointer_arithmetic
            name = parts[0].strip()
            typing = parts[1].strip()
            reflection = parts[2].strip().lower() in ["yes", "true"]
            year = int(parts[3].strip())
            pointer_arithmetic = parts[4].strip().lower() in ["yes", "true"]

            # Construct a ProgrammingLanguage object
            language = ProgrammingLanguage(name, typing, reflection, year, pointer_arithmetic)
            languages.append(language)

    # Display all languages using __str__ method
    print("All Programming Languages:")
    for language in languages:
        print(language)

    # Display only those with pointer arithmetic
    print("\nLanguages supporting pointer arithmetic:")
    for language in languages:
        if language.pointer_arithmetic:
            print(language.name)


def using_csv():
    """Language file reader version using the csv module."""
    with open('languages.csv', 'r', newline='') as in_file:
        in_file.readline()  # Skip header
        reader = csv.reader(in_file)
        for row in reader:
            print(row)


def using_namedtuple():
    """Language file reader version using a named tuple."""
    with open('languages.csv', 'r', newline='') as in_file:
        file_field_names = in_file.readline().strip().split(',')
        print(file_field_names)

        # Extend namedtuple to include the new field
        Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
        reader = csv.reader(in_file)

        for row in reader:
            language = Language._make(row)
            print(repr(language))


def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
    with open('languages.csv', 'r', newline='') as in_file:
        in_file.readline()
        for language in map(Language._make, csv.reader(in_file)):
            print(f"{language.name} was released in {language.year} "
                  f"(Pointer arithmetic: {language.pointer_arithmetic})")


if __name__ == '__main__':
    main()

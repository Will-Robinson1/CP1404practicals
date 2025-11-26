"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_phrase_as_sentence(phrase):
    """
    Format a phrase so that it starts with a capital letter and ends with a single full stop.

    >>> format_phrase_as_sentence("hello")
    'Hello.'
    >>> format_phrase_as_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_phrase_as_sentence("python is fun")
    'Python is fun.'
    """
    phrase = phrase.strip()

    # Capitalise first letter
    phrase = phrase[0].upper() + phrase[1:]

    # Ensure exactly one final full stop
    if not phrase.endswith("."):
        phrase += "."

    return phrase


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message
    assert repeat_string("Python", 1) == "Python"

    # should now pass: "hi hi"
    assert repeat_string("hi", 2) == "hi hi"

    # Car init tests
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # Test Car sets fuel correctly (default)
    assert car.fuel == 0, "Default fuel not set correctly"

    # Test Car sets fuel when provided
    car = Car(fuel=10)
    assert car.fuel == 10, "Fuel not set correctly when fuel=10"


run_tests()

# Uncomment to run doctests
# doctest.testmod()

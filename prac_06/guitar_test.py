"""
CP1404 Practical 06 - Guitar tests
Estimate: 30 minutes
Start time: 6pm
Actual: 33 minutes
"""

from guitar import Guitar

def main():
    test_year = 2022  # Use the year from the prac spec for expected values
    l5 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 0)

    print(f"{l5.name} get_age() - Expected 100. Got {l5.get_age(test_year)}")
    print(f"{another.name} get_age() - Expected 9. Got {another.get_age(test_year)}")
    print(f"{l5.name} is_vintage() - Expected True. Got {l5.is_vintage(test_year)}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage(test_year)}")

if __name__ == "__main__":
    main()
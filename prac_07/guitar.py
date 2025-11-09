"""
CP1404 Practical 06 - Guitar class
Estimate: 30 minutes
Start time: 6pm
Actual: 33 minutes
"""

from datetime import date

class Guitar:
    """Represent a Guitar with name, manufacturing year, and cost."""

    def __init__(self, name= "", year= 0, cost= 0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        # Required: Gibson L-5 CES (1922) : $16,035.40
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __repr__(self):
        """Return a developer-friendly string representation."""
        return f"Guitar({self.name!r}, {self.year}, {self.cost})"

    def __lt__(self, other):
        """Compare guitars by year for sorting (oldest to newest)."""
        return self.year < other.year

    def get_age(self, current_year: int | None = None):
        """Return how old the guitar is in years."""
        if current_year is None:
            current_year = date.today().year
        return max(0, current_year - self.year)

    def is_vintage(self, current_year: int | None = None):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age(current_year=current_year) >= 50
"""
Milestone 1 – Basic Project class
Estimated time: ~20 minutes
"""

from datetime import date


class Project:
    """Represent a project with essential details."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a user-friendly string."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion_percentage}%")
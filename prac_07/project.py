"""
CP1404/CP5632 Practical
Project class to represent details of a project.
Estimated time: ~1 hours
Actual time:    45 minutes
"""

from datetime import date


class Project:
    """Represent a project with details."""

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

    def is_complete(self):
        """Return True if project is complete."""
        return self.completion_percentage >= 100
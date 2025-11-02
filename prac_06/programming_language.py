"""
CP1404 Practical 06 - ProgrammingLanguage class
Estimate: 30 minutes
Start time: 10am
Actual: 40 minutes
"""

class ProgrammingLanguage:
    """Represent a programming language with typing, reflection support, and first-appearance year."""

    def __init__(self, name: str, typing: str, reflection: bool, year: int):
        self.name = name
        self.typing = typing  # "Static" or "Dynamic"
        self.reflection = reflection  # True/False
        self.year = year

    def is_dynamic(self) -> bool:
        """Return True if the language uses dynamic typing."""
        return self.typing.strip().lower() == "dynamic"

    def __str__(self) -> str:
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
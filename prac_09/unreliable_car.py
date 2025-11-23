"""
CP1404/CP5632 Practical
Car class
"""
from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Car that sometimes does not drive."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive; only drive if random < reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
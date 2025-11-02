"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car
from prac_06.car import Limo


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(name="My Car", fuel=180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car(name="Limo", fuel=100)
    limo.add_fuel(20)
    print(f"Limo has fuel: {limo.fuel}")
    limo.drive(115)
    print(f"Limo has fuel: {limo.fuel}")

    print(my_car)
    print(limo)

main()
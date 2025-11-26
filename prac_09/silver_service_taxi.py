from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi with fanciness multiplier and flagfall."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        fare = super().get_fare() + self.flagfall
        return fare

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
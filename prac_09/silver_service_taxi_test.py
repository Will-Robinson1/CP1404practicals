from silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Test Taxi", 100, 2)
    taxi.drive(18)
    fare = taxi.get_fare()
    print(f"Fare should be $48.78 (before rounding). Actual: ${fare:.2f}")
    assert round(fare, 2) == 48.8 or round(fare, 2) == 48.78, "Fare calculation incorrect"


if __name__ == "__main__":
    main()
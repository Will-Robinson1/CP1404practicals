from unreliable_car import UnreliableCar

def main():
    car = UnreliableCar("Unreliable", 100, 30)

    did_drive = 0
    attempts = 100

    for _ in range(attempts):
        distance = car.drive(1)
        if distance > 0:
            did_drive += 1

    print(f"Drove {did_drive} times out of {attempts} attempts (should be ~30%)")


if __name__ == "__main__":
    main()
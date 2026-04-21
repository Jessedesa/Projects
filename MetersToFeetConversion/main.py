def converter():
    print("--- Meters to Feet Converter ---")

    feet_per_meter = 3.28084

    try:
        meters = float(input("Enter distance in meters: "))

        feet = meters * feet_per_meter

        print(f"{meters} meters is approximately {feet:.2f} feet.")

    except ValueError:
        print("Invalid input! Please enter a number.")


converter()
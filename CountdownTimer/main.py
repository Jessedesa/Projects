import time


def countdown_timer():
    print("Python Countdown App")

    try:
        seconds = int(input("Enter time in seconds: "))

        print("\nStarting countdown...")

        while seconds > 0:
            print(f"Time remaining: {seconds} seconds", end="\r")

            time.sleep(1)

            seconds -= 1

        print("\n\nTIME'S UP!")
        print("BEEP BEEP BEEP!")

    except ValueError:
        print("Invalid input! Please enter a whole number.")

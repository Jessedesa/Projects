import random


def roll_dice():
    print("--- Dice Roller ---")

    while True:
        input("Press Enter to roll the die (or type 'q' to quit): ").lower()

        result = random.randint(1, 6)

        print(f"🎲 You rolled a: {result}")
        print("-" * 20)

roll_dice()
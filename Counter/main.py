def counter():
    count = 0
    print("--- Python Counter ---")
    print("Controls: '+' to increase, '-' to decrease, 'q' to quit.")

    while True:
        print(f"\n[ Current Count: {count} ]")
        action = input("Action (+ / - / q): ").lower()

        if action == '+':
            count += 1
        elif action == '-':
            count -= 1
        elif action == 'q':
            print("Final count was:", count)
            print("Goodbye!")
            break
        else:
            print("Invalid input. Use +, -, or q.")


counter()
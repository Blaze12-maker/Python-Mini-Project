from game_logic import *

while True:
    print("\n--- GAME MENU ---")
    print("1. Play Game")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        user = input("Enter stone/paper/scissors: ").lower()

        if user not in ["stone", "paper", "scissors"]:
            print("Invalid input")
            continue

        comp = get_computer_choice()

        print("Computer chose:", comp)

        result = check_winner(user, comp)
        print("Result:", result)

    elif choice == "2":
        print("Exiting game...")
        break

    else:
        print("Invalid choice")
from library import *

while True:
    print("\n--- LIBRARY MENU ---")
    print("1. Show Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_books()

    elif choice == "2":
        issue_book()

    elif choice == "3":
        return_book()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
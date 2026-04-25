books = {
    "python": True,
    "java": True,
    "c++": True
}

issued_books = {}

def show_books():
    print("\nAvailable Books:")
    for book in books:
        status = "Available" if books[book] else "Issued"
        print(f"{book} - {status}")

def issue_book():
    book = input("Enter book name: ").lower()

    if book in books and books[book]:
        student = input("Enter student name: ")
        days = int(input("Enter number of days: "))

        books[book] = False
        issued_books[book] = {
            "student": student,
            "days": days
        }

        print("Book issued successfully")

    else:
        print("Book not available")

def return_book():
    book = input("Enter book name: ").lower()

    if book in issued_books:
        actual_days = int(input("Enter days used: "))
        allowed_days = issued_books[book]["days"]

        fine = 0

        if actual_days > allowed_days:
            extra = actual_days - allowed_days

            if extra <= 7:
                fine = extra * 10
            elif extra <= 14:
                fine = extra * 20
            else:
                fine = extra * 60

        print(f"Fine: ₹{fine}")

        books[book] = True
        del issued_books[book]

        print("Book returned successfully")

    else:
        print("Invalid book")
books = {
 101: ["Python Basics", "Guido", 350],
 102: ["Maths Guide", "RD Sharma", 500]
}
n = int(input("Enter number of books: "))
# ---------- Add Books ----------
for i in range(n):
    book_id = int(input("\nEnter Book ID: "))
    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    price = float(input("Enter Price: "))

    books[book_id] = [name, author, price]
# ---------- Menu Loop ----------
while True:
    print("\n----- LIBRARY MENU -----")
    print("1. Display all books")
    print("2. Search book by ID")
    print("3. Exit")
    choice = input("Enter choice: ")
    # Display all
    if choice == "1":
        print("\nBook Records:")
        for b_id, data in books.items():
            print(b_id, "->", data)
    # Search
    elif choice == "2":
        search_id = int(input("Enter Book ID to search: "))

        if search_id in books:
            print("Book Found:", books[search_id])
        else:
            print("Book not found!")
    # Exit
    elif choice == "3":
        print("Thank you for using Library Tracker!")
        break
    else:
        print("Invalid choice!")
import colorama
from books import Book
from members import Member

# Initialize Colorama
colorama.init(autoreset=True)

# Function to add books into the library
def add_books():
    books = []
    num_books = int(input("Enter the number of books you want to add: "))
    for i in range(num_books):
        title = input(f"Enter the name of book {i + 1}: ")
        author = input(f"Enter the author of '{title}': ")
        copies = int(input(f"Enter number of copies for '{title}': "))
        books.append(Book(title, author, copies))
    return books

# Function to register members
def add_members():
    members = []
    num_members = int(input("Enter the number of members to register: "))
    for _ in range(num_members):
        member_id = int(input("Enter member ID: "))
        name = input("Enter member name: ")
        members.append(Member(member_id, name))
    return members

# To allow members to borrow a book
def borrow_book(member, book):
    return member.borrow(book)

# To allow members to return a book
def return_book(member, book):
    return member.return_book(book)

# Main library management function
def manage_library(books, members):
    while True:
        print("\n1. Borrow a book")
        print("2. Return a book")
        print("3. View borrowed books")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            member_id = int(input("Enter member ID: "))
            book_title = input("Enter book title: ").strip().lower()

            # Find the member and books based on inputs
            member = next((m for m in members if m.member_id == member_id), None)
            book = next((b for b in books if b.title.lower() == book_title), None)

            # Check if both member and book exist
            if member and book:
                print(colorama.Fore.GREEN + borrow_book(member, book))
            else:
                print(colorama.Fore.RED + "Invalid member ID or book title.")

        elif choice == '2':
            member_id = int(input("Enter member ID: "))
            book_title = input("Enter book title: ").strip().lower()

            member = next((m for m in members if m.member_id == member_id), None)
            book = next((b for b in books if b.title.lower() == book_title), None)

            if member and book:
                print(colorama.Fore.GREEN + return_book(member, book))
            else:
                print(colorama.Fore.RED + "Invalid member ID or book title.")

        elif choice == '3':
            member_id = int(input("Enter member ID to view borrowed books: "))
            member = next((m for m in members if m.member_id == member_id), None)

            # Display borrowed book or an appropriate message
            if member:
                if member.borrowed_books:
                    print(colorama.Fore.CYAN + f"{member.name} has borrowed: {', '.join(member.borrowed_books)}")
                else:
                    print(colorama.Fore.YELLOW + f"{member.name} has not borrowed any books.")
            else:
                print(colorama.Fore.RED + "Invalid member ID.")

        elif choice == '4':
            print(colorama.Fore.BLUE + "Exiting the library system.")
            break

        else:
            print(colorama.Fore.RED + "Invalid choice. Please try again.")

# Initialize the library
books = add_books()
members = add_members()
manage_library(books, members)
from books import Book
from members import Member

#function to add books into the library
def add_books():
    books = []
    num_books = int(input("Enter the number of books you want to add: "))
    for _ in range(num_books):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        copies = int(input(f"Enter number of copies for '{title}': "))
        books.append(Book(title, author, copies))
    return books

#function to register members
def add_members():
    members = []
    num_members = int(input("Enter the number of members to register: "))
    for _ in range(num_members):
        member_id = int(input("Enter member ID: "))
        name = input("Enter member name: ")
        members.append(Member(member_id, name))
    return members

#to allow members to borrow a book
def borrow_book(member, book):
    return member.borrow(book)

#to allow members to return a book
def return_book(member, book):
    return member.return_book(book)

#main library management function
def manage_library(books, members):
    while True:
        print("\n1. Borrow a book")
        print("2. Return a book")
        print("3. View borrowed books")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            member_id = int(input("Enter member ID: "))
            book_title = input("Enter book title: ").strip() .lower()

            #find the member and books based on inputs
            member = next((m for m in members if m.member_id == member_id), None)
            book = next((b for b in books if b.title == book_title), None)

            #check if both member and book exists
            if member and book:
                print(borrow_book(member, book))
            else:
                print("Invalid member ID or book title.")

        elif choice == '2':
            member_id = int(input("Enter member ID: "))
            book_title = input("Enter book title: ").strip() .lower()

            member = next((m for m in members if m.member_id == member_id), None)
            book = next((b for b in books if b.title == book_title), None)

            if member and book:
                print(return_book(member, book))
            else:
                print("Invalid member ID or book title.")

        elif choice == '3':
            member_id = int(input("Enter member ID to view borrowed books: "))
            member = next((m for m in members if m.member_id == member_id), None)

            #display borrowed book or an appropriate message
            if member:
                if member.borrowed_books:
                    print(f"{member.name} has borrowed: {', '.join(member.borrowed_books)}")
                else:
                    print(f"{member.name} has not borrowed any books.")
            else:
                print("Invalid member ID.")

        elif choice == '4':
            print("Exiting the library system.")
            break

        else:
            print("Invalid choice. Please try again.")

#initialize the library system
books = add_books()
members = add_members()
manage_library(books, members)

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow(self, book):
        if book.borrow_book():
            self.borrowed_books.append(book.title)
            return f"{self.name} has borrowed {book.title}."
        else:
            return f"{book.title} is currently unavailable."

    def return_book(self, book):
        if book.title in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.title)
            return f"{self.name} has returned {book.title}."
        else:
            return f"{self.name} doesn't have {book.title}."

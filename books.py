class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def check_availability(self):
        return self.copies > 0

    def borrow_book(self):
        if self.check_availability():
            self.copies -= 1
            return True
        return False

    def return_book(self):
        self.copies += 1

class Book:
    #constructor to initialize a book object
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
    
    #method to check if the book is available
    def check_availability(self):
        return self.copies > 0
    
    #method to borrow a book if available
    def borrow_book(self):
        if self.check_availability():
            self.copies -= 1
            return True
        return False
    
    #method to return a book
    def return_book(self):
        self.copies += 1
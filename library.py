import json
import os
from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.load_data()

    def add_book(self, book):
        self.books[book.book_id] = book
        self.save_data()

    def register_member(self, member):
        self.members[member.member_id] = member
        self.save_data()

    def borrow_book(self, member_id, book_id):
        if book_id in self.books and member_id in self.members:
            book = self.books[book_id]
            member = self.members[member_id]
            if book.available:
                book.available = False
                member.borrow_book(book_id)
                self.save_data()
                return f"Book '{book.title}' borrowed by {member.name}."
            else:
                return "Book is currently not available."
        return "Invalid book ID or member ID."

    def return_book(self, member_id, book_id):
        if book_id in self.books and member_id in self.members:
            book = self.books[book_id]
            member = self.members[member_id]
            if book_id in member.borrowed_books:
                book.available = True
                member.return_book(book_id)
                self.save_data()
                return f"Book '{book.title}' returned by {member.name}."
            else:
                return "This member did not borrow this book."
        return "Invalid book ID or member ID."

    def show_books(self):
        return list(self.books.values())

    def save_data(self):
        with open("books.json", "w") as f:
            json.dump([vars(book) for book in self.books.values()], f, indent=4)
        with open("members.json", "w") as f:
            json.dump([vars(member) for member in self.members.values()], f, indent=4)

    def load_data(self):
        if os.path.exists("books.json"):
            with open("books.json") as f:
                books_list = json.load(f)
                for b in books_list:
                    book = Book(b["book_id"], b["title"], b["author"])
                    book.available = b["available"]
                    self.books[book.book_id] = book

        if os.path.exists("members.json"):
            with open("members.json") as f:
                members_list = json.load(f)
                for m in members_list:
                    member = Member(m["member_id"], m["name"])
                    member.borrowed_books = m["borrowed_books"]
                    self.members[member.member_id] = member

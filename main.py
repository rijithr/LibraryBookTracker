from library import Library
from book import Book
from member import Member

lib = Library()

def menu():
    print("\n===== LIBRARY BOOK TRACKER =====")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Show All Books")
    print("6. Exit")

def run():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            book = Book(book_id, title, author)
            lib.add_book(book)
            print("✅ Book added.")

        elif choice == "2":
            member_id = input("Enter Member ID: ")
            name = input("Enter Name: ")
            member = Member(member_id, name)
            lib.register_member(member)
            print("✅ Member registered.")

        elif choice == "3":
            member_id = input("Enter Member ID: ")
            book_id = input("Enter Book ID: ")
            result = lib.borrow_book(member_id, book_id)
            print(result)

        elif choice == "4":
            member_id = input("Enter Member ID: ")
            book_id = input("Enter Book ID: ")
            result = lib.return_book(member_id, book_id)
            print(result)

        elif choice == "5":
            print("\n📚 All Books:")
            for book in lib.show_books():
                status = "Available" if book.available else "Borrowed"
                print(f"{book.book_id}: {book.title} by {book.author} - {status}")

        elif choice == "6":
            print("👋 Exiting. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    run()

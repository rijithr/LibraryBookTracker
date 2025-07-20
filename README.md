# 📚 Library Book Tracker

This is a simple **Python OOP project** to manage a library system, built as part of a Python with OOP course.

## ✅ Features

- Add books to the library
- Register library members
- Borrow and return books
- Track book availability
- Save and load data using JSON

## 📁 Project Structure

```
LibraryBookTracker/
│
├── main.py          # CLI-based interface
├── book.py          # Book class
├── member.py        # Member class
├── library.py       # Library manager (add, borrow, return, save/load)
├── books.json       # Auto-generated, stores book data
├── members.json     # Auto-generated, stores member data
```

## 💻 How to Run

1. Make sure Python 3 is installed.
2. Run the program using:

```bash
python main.py
```

## 💾 Data Persistence

All data is saved in `books.json` and `members.json` so that your library records are not lost when the program ends.

## 📌 Sample Usage

```
===== LIBRARY BOOK TRACKER =====
1. Add Book
2. Register Member
3. Borrow Book
4. Return Book
5. Show All Books
6. Exit
```

## 📜 License

This project was created for educational purposes as part of a Python OOP course.
from details import Book, Member
from database import load_data, save_data

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.load_library()

    def load_library(self):
        data = load_data()

        self.books = [Book.from_dict(b) for b in data["books"]]
        self.members = [Member.from_dict(m) for m in data["members"]]

    def save_library(self):
        data = {
            "books": [b.to_dict() for b in self.books],
            "members": [m.to_dict() for m in self.members]
        }
        save_data(data)

    def add_book(self, b_id, title, author):
        if self.find_book(b_id):
            print("⚠️ Book ID already exists.")
            return

        self.books.append(Book(b_id, title, author))
        self.save_library()
        print("✔️ Book added.")

    def add_member(self, m_id, name):
        if self.find_member(m_id):
            print("⚠️ Member ID already exists.")
            return

        self.members.append(Member(m_id, name))
        self.save_library()
        print("✔️ Member registered.")

    def find_book(self, b_id):
        return next((b for b in self.books if b.book_id == b_id), None)

    def find_member(self, m_id):
        return next((m for m in self.members if m.member_id == m_id), None)

    def borrow_process(self, m_id, b_id):
        member = self.find_member(m_id)
        book = self.find_book(b_id)

        if not member or not book:
            print("⚠️ Invalid ID.")
            return

        if not book.is_available:
            print("⚠️ Book already borrowed.")
            return

        book.mark_borrowed()
        member.borrowed_books.append(b_id)

        self.save_library()
        print("👍 Borrow successful.")

    def return_process(self, m_id, b_id):
        member = self.find_member(m_id)
        book = self.find_book(b_id)

        if member and b_id in member.borrowed_books:
            book.mark_returned()
            member.borrowed_books.remove(b_id)
            self.save_library()
            print("👍 Return successful.")
        else:
            print("⚠️ Error.")
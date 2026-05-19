class Book:
    def __init__(self, book_id, title, author, is_available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = is_available

    def mark_borrowed(self):
        self.is_available = False

    def mark_returned(self):
        self.is_available = True

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "is_available": self.is_available
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["book_id"],
            data["title"],
            data["author"],
            data["is_available"]
        )

    def __str__(self):
        status = "✅ Available" if self.is_available else "❌ Borrowed"
        return f"{self.book_id} | {self.title} | {self.author} | {status}"


class Member:
    def __init__(self, member_id, name, borrowed_books=None):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books or []

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["member_id"],
            data["name"],
            data["borrowed_books"]
        )

    def __str__(self):
        books = ", ".join(self.borrowed_books) if self.borrowed_books else "None"
        return f"{self.member_id} | {self.name} | Borrowed: {books}"
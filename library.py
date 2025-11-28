import json
from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.load_data()
    
    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        print(f"Book '{title}' added successfully!")
        self.save_data()
    
    def register_member(self, name, member_id):
        member = Member(name, member_id)
        self.members.append(member)
        print(f"Member '{name}' registered successfully!")
        self.save_data()
    
    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    
    def lend_book(self, member_id, isbn):
        book = self.find_book(isbn)
        member = self.find_member(member_id)
        
        if book is None:
            print("Book not found!")
            return
        
        if member is None:
            print("Member not found!")
            return
        
        if not book.available:
            print("Book is already borrowed!")
            return
        
        book.borrow()
        member.borrow_book(book)
        print(f"Book '{book.title}' borrowed by {member.name}")
        self.save_data()
    
    def take_return(self, member_id, isbn):
        book = self.find_book(isbn)
        member = self.find_member(member_id)
        
        if book is None:
            print("Book not found!")
            return
        
        if member is None:
            print("Member not found!")
            return
        
        if isbn not in member.borrowed_books:
            print("This member has not borrowed this book!")
            return
        
        book.return_book()
        member.return_book(book)
        print(f"Book '{book.title}' returned by {member.name}")
        self.save_data()
    
    def save_data(self):
        try:
            books_data = [book.to_dict() for book in self.books]
            with open('books.json', 'w') as f:
                json.dump(books_data, f)
            
            members_data = [member.to_dict() for member in self.members]
            with open('members.json', 'w') as f:
                json.dump(members_data, f)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def load_data(self):
        try:
            with open('books.json', 'r') as f:
                books_data = json.load(f)
                self.books = [Book.from_dict(data) for data in books_data]
        except FileNotFoundError:
            print("No previous book data found. Starting fresh.")
        except Exception as e:
            print(f"Error loading books: {e}")
        
        try:
            with open('members.json', 'r') as f:
                members_data = json.load(f)
                self.members = [Member.from_dict(data) for data in members_data]
        except FileNotFoundError:
            print("No previous member data found. Starting fresh.")
        except Exception as e:
            print(f"Error loading members: {e}")
    
    def generate_report(self):
        print("\n" + "="*50)
        print("LIBRARY ANALYTICS REPORT")
        print("="*50)
        
        # Total books
        total_books = len(self.books)
        print(f"Total Books in Library: {total_books}")
        
        # Available books
        available_books = sum(1 for book in self.books if book.available)
        print(f"Available Books: {available_books}")
        
        # Borrowed books
        borrowed_books = total_books - available_books
        print(f"Currently Borrowed Books: {borrowed_books}")
        
        # Total members
        total_members = len(self.members)
        print(f"Total Registered Members: {total_members}")
        
        # Active members (with borrowed books)
        active_members = sum(1 for member in self.members if len(member.borrowed_books) > 0)
        print(f"Active Members (with borrowed books): {active_members}")
        
        # Most borrowed book
        borrow_count = {}
        for member in self.members:
            for isbn in member.borrowed_books:
                borrow_count[isbn] = borrow_count.get(isbn, 0) + 1
        
        if borrow_count:
            most_borrowed_isbn = max(borrow_count, key=borrow_count.get)
            most_borrowed_book = self.find_book(most_borrowed_isbn)
            if most_borrowed_book:
                print(f"Most Borrowed Book: '{most_borrowed_book.title}' by {most_borrowed_book.author}")
        else:
            print("Most Borrowed Book: None (no books borrowed yet)")
        
        print("="*50 + "\n")
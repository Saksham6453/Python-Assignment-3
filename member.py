class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        self.borrowed_books.append(book.isbn)
    
    def return_book(self, book):
        if book.isbn in self.borrowed_books:
            self.borrowed_books.remove(book.isbn)
    
    def list_books(self):
        if len(self.borrowed_books) == 0:
            print("No books borrowed.")
        else:
            print(f"Books borrowed by {self.name}:")
            for isbn in self.borrowed_books:
                print(f"  - ISBN: {isbn}")
    
    def to_dict(self):
        return {
            'name': self.name,
            'member_id': self.member_id,
            'borrowed_books': self.borrowed_books
        }
    
    @staticmethod
    def from_dict(data):
        member = Member(data['name'], data['member_id'])
        member.borrowed_books = data['borrowed_books']
        return member
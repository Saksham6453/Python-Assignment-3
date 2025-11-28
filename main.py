# Name- Saksham Sharma
# Date- 24/11/2025
# Project Title:  Python Object-Oriented Library Inventory System

from library import Library

def display_menu():
    print("\n" + "="*50)
    print("LIBRARY MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Library Report")
    print("6. Exit")
    print("="*50)

def main():
    # Welcome message
    print("\n" + "*"*50)
    print("WELCOME TO THE LIBRARY MANAGEMENT SYSTEM")
    print("*"*50)
    print("Manage your books and members efficiently!")
    print("*"*50 + "\n")
    
    # Create library instance
    library = Library()
    
    # Main menu loop
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            # Add Book
            print("\n--- Add New Book ---")
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            library.add_book(title, author, isbn)
        
        elif choice == '2':
            # Register Member
            print("\n--- Register New Member ---")
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            library.register_member(name, member_id)
        
        elif choice == '3':
            # Borrow Book
            print("\n--- Borrow Book ---")
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN: ")
            library.lend_book(member_id, isbn)
        
        elif choice == '4':
            # Return Book
            print("\n--- Return Book ---")
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN: ")
            library.take_return(member_id, isbn)
        
        elif choice == '5':
            # View Report
            library.generate_report()
        
        elif choice == '6':
            # Exit
            print("\nThank you for using the Library Management System!")
            print("Goodbye!\n")
            break
        
        else:
            print("\nInvalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
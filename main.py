from functions import Library
def main():
    my_library = Library()
    
    # Adding some dummy data for a quick start
    my_library.add_book("101", "The Forty Rules of Love", "Elif Shafak")
    my_library.add_book("102", "Peer-e-Kamil", "Umera Ahmad")
    my_library.add_member("M1", "Ahmed Ali")

    while True:
        print("\n📚 SCHOOL LIBRARY SYSTEM - LAHORE")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Show All Books")
        print("6. Show Member Details")
        print("7. Exit")
        
        choice = input("\nSelect an option (1-7): ")

        if choice == "1":
            bid = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            my_library.add_book(bid, title, author)

        elif choice == "2":
            mid = input("Enter Member ID: ")
            name = input("Enter Member Name: ")
            my_library.add_member(mid, name)

        elif choice == "3":
            mid = input("Enter Member ID: ")
            bid = input("Enter Book ID: ")
            my_library.borrow_process(mid, bid)

        elif choice == "4":
            mid = input("Enter Member ID: ")
            bid = input("Enter Book ID: ")
            my_library.return_process(mid, bid)

        elif choice == "5":
            my_library.display_status()

        elif choice == "6":
            mid = input("Enter Member ID: ")
            m = my_library.find_member(mid)
            print(m if m else "⚠️ Member not found.")

        elif choice == "7":
            print(" Closing system...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
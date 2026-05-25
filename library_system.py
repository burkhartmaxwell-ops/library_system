class LibraryItem: 

    # represents library items

    def __init__(self, title, item_id):
        self._title = title
        self._item_id = item_id 
        self._is_checked_out = False 
        self._checked_out_by = None 

    def get_title(self):
        # returns title 
        return self._title 
    
    def get_item_id(self):
        
        return self._item_id
    
    def is_available(self):
        # returns true if item is available
        return not self._is_checked_out
    
    def check_out(self, patron_name):
        if not self._is_checked_out:
            self._is_checked_out = True
            self._checked_out_by = patron_name
            return True
        return False
    
    def return_item(self):
        # returns the item to the library
        if self._is_checked_out: 
            self._is_checked_out = False
            self._checked_out_by = None 
            return True
        return False
    
    def get_checked_out_by(self):
        return self._checked_out_by
    
    def get_status(self):

        if self._is_checked_out:
            return f"Checked out to {self._checked_out_by}"
        return "Available"
    
    def get_details(self):

        return (
            f"Title: {self.title}\n"
            f"ID: {self._item_id}\n"
            f"Status: {self.get_status()}"
        )
    
class Book(LibraryItem):

    def __init__(self, title, item_id, author, isbn, pages):
        super().__init__(title, item_id)
        self.author = author 
        self.isbn = isbn
        self.pages = pages

    def get_details(self):
        # returns book details
        return (
            f"Title: {self.get_title()}\n"
            f"ID: {self.get_item_id()}\n"
            f"Type: Book\n"
            f"Author: {self.author}\n"
            f"ISBN: {self.isbn}\n"
            f"Pages: {self.pages}\n"
            f"Status: {self.get_status()}"
        )

class DVD(LibraryItem):
    # represents DVD in library

    def __init__(self, title, item_id, director, runtime, rating):
        super().__init__(title, item_id)
        self.director = director
        self.runtime = runtime
        self.rating = rating

    def get_details(self):

        return (
            f"Title: {self.get_title()}\n"
            f"ID: {self.get_item_id()}\n"
            f"Type: DVD\n"
            f"Director: {self.director}\n"
            f"Runtime: {self.runtime} minutes\n"
            f"Rating: {self.rating}\n"
            f"Status: {self.get_status()}"
        )
class Magazine(LibraryItem):
    # represents magazine

    def __init__(self, title, item_id, issue_number, publication_date):
        super().__init__(title, item_id)
        self.issue_number = issue_number
        self.publication_date = publication_date

    def get_details(self):
        return (
            f"Title: {self.get_title()}\n"
            f"ID: {self.get_item_id()}\n"
            f"Type: Magazine\n"
            f"Issue: #{self.issue_number}\n"
            f"Publication Date: {self.publication_date}\n"
            f"Status: {self.get_status()}"
        )
    
class Library:
    # represents library system

    def __init__(self, name):
        self.name = name 
        self.items = []

    def add_item(self, item):
        # adds item
        self.items.append(item)

    def find_item(self, item_id):
        # finds item by id
        for item in self.items:
            if item.get_item_id() == item_id:
                return item
        return None 
    
    def check_out_item(self, item_id, patron_name):
        # checks out item
        item = self.find_item(item_id)

        if item and item.check_out(patron_name):
            print(
                f"Successfully checked out: "
                f"{item.get_title()} to {patron_name}"
            )
        else:
            print(f"Item not available: {item.get_title()}")

    def list_available_items(self):
        # returns list of available items
        available_items = []

        for item in self.items:
            if item.is_available():
                available_items.append(item.get_title)
            
        return available_items
    
    def list_checked_out_items(self):
        # returns list of checked out items
        checked_out_items = []

        for item in self.items: 
            checked_out_items.append(
                (
                    item.get_title(),
                    item.get_checked_out_by()
                )
            )
        return checked_out_items
    
    def display_catalog(self):
        # displays all catalog items
        for item in self.items:
            print(item.get_details())
            print()
    
    def return_item(self, item_id):
        # returns item
        item = self.find_item(item_id)

        if item and item.return_item():
            print(f"Successfully returned: {item.get_title()}")
        else:
            print(f"Item was not checked out: {item.get_title()}")


# main program

print("===================================")
print("LIBRARY MANAGEMENT SYSTEM")
print("===================================")

library = Library("Oakland City University Library")

print("\nLibrary Name:", library.name)

print("\n--- Adding Items to Catalog ---")

book1 = Book(
    "1984",
    "BOOK001",
    "George Orwell",
    "978-0451524935",
    328
)

book2 = Book(
    "To Kill a Mockingbird",
    "BOOK002",
    "Harper Lee",
    "978-0060935467",
    336
)

dvd1 = DVD(
    "The Matrix",
    "DVD001",
    "The Wachowskis",
    136,
    "R"
)

dvd2 = DVD(
    "Inception",
    "DVD002",
    "Christopher Nolan",
    148,
    "PG-13"
)

mag1 = Magazine(
    "National Geographic",
    "MAG001",
    245,
    "January 2026"
)

mag2 = Magazine(
    "Time Magazine",
    "MAG002",
    12,
    "December 2025"
)

items = [book1, book2, dvd1, dvd2, mag1, mag2]

for item in items:
    library.add_item(item)
    print(f"Added: {item.get_title()} ({item.get_item_id()})")

print("\n--- Checking Out Items ---")

library.check_out_item("BOOK001", "Alice Smith")
library.check_out_item("DVD001", "Bob Johnson")
library.check_out_item("MAG001", "Alice Smith")
library.check_out_item("BOOK001", "Charlie Brown")

print("\n--- Returning Items ---")

library.return_item("BOOK001")
library.return_item("BOOK002")

print("\n--- Complete Catalog ---")
library.display_catalog()

available_items = library.list_available_items()

print(f"--- Available Items ({len(available_items)}) ---")

checked_out_items = library.list_checked_out_items()

print(f"\n--- Checked Out Items ({len(checked_out_items)}) ---")

for index, item in enumerate(checked_out_items, start=1):
    print(f"  {index}. {item[0]} (by {item[1]})")

print("\n===================================")
print("END OF REPORT")
print("===================================")

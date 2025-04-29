class Person:
    """Create a Person class"""
    def __init__(self, first_name : str, last_name : str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        """String representation of the person"""
        return f"{self.first_name} {self.last_name}"


class Book:
    """Create a Book class"""
    def __init__(self, title : str, author : Person):
        self.title = title
        self.author = author

    def __str__(self) -> str:
        """String representation of the book"""
        return f"{self.title} ({self.author})"


class LibraryError(Exception):
    """Base class for Library errors"""


class Library:
    """""Create a Library class"""
    def __init__(self, name : str) -> None:
        self.name = name
        self._books = []
        self._members = set()
        self._borrowed_books = {}

    def is_book_available(self, book : Book) -> bool:
        """Check if book is ready to borrow"""
        if(book in self._books): 
            print(f"{book} is ready to borrow")
            return True
        else : 
            raise LibraryError("Book not available")

    def borrow_book(self, book: Book, person: Person) :
        """Borrow a book"""
        if(book in self._books and person in self._members):
            if(book not in self._borrowed_books):
                self._borrowed_books[book] = person
                print(f"{person} borrowed {book}")
        elif(book not in self._books):
            raise LibraryError(f"{book} is not available")
        elif(person not in self._members):
            raise LibraryError(f"{person} is not a member of the library")
        return None
    
    def return_book(self, book : Book):
        """"Return a borrowed book"""
        if(book in self._borrowed_books):
            del self._borrowed_books[book]
            print(f"{book} returned")
        else:
            print(f"{book} is not borrowed")
        return None
    
    def add_new_member(self, person : Person):
        """"Add a new member to the library"""
        if(person not in self._members):
            self._members.add(person)
            print(f"{person} added as a member")
        else:
            print(f"{person} already a member")
        return None
    
    def add_new_book(self, book : Book):
        """Add a new book to the library"""
        if(book not in self._books):
            self._books.append(book)
            print(f"{book} added to the library")
        else:
            print("Book already in the library")
        return None
    
    def print_status(self):
        """Print the status of the library"""
        available_books = [book for book in self._books if book not in self._borrowed_books]#check if book is available to borrow
        print("Library Status:")
        print("Books catalogue :")#Print all books in the library
        for book in self._books:
            print(f"  - {book}")
        print("Members:") #Print all members of the library
        for member in self._members:
            print(f"  - {member}")
        print("Available Books:") #Print all available books to borrow
        for book in available_books:
            print(f"  - {book}")
        print("Borrowed Books:") #Print all borrowed books
        for book, person in self._borrowed_books.items():
            print(f"  - {book} borrowed by {person}")
        print("-----")
            

def main():
    """Test your code here"""
    antoine = Person("Antoine", "Dupont")
    print(antoine)

    julia = Person("Julia", "Roberts")
    print(julia)

    rugby_book = Book("Jouer au rugby pour les nuls", Person("Louis", "BB"))
    print(rugby_book)

    novel_book = Book("Vingt mille lieues sous les mers", Person("Jules", "Verne"))
    print(novel_book)

    library = Library("Public library")
    library.print_status()

    library.add_new_book(rugby_book)
    library.add_new_book(novel_book)
    library.add_new_member(antoine)
    library.add_new_member(julia)
    library.print_status()

    print(f"Is {rugby_book} available? {library.is_book_available(rugby_book)}")
    library.borrow_book(rugby_book, antoine)
    library.print_status()

    try:
        library.borrow_book(rugby_book, julia)
    except LibraryError as error:
        print(error)

    try:
        library.borrow_book(Book("Roméo et Juliette", Person("William", "Shakespeare")), julia)
    except LibraryError as error:
        print(error)

    try:
        library.borrow_book(novel_book, Person("Simone", "Veil"))
    except LibraryError as error:
        print(error)

    try:
        library.return_book(novel_book)
    except LibraryError as error:
        print(error)

    library.return_book(rugby_book)
    library.borrow_book(novel_book, julia)
    library.print_status()

    library.borrow_book(rugby_book, julia)
    library.print_status()

if __name__ == "__main__":
    main()

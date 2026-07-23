"""class -> a blue print 
which contains 
- properties (variables)
- actions (functions that are defined inside a class)
- if a function is defined inside a class it is called as method.

class (blue print) -> constructor -> object (real world instance)

1. variable that belong to object (instance variables)
- a object variable is different for all the different instance 
ex: author of a book
- this are defined inside constructor
2. variables that belong to class 
- will be same for all the classess , there will be only one variable 
all the objects have shared access to the varaible 
- outside the constructor
ex: vechile type

1. Getters -> methods that return us the values of a variable 
2. Setters -> methods that sets the values of the variables 
3. Actions -> They perform certain tasks like displaying data, calculating something

Access Modifiers: 
they control the access of the varaible 
1. Public -> will allow the access from anywhere just by using the object reference 
ex: rating,bid 
2. Private -> will only allow within the class access , you cannot access outside from a class 
ex: __name 
3. protectes -> it is somewhat similar to private. but it allows child classess to access the 
properties. 
ex: _name 
You can have access to your parents information: 
protected: 
- habits 
- how they behave when they are angry 
public: 
- work 
- details 
private: 
- bank passwords ? you dont have access to it 
- secrets 
"""
from tabulate import tabulate 
from datetime import datetime, date

class User:
    count = 9999
    def __init__(self):
        User.count += 1
        self.__uid = User.count
        self.__username = ""
        self.__name = ""
        self.__age = 0
        self.__joining_date = datetime.now().strftime("%d/%m/%Y")
        self.__password = ""

    def set_username(self, username):
        self.__username = username

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_password(self, password):
        self.__password = password

    def get_id(self):
        return self.__uid

    def get_username(self):
        return self.__username

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_joining_date(self):
        return self.__joining_date
        
    def login(self, password):
        if password == self.__password:
            return True
        else:
            return False

    def display(self):
        columns = [
            "User ID",
            "Username",
            "Name",
            "Age",
            "Joining Date"
        ]

        row = [
            self.get_id(),
            self.get_username(),
            self.get_name(),
            self.get_age(),
            self.get_joining_date()
        ]

        table = tabulate([row], headers=columns, tablefmt="grid")
        print(table)
        
class Book: 
    count = 0
    def __init__(self):
        Book.count += 1
        self.__title = ""
        self.__is_available = True 
        self.__category = "" 
        self.__description = "" 
        self.__bid = Book.count
        self.__author = "" 
        self.__borrowed_by = None
        self.__date_of_borrowing = ""
        self.__return_date = ""

    def set_title(self,title):
        self.__title = title 
    
    def set_description(self,description):
        self.__description = description
    
    def set_category(self,category):
        self.__category = category 
        
    def set_author(self,author):
        self.__author = author 
        
    def set_status(self,status):
        self.__is_available = status
        
    def get_title(self):
        return self.__title 
    
    def get_description(self):
        return self.__description
    
    def get_author(self):
        return self.__author 
    
    def get_status(self):
        return self.__is_available
        
    def get_category(self):
        return self.__category
        
    def get_id(self):
        return self.__bid
    
    def get_borrowed_by(self):
        return self.__borrowed_by

    def get_date_of_borrowing(self):
        return self.__date_of_borrowing

    def get_return_date(self):
        return self.__return_date
        
    def borrow(self, borrowed_by):
        if self.__is_available:
            today = str(date.today())
            year, month, day = map(int, today.split("-"))
            self.__borrowed_by = borrowed_by
            self.__date_of_borrowing = f"{day}/{month}/{year}"
            return_day = day + 14
            return_month = month
            return_year = year
            if return_day > 30:
                return_day = return_day % 30
                return_month += 1
                if return_month > 12:
                    return_month = 1
                    return_year += 1
            self.__return_date = f"{return_day}/{return_month}/{return_year}"
            self.__is_available = False
            print("Book borrowed successfully.")
            return True
        else:
            print("This book is already borrowed.")
            return False

    def return_book(self):
        if self.__is_available:
            print("This book is already available.")
            return False
        else:
            self.__is_available = True
            self.__borrowed_by = None
            self.__date_of_borrowing = ""
            self.__return_date = ""
            print("Book returned successfully.")
            return True

    def display(self):
        if self.get_status():
            status = "Available"
        else:
            status = "Borrowed"
        if self.get_borrowed_by() is None:
            borrowed_by = "-"
        else:
            borrowed_by = self.get_borrowed_by()
        borrowing_date = self.get_date_of_borrowing()
        if borrowing_date == "":
            borrowing_date = "-"
        return_date = self.get_return_date()
        if return_date == "":
            return_date = "-"
        columns = [
            "ID",
            "Title",
            "Description",
            "Category",
            "Author",
            "Status",
            "Borrowed By",
            "Borrowing Date",
            "Return Date"
        ]
        row = [
            self.get_id(),
            self.get_title(),
            self.get_description(),
            self.get_category(),
            self.get_author(),
            status,
            borrowed_by,
            borrowing_date,
            return_date
        ]
        table = tabulate([row], headers=columns, tablefmt="grid")
        print(table)
        
class Library: 
    def __init__(self,name):
        self.name = name 
        self.books = [] 
        self.accounts = []
        self.current_uid = 0 
        
    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")
    
    def checkout(self,bid,uid = None): 
        if uid is None:
            uid = self.current_uid
        if uid == 0:
            print("Please login first.")
            return False
        account = None
        for a in self.accounts:
            if a.get_id() == uid:
                account = a
                break
        if account is None:
            print("User not found.")
            return False
        if self.books == []:
            print("No books found.")
            return False
        book = None
        for b in self.books:
            if b.get_id() == bid:
                book = b
                break
        if book is None:
            print("Book not found.")
            return False
        else:
            return book.borrow(uid)
                
    def checkin(self,bid):
        if self.books == []:
            print("No books found.")
            return False
        book = None
        for b in self.books:
            if b.get_id() == bid:
                book = b
                break
        if book is None:
            print("Book not found.")
            return False
        else:
            return book.return_book()

    def search_by_category(self,category):
        books = []
        for b in self.books:
            if b.get_category().lower() == category.lower():
                books.append(b)
        return books
            
    def search_by_title(self, title):
        books = []
        for b in self.books:
            if b.get_title().lower() == title.lower():
                books.append(b)
        return books

    def search_by_author(self, author):
        books = []
        for b in self.books:
            if b.get_author().lower() == author.lower():
                books.append(b)
        return books
    
    def logIn(self,uid,password):
        account = None 
        if self.accounts == []: 
            print("No accounts found, first create an account")
            return False 
        for a in self.accounts:
            if a.get_id() == uid:
                account = a
                break
        if account is None:
            print("User not found.")
            return False
        else:
            success = account.login(password)
            if success:
                print("Login successful.")
                self.current_uid = account.get_id()
                return True
            else:
                print("Login failed. Password incorrect.")
                return False
                    
    def signUp(self, name, age, password):
        if age < 18:
            print("User should be above 18.")
            return False
        elif password == "":
            print("Password cannot be empty. It should be at least 5 characters.")
            return False
        elif len(password) < 5:
            print("Password should be at least 5 characters.")
            return False
        user = User()
        user.set_name(name)
        user.set_username(name)
        user.set_age(age)
        user.set_password(password)
        self.accounts.append(user)
        print("Account created successfully.")
        print(f"Your User ID is: {user.get_id()}")
        return True

    def display(self,books: list[Book]):
        if books == []:
            print("No books found.")
            return
        rows = []
        for book in books:
            if book.get_status():
                status = "Available"
            else:
                status = "Borrowed"
            if book.get_borrowed_by() is None:
                borrowed_by = "-"
            else:
                borrowed_by = book.get_borrowed_by()
            borrowing_date = book.get_date_of_borrowing()
            if borrowing_date == "":
                borrowing_date = "-"
            return_date = book.get_return_date()
            if return_date == "":
                return_date = "-"
            rows.append([
                book.get_id(),
                book.get_title(),
                book.get_description(),
                book.get_category(),
                book.get_author(),
                status,
                borrowed_by,
                borrowing_date,
                return_date
            ])
        columns = [
            "ID",
            "Title",
            "Description",
            "Category",
            "Author",
            "Status",
            "Borrowed By",
            "Borrowing Date",
            "Return Date"
        ]
        table = tabulate(rows, headers=columns, tablefmt="grid")
        print(table)
        
library = Library("Chandler Library")
application_name = "Library Management Application"
options = """Options:
1. Sign Up
2. Login
3. Add a Book
4. Display All Books
5. Search Book by Title
6. Search Book by Author
7. Search Book by Category
8. Checkout Book
9. Return Book
10. Display Current User
11. Exit
"""
while True:
    print(application_name)
    print(options)
    choice = int(input("Enter your choice (1-11): "))
    print("-" * 20)
    match choice:
        case 1:
            print("Sign Up:")
            name = input("Name: ")
            age = int(input("Age: "))
            password = input("Password: ")
            library.signUp(name, age, password)
        case 2:
            print("Login:")
            uid = int(input("User ID: "))
            password = input("Password: ")
            library.logIn(uid, password)
        case 3:
            print("Adding a Book:")
            book = Book()
            title = input("Title: ")
            description = input("Description: ")
            category = input("Category: ")
            author = input("Author: ")
            book.set_title(title)
            book.set_description(description)
            book.set_category(category)
            book.set_author(author)
            library.add_book(book)
            print(f"Book ID: {book.get_id()}")
        case 4:
            print("Displaying All Books:")
            library.display(library.books)
        case 5:
            print("Search Book by Title:")
            title = input("Title: ")
            books = library.search_by_title(title)
            library.display(books)
        case 6:
            print("Search Book by Author:")
            author = input("Author: ")
            books = library.search_by_author(author)
            library.display(books)
        case 7:
            print("Search Book by Category:")
            category = input("Category: ")
            books = library.search_by_category(category)
            library.display(books)
        case 8:
            print("Checkout Book:")
            bid = int(input("Book ID: "))
            library.checkout(bid)
        case 9:
            print("Return Book:")
            bid = int(input("Book ID: "))
            library.checkin(bid)
        case 10:
            print("Current User:")
            if library.current_uid == 0:
                print("No user is currently logged in.")
            else:
                current_user = None
                for account in library.accounts:
                    if account.get_id() == library.current_uid:
                        current_user = account
                        break
                if current_user is None:
                    print("User not found.")
                else:
                    current_user.display()
        case 11:
            print("Exiting...")
            break
        case _:
            print("Invalid choice. Try again.")
    if choice != 11:
        input("Press Enter to continue...")
        print("-" * 20)

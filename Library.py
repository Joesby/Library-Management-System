class Book():
    def __init__(self, title, author, genre, isbn, pub_date, availability):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.pub_date = pub_date
        self.availability = availability

    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_genre(self):
        return self.genre
    
    def get_isbn(self):
        return self.isbn
    
    def get_pub_date(self):
        return self.pub_date
    
    def get_availability(self):
        return self.availability
    
    def set_title(self, new_title):
        self.title = new_title

    def set_author(self, new_author):
        self.author = new_author
    
    def set_genre(self, new_genre):
        self.genre = new_genre

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn

    def set_pub_date(self, new_pub_date):
        self.pub_date = new_pub_date

    def set_availability(self, new_availability):
        self.availability = new_availability

    def display_book_data(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nISBN: {self.isbn}\nDate Published: {self.pub_date}\nAvailability: {self.availability}\n")
    
class User():
    def __init__(self, name, lib_id):
        self.name = name
        self.lib_id = lib_id
        self.borrowed_books = []

    def get_name(self):
        return self.name
        
    def get_lib_id(self):
        return self.lib_id
        
    def get_borrowed_books(self):
        return self.borrowed_books
        
    def set_name(self, new_name):
        self.name = new_name

    def set_lib_id(self, new_lib_id):
        self.lib_id = new_lib_id

    def borrow_book(self, new_book):
        self.borrowed_books.append(new_book)

    def return_book(self, returned_book):
        self.borrowed_books.remove(returned_book)

# User type that inherits traits from the base User class but doesn't pay for larger borrow cap
class FreeUser(User):
    def __init__(self, name, lib_id):
        super().__init__(name, lib_id)
        self.borrow_cap = 3

    def get_borrow_cap(self):
        return self.borrow_cap
    
    def set_borrow_cap(self, new_cap):
        self.borrow_cap = new_cap

    def display_user_data(self):
        print(f"Name: {self.name}\nLibrary ID: {self.lib_id}\nBook Limit: {self.borrow_cap}")
        print("Borrowed Books:")
        if len(self.borrowed_books) == 0:
            print("None")
        else:
            for i in self.borrowed_books:
                print(f"Title: {i.get_title()}\nAuthor: {i.get_author()}\nGenre: {i.get_genre()}\nISBN: {i.get_isbn()}\nDate Published: {i.get_pub_date()}\n")

# User type that inherits traits from the base User class and pays for a larger borrow cap
class PaidUser(User):
    def __init__(self, name, lib_id):
        super().__init__(name, lib_id)
        self.borrow_cap = 100

    def get_borrow_cap(self):
        return self.borrow_cap

    def display_user_data(self):
        print(f"Name: {self.name}\nLibrary ID: {self.lib_id}\nBook Limit: {self.borrow_cap}")
        print("Borrowed Books:")
        if len(self.borrowed_books) == 0:
            print("None")
        else:
            for i in self.borrowed_books:
                print(f"Title: {i.get_title()}\nAuthor: {i.get_author()}\nGenre: {i.get_genre()}\nISBN: {i.get_isbn()}\nDate Published: {i.get_pub_date()}\n")

class Author():
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def get_name(self):
        return self.name
        
    def get_biography(self):
        return self.biography
        
    def set_name(self, new_name):
        self.name = new_name

    def set_biography(self, new_bio):
        self.biography = new_bio

    def display_author_data(self):
        print(f"Name: {self.name}\nBiography: {self.biography}\n")

class Genre():
    def __init__(self, genre, description, category):
        self.genre = genre
        self.description = description
        self.category = category

    def get_name(self):
        return self.genre
        
    def get_description(self):
        return self.description
        
    def get_category(self):
        return self.category
        
    def set_name(self, new_genre):
        self.genre = new_genre

    def set_description(self, new_descripton):
        self.description = new_descripton
        
    def set_category(self, new_category):
        self.category = new_category

    def display_genre_data(self):
        print(f"Genre: {self.genre}\nCategory: {self.category}\nDescription: {self.description}\n")

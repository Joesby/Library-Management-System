from Library import *    

# create lists to contain each set of objects
list_of_books = []
list_of_users = []
list_of_authors = []
list_of_genres = []

# add books to library's default collection by importing information from a text file
with open('collection.txt', 'r') as file:
    lines_list = file.readlines()

    for i in lines_list:
        i = i.strip()
        book_data = i.split(", ")

        for j in range(len(book_data)):
            book_data[j] = book_data[j].replace("-", " ")

        book = Book(book_data[0], book_data[1], book_data[2], book_data[3], book_data[4], "Available")
        list_of_books.append(book)

print("Welcome to the Library Management System!")
print("")
print("Main Menu:")
print("1. Book Operations")
print("2. User Operations")
print("3. Author Operations")
print("4. Genre Operations")
print("5. Quit")
print("")

user_input = input("Please select one of the numbered options: ")

while user_input != "5":

    # 1st main menu option: Book Options
    if user_input == "1":
        print("Book Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print(f"5. Display all books\n")
        
        option = input("Which option would you like? ")

        # option for adding a new book to the library's collection
        if option == "1":
            title = input("What is the title of the book? ")
            author = input("Who is the author? ")
            genre = input("What is the genre for this book? ")
            isbn = input("What is this books ISBN? ")
            pub_date = input("What date was the book published (mm/dd/yyyy)? ")
            availability = "Available"

            # user the provided input to create a new book object, then store in a list
            book = Book(title, author, genre, isbn, pub_date, availability)
            list_of_books.append(book)

        # option for a user borrowing a book
        elif option == "2":
            search_term = input("Which user will be checking out a book? ")
            user_found = False

            for i in list_of_users:
                if i.get_name().lower() == search_term.lower() or i.get_lib_id() == search_term:                        # search for user by name or id
                    user_found = True
                    selected_user = i                                                                                   # store iterable for future use
                    break
                
            if user_found == False:
                print("I'm sorry, I couldn't find a user with that name in our system.")
            else:
                if len(selected_user.get_borrowed_books()) >= selected_user.get_borrow_cap():                   # check the users borrow limit
                    print(f"I'm sorry, but {selected_user.get_name()} has reached their borrow limit.")
                else:
                    search_term = input(f"Which book would {selected_user.get_name()} like to check out? ")                 # request which book the user would like to check out
                    book_available = False
                    book_found = False

                    for i in list_of_books:                                                                 # loop through books in collection
                        if i.get_title().lower() == search_term.lower() or i.get_isbn() == search_term:     # search book titles by title or isbn
                            book_found = True

                            if i.get_availability() == "Available":     # checks if a book is available
                                book_available = True
                            
                                i.set_availability("Borrowed")          # sets a book to 'borrowed' if it was available
                                book_to_borrow = i                      # stores current iteration for future use
                                break
                    
                    # before a book is checked out, use checks to ensure the book could be found and that it is available
                    if book_found == False:
                        print("I'm sorry, I could not find a book matching that description.")
                    else:
                        if book_available == False:
                            print("I'm sorry, that book is currently unavailable.")
                        else:
                            selected_user.borrow_book(i)
                            print(f"{selected_user.get_name()} successfully borrowed {book_to_borrow.get_title()}!")

        # option for a user returning a book
        elif option == "3":
            search_term = input("Which user will be returning a book? ")
            user_found = False

            # loop through the list of users, searching for the one specified in user input
            for i in list_of_users:
                if i.get_name().lower() == search_term.lower() or i.get_lib_id() == search_term:
                    user_found = True
                    selected_user = i
                    break
                
            # check to see if the user searched exists
            if user_found == False:
                print("I'm sorry, I couldn't find a user with that name in our system.")
            else:
                # when the user is found, request the title or isbn to search the users list of borrowed books to return
                search_term = input(f"Which book would {selected_user.get_name()} like to return? ")
                book_found = False
                users_borrowed_books = selected_user.get_borrowed_books()   # list of users borrowed books

                # loop through the list to find the matching title or isbn
                for i in users_borrowed_books:
                    if i.get_title().lower() == search_term.lower() or i.get_isbn() == search_term:
                        book_found = True
                        book_to_return = i

                if book_found == False:
                    print(f"I'm sorry, but {selected_user.get_name()} doesn't seem to have that book.")     # option for if book is not found in list
                else:
                    # loop through library collection, match the found isbn, and set the availability back to 'available'
                    for i in list_of_books:
                        if book_to_return.get_isbn() == i.get_isbn():
                            i.set_availability("Available")

                    # remove the returned book from the users personal list
                    selected_user.return_book(book_to_return)
                    print(f"{selected_user.get_name()} successfully returned {book_to_return.get_title()}!")

        # option for displaying a specific books details
        elif option == "4":
            # request specific information for the book search
            search_term = input("Which title or ISBN are you looking for? ")
            book_found = False

            # if matching book is found, display the information
            for i in list_of_books:
                if i.get_title().lower() == search_term.lower() or i.get_isbn() == search_term:
                    book_found = True
                    print("Here are the matching books in our collection:")
                    i.display_book_data()
                
            # option for if a matching book isn't found
            if book_found == False:
                print("I'm sorry, I couldn't find a matching book in our collection.")
                

        # option for displaying all books details from the entire library collection
        elif option == "5":
            for i in list_of_books:
                i.display_book_data()

    # 2nd main menu option: User Options
    elif user_input == "2":
        print("User Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print(f"3. Display all users\n")
        
        option = input("Which option would you like? ")
        
        # option for adding a new user
        if option == "1":
            name = input("What is the name of the new patron? ")
            paid_option = input("Would you like the paid option for your library card (Yes/No)? ")
            name = name.strip()                                     # ensure the patron name doesn't include any accidental white space
            lib_id = f"00{len(list_of_users)}"                      # assign a library id

            if paid_option.lower() == "yes":
                user = PaidUser(name, lib_id)       # use the PaidUser class for yes            
                list_of_users.append(user)          # store in a list
            elif paid_option.lower() == "no":
                user = FreeUser(name, lib_id)       # use the FreeUser class for no
                list_of_users.append(user)          # store in a list
            else:
                print("I'm sorry, that was not a valid option.")

        # option for viewing a specific users details
        elif option == "2":
            search_term = input("Which user are you looking for? ")
            user_found = False

            # loop through the users in the system to display their information
            for i in list_of_users:
                if i.get_name().lower() == search_term.lower() or i.get_lib_id() == search_term:
                    user_found = True
                    print("Here are the matching user details:")
                    i.display_user_data()

            # option for if a matching user isn't found
            if user_found == False:
                print("I'm sorry, I couldn't find a matching user in our system.")

        # option for viewing all users details
        elif option == "3":
            for i in list_of_users:
                i.display_user_data()

    # 3rd main menu option: Author Options
    elif user_input == "3":
        # collect information to make an author object
        print("Author Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print(f"3. Display all authors\n")
        
        option = input("Which option would you like? ")

        # option for adding a new author
        if option == "1":
            name = input("What is this authors name? ")
            biography = input(f"Please provide a brief biography for {name}: ")

            # user the provided input to create a new author object, then store in a list
            author = Author(name, biography)
            list_of_authors.append(author)

        # option for viewing a specific authors details
        elif option == "2":
            search_term = input("What is the name of the author you're looking for? ")
            author_found = False

            # loop through authors in the system to display their information
            for i in list_of_authors:
                if i.get_name().lower() == search_term.lower():
                    author_found = True
                    print("Here are the matching author details:")
                    i.display_author_data()

            # option for if a matching author isn't found
            if author_found == False:
                print("I'm sorry, I couldn't find any matching authors in our system.")

        # option for viewing all authors details
        elif option == "3":
            for i in list_of_authors:
                i.display_author_data()

    # 4th main menu option: Genre Options
    elif user_input == "4":
        print("Genre Operations:")
        print("1. Add a new genre")
        print("2. View genre details")
        print(f"3. Display all genres\n")
        
        option = input("Which option would you like? ")

        if option == "1":
            # collect information to create a genre object
            new_genre = input("What is this genre called? ")
            description = input("Please provide a brief description for this genre: ")
            category = input("What category does this genre fall under? ")

            # user the provided input to create a new genre object, then store in a list
            genre = Genre(new_genre, description, category)
            list_of_genres.append(genre)

        elif option == "2":
            search_term = input("Which genre are you looking for? ")
            genre_found = False

            # loop through genres in system to display their information
            for i in list_of_genres:
                if i.get_name().lower() == search_term.lower():
                    genre_found = True
                    i.display_genre_data()
            
            # option for if matching genre isn't found
            if genre_found == False:
                print("I'm sorry, I couldn't find any matching genres in our system.")

        # display all genres in the system
        elif option == "3":
            for i in list_of_genres:
                i.display_genre_data()

    # 5th main menu option: Quit
    elif user_input == "5":
        break

    # give the user feedback so they know they didn't input correctly
    else:
        print(f"That was not a valid selection.\n")

    # reiterate options for clarity and request another input
    print(f"\nMain Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Genre Operations")
    print("5. Quit")
    print("")
    user_input = input("Please select one of the numbered options: ")

# exit message when the user quits
print("Thank you for using the Library Management System!")
print("Good-bye!")
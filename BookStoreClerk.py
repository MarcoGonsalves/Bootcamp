#Capstone Project - Bookstore Clerk

import sqlite3

#Cursor Object
bookDB = sqlite3.connect('bookstoreDB')
cursor = bookDB.cursor()

#Creat books database with id, Title, Author and Quantity
def createBooksTable():
    try:
        cursor.execute('''
        CREATE TABLE books(
        id INTEGER PRIMARY KEY,
        Title TEXT,
        Author TEXT,
        Qty INTEGER)
        ''')
        bookDB.commit
    except: #Exception if table exists
        print('The books table already exists')
      
#Hard coded books into variables
def insertBooks():
    id1 = 3001
    Title1 = 'A Tale of Two Cities'
    Author1 = 'Charles Dickens'
    Qty1 = 30
    id2 = 3002
    Title2 = "Harry Potter and the Philosopher's Stone"
    Author2 = 'J.K. Rowling'
    Qty2 = 40
    id3 = 3003
    Title3 = 'The Lion, the Witch and the Wardrobe'
    Author3 = 'C. S. Lewis'
    Qty3 = 25
    id4 = 3004
    Title4 = 'The Lord of the Rings'
    Author4 = 'J.R.R Tolkien'
    Qty4 = 37
    id5 = 3005
    Title5 = 'Alice in Wonderland'
    Author5 = 'Lewis Carroll'
    Qty5 = 12
    #Create tuple of the books
    bookList = [(id1, Title1, Author1, Qty1), (id2, Title2, Author2, Qty2), (id3, Title3, Author3, Qty3), (id4, Title4, Author4, Qty4), (id5, Title5, Author5, Qty5)]
    cursor.executemany('''INSERT INTO books(
    id, Title, Author, Qty)VALUES(?,?,?,?)''', bookList)
    bookDB.commit#Insert the books into the 'books' database

def printBooks(): #Function to print out the whole 'books' database
    cursor.execute('''SELECT * FROM books''')
    records = cursor.fetchall()
    for newLine in records: 
        print(f"Id:       {newLine[0]}")
        print(f"Title:    {newLine[1]}")
        print(f"Author:   {newLine[2]}")
        print(f"Quantity: {newLine[3]}\n")
    input("Press enter to return to menu") #On users input return to menu
    printMenu()
    
def enterBook(): #Function to enter in a new book
    newBookid = input('\nEnter the books id: ')
    newBookTitle = input('Enter the books title: ')
    newBookAuthor = input('Enter the books author: ')
    newBookQty = input('Enter the quantity of books in stock: ') #Gather inputs from the user
    newBook = (newBookid, newBookTitle, newBookAuthor, newBookQty) #Create tuple of the users new book
    cursor.execute('''INSERT INTO books(
    id, Title, Author, Qty) VALUES(?,?,?,?)''', newBook)
    bookDB.commit #Insert the new book
    print(f'\n"{newBookTitle}" has been added to the database\n')
    input("Press enter to return to menu") #On users input return to menu
    printMenu()

def updateBook(): #Function to update the atrribute of an existing book
    updateBook = input("\nEnter the ID or Title of the book you want to update: ") #User chooses the book to change
    cursor.execute('''SELECT * FROM books
    WHERE id == ? OR Title LIKE ?''', (updateBook, updateBook))
    makeChange = input(f"\nIs this the book you want to update?\n{cursor.fetchall()}\n[y/n]: ") #Requires user confirmation to change the book
    if makeChange == 'y':
        print("+-------------------+") 
        print("|1. ID              |")
        print("|2. Title           |")
        print("|3. Author          |")
        print("|4. Quantity        |")
        print("+-------------------+") #Print user options for which attribute to change
        selectChange = int(input('What would you like to change? [1-4]: ')) #User chooses the attribute to change
        if selectChange == 1:
            update = input('Enter the books new id: ')
            cursor.execute('''UPDATE books SET id = ?
            WHERE id == ? OR Title LIKE ?''', (update, updateBook, updateBook))
            bookDB.commit #Change the 'id' attribute
        elif selectChange == 2:
            update = input('Enter the books new title: ')
            cursor.execute('''UPDATE books SET Title = ?
            WHERE id == ? OR Title LIKE ?''', (update, updateBook, updateBook))
            bookDB.commit #Change the 'Title' attribute
        elif selectChange == 3:
            update = input('Enter the books new author: ')
            cursor.execute('''UPDATE books SET Author = ?
            WHERE id == ? OR Title LIKE ?''', (update, updateBook, updateBook))
            bookDB.commit #Change the 'Author' attribute
        elif selectChange == 4:
            update = input('Enter the new quantity of books in stock: ')
            cursor.execute('''UPDATE books SET Qty = ?
            WHERE id == ? OR Title LIKE ?''', (update, updateBook, updateBook))
            bookDB.commit #Change the 'Qty' attribute
        else:
            print('Error, try again') #Fault detection. Returns to menu
            printMenu()
    elif makeChange == 'n':
        input("Press enter to return to menu") #If user made a mistake or changed mind. Returns to menu
        printMenu()
    else:
        tryAgain = input("Do you want to choose a different book? [y/n]: ") #If user made a mistake or changed mind. Returns to update menu
        if tryAgain == 'y':
            updateBook()
        else:
            input("Press enter to return to menu") #If user made a mistake or changed mind. Returns to menu
            printMenu()

def deleteBook(): #Function to delete a book from the 'books' database
    delBook = input("Enter the ID or Title of the book you want to delete: ") #User chooses the book to delete
    cursor.execute('''SELECT * FROM books
    WHERE id == ? OR Title LIKE ?''', (delBook, delBook))
    delete = input(f"Is this the book you want to delete?\n{cursor.fetchmany()}\n[y/n]: ") #Requires user confirmation to delete the book
    if delete == 'y': #Confirming deletion
        cursor.execute('''DELETE FROM books
        WHERE id == ? OR Title LIKE ?''', (delBook, delBook))
        bookDB.commit #Delete book
        input("Book deleted. Press enter to return to menu") #On users input return to menu
        printMenu()
    else:
        input("Press enter to return to menu") #If user made a mistake or changed mind. Returns to menu
        printMenu()

def searchBook(): #Function to search for a book from the 'books' database
    search = input("\nEnter the book ID or Title: ") #User chooses the book to search for by ID or Title
    cursor.execute('''SELECT * FROM books
    WHERE id == ? OR Title LIKE ?''',(search, search))
    records = cursor.fetchall()
    for newLine in records:
        print(f"\n")
        print(f"Id:       {newLine[0]}")
        print(f"Title:    {newLine[1]}")
        print(f"Author:   {newLine[2]}")
        print(f"Quantity: {newLine[3]}\n") #Print the chosen book
    input("Press enter to return to menu") #On users input return to menu
    printMenu()

def printMenu(): #Print menu for user to navigate
    print("\n")
    print("+-------------------+")
    print("|1. Enter book      |")
    print("|2. Update book     |")
    print("|3. Delete book     |")
    print("|4. Search books    |")
    print("|5. Show all books  |")
    print("|0. Exit            |")
    print("+-------------------+") #Print menu
    
    menuOption = int(input("What would you like to do? [0-5]: ")) #Users navigation choice
    
    if menuOption == 1:
        enterBook()
    elif menuOption == 2:
        updateBook()
    elif menuOption == 3:
        deleteBook()
    elif menuOption == 4:
        searchBook()
    elif menuOption == 5:
        printBooks()
    elif menuOption == 0: #Perform navigation choice
        exit
    else:
        input("Error!\nPress enter to return to menu") #Fault detection
    printMenu()


#createBooksTable()
insertBooks()
printMenu()



















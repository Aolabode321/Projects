import sqlite3
import random as rd

#connect to a database
db = sqlite3.connect('books_db')
print('connection established')


# create cursor object
cursor = db.cursor()


# create a table for books 
cursor.execute('''
     CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, 
                                       title TEXT NOT NULL UNIQUE,
                                        author TEXT,
                                        genre TEXT,
                                        copies INTEGER,
                                        borrowed INTEGER);

''')

# create table for customers with foreign key 
cursor.execute('''
       CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY,
                                              name TEXT NOT NULL,
                                              fines INTEGER,
                                              books_id INTEGER NOT NULL,
                                              FOREIGN KEY (books_id)
                                              REFERENCES books(id));

''')


results1 = cursor.execute('''
SELECT books.title, customers.name
FROM books
INNER JOIN customers ON books.id = customers.books_id
''')

db.commit()
print('table created!')




# create a menu
menu = input('''
Welcome to the Library Database! Please make a selection below!
      a - add a new book to database
      d - delete book from database       
      e - edit book in the database 
      i - view inventory
      b - check books being borrowed
      q - quit
''')


# create a fuction to insert book into database
def insert_book ():
    id_ = rd.randint(1000,9999)
    title = input("Please enter title of book : ")
    author = input("Please enter the author of the book : ")
    genre = input("please enter the genre of book : ")
    copies = input("how many copies : ")
    borrowed = 0

    cursor.execute('''
       INSERT INTO books (id, title, author, genre, copies, borrowed)
                   VALUES(?,?,?,?,?,?);
''',      (id_,title,author,genre,copies,borrowed))
    
    db.commit()
    print('Books have been inserted!')


# create a function to view books in table 
def view_books ():
    result = cursor.execute('SELECT * FROM books')
    data = result.fetchall()

   

    for row in data:
        print(f'ID: {row[0]}' )
        print(f'Title: {row[1]}')
        print(f'Author: {row[2]}')
        print(f'Genre: {row[3]}')
        print(f'copies: {row[4]}')
        print(f'borrowed: {row[5]}')

        print('')


# check books being borrowed
def check_borrowed ():

    for row in results1.fetchall():
        print(f'Title: {row[0]},is being borrowed to Customer: {row[1]}')


# create a function to check out a book
def delete_book():
    book_to_delete = int(input(print('plese enter the id of the book to delete : ')))

    cursor.execute('DELETE FROM books WHERE id = ?', (book_to_delete,))
    db.commit()

    print('Book Deleted!')
    








if menu == 'a':
    insert_book()
elif menu == 'i':
    view_books()
elif menu == 'b':
    check_borrowed()
elif menu == 'd':
    delete_book()
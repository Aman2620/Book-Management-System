import mysql.connector


config = {
    'user': 'root',
    'password': 'Aman260102_',
    'host': 'localhost',
    'database': 'book_management',
}

def add_book(title, author, publication_year):
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            print("Connected to MySQL database")

            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # SQL query to insert a new book
            sql_query = "INSERT INTO books (title, author, PUBLICATIONYEAR) VALUES (%s, %s, %s)"
            book_data = (title, author, publication_year)

            # Execute the SQL query
            cursor.execute(sql_query, book_data)

            # Commit the changes to the database
            connection.commit()

            print("Book added successfully.")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))

    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

def display_books():
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            print("Connected to MySQL database")

            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # SQL query to select all books
            sql_query = "SELECT * FROM BOOKS"

            # Execute the SQL query
            cursor.execute(sql_query)

            # Fetch all rows from the executed query
            rows = cursor.fetchall()

            # Display the fetched rows
            for row in rows:
                print(row)

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    
    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

# Function to update book information
def update_book(book_id, new_title, new_author, new_publication_year):
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            print("Connected to MySQL database")

            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # SQL query to update book information
            sql_query = "UPDATE BOOKS SET TITLE = %s, AUTHOR = %s, PUBLICATIONYEAR = %s WHERE ID = %s"
            book_data = (new_title, new_author, new_publication_year, book_id)

            # Execute the SQL query
            cursor.execute(sql_query, book_data)

            # Commit the changes to the database
            connection.commit()

            print("Book information updated successfully.")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))

    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")


# Function to delete a book
def delete_book(book_id):
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            print("Connected to MySQL database")

            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # SQL query to delete a book
            sql_query = "DELETE FROM BOOKS WHERE ID = %s"
            book_data = (book_id,)

            # Execute the SQL query
            cursor.execute(sql_query, book_data)

            # Commit the changes to the database
            connection.commit()

            print("Book deleted successfully.")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))

    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

# Main function to interact with the user
def main():
    while True:
        print("Book Management System")
        print("1. Add a new book")
        print("2. Display all books")
        print("3. Update book information")
        print("4. Delete a book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Get book details from the user
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            publication_year = int(input("Enter the publication year of the book: "))
            
            # Call the add_book function
            add_book(title, author, publication_year)

        elif choice == '2':
            # Call the display_books function
            display_books()

        elif choice == '3':
            # Get book ID and updated details from the user
            book_id = int(input("Enter the ID of the book you want to update: "))
            new_title = input("Enter the new title of the book: ")
            new_author = input("Enter the new author of the book: ")
            new_publication_year = int(input("Enter the new publication year of the book: "))
            
            # Call the update_book function
            update_book(book_id, new_title, new_author, new_publication_year)

        elif choice == '4':
            # Get book ID from the user
            book_id = int(input("Enter the ID of the book you want to delete: "))
            
            # Call the delete_book function
            delete_book(book_id)

        elif choice == '5':
            # Exit the program
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()





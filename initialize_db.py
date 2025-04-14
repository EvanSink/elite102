import sqlite3

DB_NAME = 'evans_project.db'


def initialize_database():
    connection = sqlite3.connect(DB_NAME)
    print("Connected to the database.")
    cursor = connection.cursor()
    print("Cursor created.")
    # Create a sample table
    print("Creating table if it does not exist...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bankingInfo
            (bank_id integer primary key, 
            username text, 
            bank_pin integer, 
            credit integer, 
            balance integer)
    ''')

    print("Table created.")

    print("Please enter the following information:")
    username = input("Username: ")
    bank_pin = int(input("Bank Pin: "))
    credit = int(input("Credit: "))
    balance = int(input("Balance: "))

    # Insert sample data
    print("Inserting sample data...")
    cursor.execute('''
        INSERT INTO bankingInfo (username, bank_pin, credit, balance) VALUES
        (?, ?, ?, ?)
    ''', (username, bank_pin, credit, balance))
    print("Person data inserted.")
    # Commit the changes and close the connection
    print("Making sure the code is actually changing and not just repeating...")
    print("Committing changes and closing the connection...")
    connection.commit()
    connection.close()


initialize_database()

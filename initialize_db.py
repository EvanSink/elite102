import sqlite3

DB_NAME = 'evans_project.db'

"""Initializes the database."""
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
    """Asks to delete an existing account. DOES NOT WORK!!!"""
    delete_existing_data = input("Do you want to delete an existing account? (yes/no): ")
    if delete_existing_data.lower() == 'yes':
        username_to_delete = input("Enter the username of the account to delete: ")
        cursor.execute('DELETE FROM bankingInfo WHERE username = ?', (username_to_delete,))
        print(f"Account with username '{username_to_delete}' deleted.")
        print("THIS FEATURE ONLY WORKS WITH SQL PRO! VERY SORRY!")
    else:
        print("No accounts deleted.")
        print("THIS FEATURE ONLY WORKS WITH SQL PRO! VERY SORRY!")
    """Asks the user if they would like to exit the program or continue."""
    ask_to_exit = input("Is there anything else you want to do? (yes/no): ")
    if ask_to_exit.lower() == 'yes':
        print("Returning to the program...")
    else:
        print("Exiting the program...")
        exit()
    
    

    """Asks for the user and their info to make a new account."""
    print("Please enter the following information:")
    username = input("Username: ")
    bank_pin = int(input("Bank Pin: "))
    credit = int(input("Credit: "))
    balance = int(input("Balance: "))

    """Creates new account."""
    # Insert sample data
    print("Inserting sample data...")
    cursor.execute('''
        INSERT INTO bankingInfo (username, bank_pin, credit, balance) VALUES
        (?, ?, ?, ?)
    ''', (username.lower(), bank_pin, credit, balance))
    print("Person data inserted.")
    # Commit the changes and close the connection
    print("Making sure the code is actually changing and not just repeating...")
    """
    maybe_delete = input("Do you want to delete the account? (yes/no): ")
    if maybe_delete.lower() == 'yes':
        cursor.execute('DELETE FROM bankingInfo WHERE username = ?', (username,))
        print("Account deleted.")
    else:
        print("Account not deleted.")
    """
    print("Committing changes and closing the connection...")
    print("Thank you!")
    connection.commit()
    connection.close()


initialize_database()

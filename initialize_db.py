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

    """Asks for the user and their info to make a new account."""
    print("Please enter the following information:")
    username = input("Username: ")
    bank_pin = int(input("Bank Pin: "))
    credit = int(input("Credit: "))
    balance = int(input("Balance: "))
    print("If this doesn't match any accounts in the database, it will create a new account.")
    print("If this matches an account in the database, it will update the account.")
    # Check if the table exists
    cursor.execute('''
        SELECT name FROM sqlite_master WHERE type='table' AND name='bankingInfo'
    ''')
    if cursor.fetchone() is None:
        print("Table does not exist. Creating table...")
        cursor.execute('''
            CREATE TABLE bankingInfo
                (bank_id integer primary key, 
                username text, 
                bank_pin integer, 
                credit integer, 
                balance integer)
        ''')
    else:
        print("Table already exists.")
        print("Fetching all rows from the bankingInfo table...")
    results = cursor.execute('''
        SELECT * FROM bankingInfo
    ''')
    print("Results:")
    for row in results:
        print(row)

    print("What would you like to do?): ")
    menu = input("1. Create a new account\n2. Delete an existing account\n3. Make a deposit into your account.\n4. Make a withdraw from your account\n5. Exit\n")

    if menu == '1':
        pass
    elif menu == '2':
        """Asks to delete an existing account. DOES NOT WORK!!!"""
        delete_existing_data = input("Do you want to delete an existing account? (yes/no): ")
        if delete_existing_data.lower() == 'yes':
            username_to_delete = input("Enter the username of the account to delete: ")
            if username_to_delete == username:
                username = username_to_delete
            else:
                print("No account found with that username.")
                exit()
            inputPin = int(input("Enter the bank pin of the account to delete: "))
            if inputPin != bank_pin:
                print("Incorrect bank pin.")
                exit()
            if username_to_delete == username and inputPin == bank_pin:
                print("Account found.")
                print("Deleting account...")
            cursor.execute('DELETE FROM bankingInfo WHERE username = ?', (username,))
            print(f"Account with username '{username}' deleted.")
            print("THIS FEATURE ONLY WORKS WITH SQL PRO! VERY SORRY!")
            exit()
        else:
            print("No accounts deleted.")
            print("THIS FEATURE ONLY WORKS WITH SQL PRO! VERY SORRY!")
            exit() 
    elif menu == '3':
        deposit_into_balance = input("Do you want to deposit into your balance? (yes/no): ")
        if deposit_into_balance.lower() == 'yes':
            username_to_deposit = input("Enter the username of the account to deposit into: ")
            username = username_to_deposit
            newPin = int(input("Enter the bank pin of the account to deposit into: "))
            if newPin != bank_pin:
                print("Incorrect bank pin.")
                exit()
            if username_to_deposit == username and newPin == bank_pin:
                print("Account found.")
                deposit_amount = int(input("Enter the amount to deposit: "))
                cursor.execute('UPDATE bankingInfo SET balance = balance + ? WHERE username = ?', (deposit_amount, username))
                print(f"Deposited {deposit_amount} into the account.")
        else:
            print("No deposit made.")
            print("Returning to the program...")
    elif menu == '4':
        withdraw_from_balance = input("Do you want to withdraw from your balance? (yes/no): ")
        if withdraw_from_balance.lower() == 'yes':
            username_to_withdraw = input("Enter the username of the account to withdraw from: ")
            username = username_to_withdraw
            withdraw_amount = int(input("Enter the amount to withdraw: "))
            cursor.execute('UPDATE bankingInfo SET balance = balance - ? WHERE username = ?', (withdraw_amount, username))
            print(f"Withdrew {withdraw_amount} from the account.")
        else:
            print("No withdrawal made.")
            print("Returning to the program...")
    elif menu == '5':
        print("Exiting the program...")
        exit()
    else:
        print("Exiting the program...")
        exit()
    print("Table created.")
    """
    delete_existing_data = input("Do you want to delete an existing account? (yes/no): ")
    if delete_existing_data.lower() == 'yes':
        username_to_delete = input("Enter the username of the account to delete: ")
        cursor.execute('DELETE FROM bankingInfo WHERE username = ?', (username_to_delete,))
        print(f"Account with username '{username_to_delete}' deleted.")
        print("THIS FEATURE ONLY WORKS WITH SQL PRO! VERY SORRY!")
    else:
        print("No accounts deleted.")
        print("THIS FEATURE ONLY WORKS WITH SQL PRO! VERY SORRY!")
    ask_to_exit = input("Is there anything else you want to do? (yes/no): ")
    if ask_to_exit.lower() == 'yes':
        print("Returning to the program...")
    else:
        print("Exiting the program...")
        exit()

    deposit_into_balance = input("Do you want to deposit into your balance? (yes/no): ")
    if deposit_into_balance.lower() == 'yes':
        deposit_amount = int(input("Enter the amount to deposit: "))
        cursor.execute('UPDATE bankingInfo SET balance = balance + ? WHERE username = ?', (deposit_amount, username_to_delete))
        print(f"Deposited {deposit_amount} into the account.")
    else:
        print("No deposit made.")
        print("Returning to the program...")
    """

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

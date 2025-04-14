import sqlite3


def main():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    # Get all rows from the students table
    print("Fetching all rows from the students table...")
    results = cursor.execute('''
        SELECT * FROM students
    ''')

    print("Results:")
    for row in results:
        print(row)

    # Get all students with a GPA greater than 3.5
    print("Fetching students with GPA greater than 3.5...")
    results = cursor.execute('''
        SELECT * FROM students WHERE gpa > 3.5
    ''')
    print("Results:")
    for row in results:
        print(row)

    connection.close()


if __name__ == "__main__":
    main()


"""
Print the gui to the screen
import tkinter as tk
def main():
    root = tk.Tk()
    root.title("Sample GUI")

    label = tk.Label(root, text="Hello, World!")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Click Me", command=lambda: print(entry.get()))
    button.pack()

    root.mainloop()
if __name__ == "__main__":  
Whats your Pin?
Whats your User?
Whats your Password?

"""
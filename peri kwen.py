from tkinter import *
import sqlite3

root = Tk()
root.title("My Project")
root.geometry("500x500")

# Database connection
conn = sqlite3.connect('my_project.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute("""CREATE TABLE IF NOT EXISTS student_info (
    f_name TEXT,
    l_name TEXT,
    age INTEGER,
    address TEXT,
    email TEXT
)""")
conn.commit()

# Submit function to insert data into the database
def submit():
    c.execute("INSERT INTO student_info (f_name, l_name, age, address, email) VALUES (?, ?, ?, ?, ?)",
              (f_name.get(), l_name.get(), age.get(), address.get(), email.get()))
    conn.commit()

    # Clear the text boxes after submission
    f_name.delete(0, END)
    l_name.delete(0, END)
    age.delete(0, END)
    address.delete(0, END)
    email.delete(0, END)

# Query function to fetch and display data from the database
def query():
    c.execute("SELECT *, oid FROM student_info")
    records = c.fetchall()

    print_records = ""
    for record in records:
        print_records += f"{record[0]} {record[1]} {record[2]} {record[3]} {record[4]} \t {record[5]}\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=30, column=0, columnspan=2)

# Delete function to remove a record by its ID
def delete():
    record_id = delete_box.get()
    c.execute("DELETE from student_info WHERE oid=?", (record_id,))
    conn.commit()

    delete_box.delete(0, END)

# Edit function to update a record by its ID
def edit():
    editor = Tk()
    editor.title("Update Record")
    editor.geometry("500x500")

    record_id = delete_box.get()
    c.execute("SELECT * FROM student_info WHERE oid=?", (record_id,))
    records = c.fetchall()

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        age_editor.insert(0, record[2])
        address_editor.insert(0, record[3])
        email_editor.insert(0, record[4])

    # Create text boxes in the editor window
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    age_editor = Entry(editor, width=30)
    age_editor.grid(row=2, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=3, column=1, padx=20)
    email_editor = Entry(editor, width=30)
    email_editor.grid(row=4, column=1, padx=20)

    editor.mainloop()

# Text boxes for input
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
age = Entry(root, width=30)
age.grid(row=2, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=3, column=1, padx=20)
email = Entry(root, width=30)
email.grid(row=4, column=1, padx=20)

# Labels for text boxes
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
age_label_label = Label(root, text="Age")
age_label_label.grid(row=2, column=0)
address_label_label = Label(root, text="Address")
address_label_label.grid(row=3, column=0)
email_label_label = Label(root, text="Email")
email_label_label.grid(row=4, column=0)

# Submit button to add data to the database
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Query button to fetch records from the database
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Delete entry field for specifying which ID to delete
delete_box = Entry(root, width=30)
delete_box.grid(row=10, column=1, padx=30)

delete_box_label = Label(root, text="Select ID No.")
delete_box_label.grid(row=10, column=0)

# Delete button to delete records from the database
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

root.mainloop()

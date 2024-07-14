# Welcome to Julie's Party Hire Store created by Neil.

from tkinter import *
import sqlite3


root = Tk()
root.title("Julie's Party Hire Store")
root.configure(bg="goldenrod")
root.geometry("462x400")

# Databases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        receipt integer,
        item text,
        number integer,
        date integer
        )""")
'''
# Create function to Delete a row of a customers details
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #Create cursor
    c = conn.cursor()  

    # Delete a certain row of Customers details
    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())

    delete_box.delete(0, END)

    #Commit changes
    conn.commit()

    # Close Connection
    conn.close()



# Create submit function for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #Create cursor
    c = conn.cursor()  
    
    # Insert into Table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :receipt, :item, :number, :date)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'receipt': receipt.get(),
                'item': item.get(),
                'number': number.get(),
                'date': date.get()
            })


    #Commit changes
    conn.commit()

    # Close Connection
    conn.close()
    
    # Clear The Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    receipt.delete(0, END)
    item.delete(0, END)
    number.delete(0, END)
    date.delete(0, END)    
    
# Create Query Function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #Create cursor
    c = conn.cursor() 

    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    customerdetails = c.fetchall()
    print(customerdetails)
    
    # Loop Thru Results
    print_customerdetails = ''
    for customerdetail in customerdetails:
        print_customerdetails += str(customerdetail) + "\n"

    query_label = Label(root, text=print_customerdetails, bg="hot pink")    
    query_label.grid(row=11, column=0, columnspan=2)

    #Commit changes
    conn.commit()

    # Close Connection
    conn.close()

# Create Text boxes of each 6 customer details needed
f_name = Entry(root, width=30)
f_name.grid(row=2, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=3, column=1, padx=20)
receipt = Entry(root, width=30)
receipt.grid(row=4, column=1, padx=20)
item = Entry(root, width=30)
item.grid(row=5, column=1, padx=20)
number = Entry(root, width=30)
number.grid(row=6, column=1, padx=20)
date = Entry(root, width=30)
date.grid(row=7, column=1, padx=20)
delete_box =Entry(root, width=30)
delete_box.grid(row=8, column=1, pady=5)

# Create labels on the side for each box to know where your writting to customer details
f_name_label = Label(root, text="First Name :", bg="dark goldenrod", fg="purple")
f_name_label.grid(row=2, column=0, pady=(10, 0))
f_name_label = Label(root, text="Must Be a String", fg="red")
f_name_label.grid(row=2, column=3, pady=(10, 0))

l_name_label = Label(root, text="Last Name :", bg="dark goldenrod", fg="purple")
l_name_label.grid(row=3, column=0)
l_name_label = Label(root, text="Must be a String", fg="red")
l_name_label.grid(row=3, column=3)

receipt_label = Label(root, text="Receipt Number", bg="dark goldenrod")
receipt_label.grid(row=4, column=0)
receipt_label = Label(root, text="Must be an Integer", fg="red")
receipt_label.grid(row=4, column=3)

item_label = Label(root, text="Item Hired :", bg="dark goldenrod", fg="purple")
item_label.grid(row=5, column=0)
item_label = Label(root, text="Must be a String", fg="red")
item_label.grid(row=5, column=3)

number_name_label = Label(root, text="Number of Item Hired :", bg="dark goldenrod")
number_name_label.grid(row=6, column=0)
number_name_label = Label(root, text="Must be an Integer", fg="red")
number_name_label.grid(row=6, column=3)

date_name_label = Label(root, text="Date Hired :", bg="dark goldenrod")
date_name_label.grid(row=7, column=0)
date_name_label = Label(root, text="Must be Entered", fg="red")
date_name_label.grid(row=7, column=3)


# Creating a Submit Button
submit_btn = Button(root, text="Append Customers Details", command=submit, fg="white", bg="deep sky blue")
submit_btn.grid(row=0, column=0, columnspan=2, pady=1, padx=1, ipadx=1)

# Creating a Query Button
query_btn = Button(root, text="Print", command=query, fg="white", bg="deep sky blue")
query_btn.grid(row=1, column=0, columnspan=2, pady=1, padx=15, ipadx=15)

#Create a Delete Button
delete_btn = Button(root, text="Delete Row #", command=delete, bg="maroon")
delete_btn.grid(row=8, column=0, pady=5, ipadx=23)

# Create a Quit Button
quit_btn = Button(root, text="EXIT", command=quit, fg="white", bg="dark green")
quit_btn.grid(row=0, column=3, columnspan=1, pady=1, padx=10, ipadx=15)

#Commit changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()
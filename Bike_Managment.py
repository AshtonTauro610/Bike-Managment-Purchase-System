# IMPORTING ALL THE MODULES FOR THE PROGRAM
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector as con

# CREATING THE FRAME OF TKINTER
root = Tk()
root.title('Harley Davidson Motors')
root.iconbitmap(r'harley.ico')
root.geometry('905x650+300+150')
root.resizable(0, 0)

# mySQL FRAME WORK OR STRUCTURE
mainframe = Frame(root, bd=10, width=770, height=700, relief=RIDGE, bg='black')
mainframe.grid()

titleframe = Frame(mainframe, bd=7, width=770, height=100, relief=RIDGE, bg='black')
titleframe.grid(row=0, column=0)

topframe = Frame(mainframe, bd=5, width=770, height=500, relief=RIDGE, bg='red')
topframe.grid(row=1, column=0)

leftframe = Frame(topframe, bd=5, width=770, height=400, padx=2, relief=RIDGE, bg='gold')
leftframe.pack(side=LEFT)

leftframe1 = Frame(leftframe, bd=5, width=600, height=180, padx=2, pady=4, relief=RIDGE, bg='grey')
leftframe1.pack(side=TOP, padx=0, pady=0)

rframe = Frame(topframe, bd=5, width=100, height=400, padx=2, relief=RIDGE, bg='maroon')
rframe.pack(side=RIGHT)

rframe1 = Frame(rframe, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE)
rframe1.pack(side=TOP)

# Defining the type of the variable
Bill = StringVar()
ModelName = StringVar()
CustomerName = StringVar()
MobileNo = StringVar()
City = StringVar()
DOP = StringVar()
Price = StringVar()

# Functions
def Exit():
    Exit = tkinter.messagebox.askyesno('Harley Davidson Motors', 'Thank You\nDo You Want To EXIT')
    if Exit:
        root.destroy()
        return

def Reset():
    eBill.delete(0, END)
    ModelName.set(" ")
    eCustomerName.delete(0, END)
    eMobileNo.delete(0, END)
    eCity.delete(0, END)
    edop.delete(0, END)
    ePrice.delete(0, END)

def display():
    db = con.connect(host='localhost', user='root', password='200506', database='harleymotors')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM bikes')
    res = cursor.fetchall()
    if len(res) != 0:
        strecords.delete(*strecords.get_children())
        for i in res:
            strecords.insert('', END, values=i)
    db.commit()
    db.close()

def displaydata(h):
    info = strecords.focus()
    data = strecords.item(info)
    row = data['values']
    Bill.set(row[0])
    ModelName.set(row[1])
    CustomerName.set(row[2])
    MobileNo.set(row[3])
    City.set(row[4])
    DOP.set(row[5])
    Price.set(row[6])

def add():
    db = con.connect(host='localhost', user='root', password='200506', database='harleymotors')
    cursor = db.cursor()
    cursor.execute('INSERT INTO bikes VALUES (%s, %s, %s, %s, %s, %s, %s)',
                   (Bill.get(), ModelName.get(), CustomerName.get(), MobileNo.get(), City.get(), DOP.get(), Price.get()))
    db.commit()
    db.close()
    tkinter.messagebox.showinfo('Data Entry Form', 'Record Entered Successfully')
    display()

def update():
    db = con.connect(host='localhost', user='root', password='200506', database='harleymotors')
    cursor = db.cursor()
    cursor.execute('UPDATE bikes SET ModelName=%s, CustName=%s, Mobileno=%s, City=%s, DOP=%s, Price=%s WHERE Billno=%s',
                   (ModelName.get(), CustomerName.get(), MobileNo.get(), City.get(), DOP.get(), Price.get(), Bill.get()))
    db.commit()
    db.close()
    tkinter.messagebox.showinfo('Data Entry Form', 'Record Updated Successfully')
    Reset()
    display()

def deletedb():
    db = con.connect(host='localhost', user='root', password='200506', database='harleymotors')
    cursor = db.cursor()
    cursor.execute('DELETE FROM bikes WHERE Billno=%s', (Bill.get(),))
    db.commit()
    db.close()
    tkinter.messagebox.showinfo('Data Entry Form', 'Record Deleted Successfully')
    Reset()
    display()

def search():
    try:
        db = con.connect(host='localhost', user='root', password='200506', database='harleymotors')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM bikes WHERE Billno=%s', (Bill.get(),))
        row = cursor.fetchone()
        if row:
            Bill.set(row[0])
            ModelName.set(row[1])
            CustomerName.set(row[2])
            MobileNo.set(row[3])
            City.set(row[4])
            DOP.set(row[5])
            Price.set(row[6])
        else:
            tkinter.messagebox.showinfo('Data Entry Form', 'Record Not Found')
            Reset()
        db.commit()
        db.close()
    except:
        tkinter.messagebox.showinfo('Data Entry Form', 'Record Not Found')
        Reset()

# CREATING THE TITLE OR NAME OF THE COMPANY
title = Label(titleframe, font=('Georgia', 35, 'bold'), text='Harley Davidson Motors', bd=7, bg='black', fg='gold')
title.grid(row=0, column=0, padx=132)

# CREATING LABEL AND ENTRY WIDGET FOR ENTERING THE VALUES IN TKINTER THROUGH PYTHON
lBill = Label(leftframe1, font=('Georgia', 10, 'bold'), text='Bill No.', bd=7, bg='grey')
lBill.grid(row=1, column=0, sticky=W, padx=5)
eBill = Entry(leftframe1, font=('Georgia', 10, 'bold'), bd=5, width=40, justify='left', textvariable=Bill)
eBill.grid(row=1, column=1, sticky=W, padx=5)

lModelName = Label(leftframe1, font=('Georgia', 10, 'bold'), text='Model Name', bd=5, bg='grey')
lModelName.grid(row=2, column=0, sticky=W, padx=5)
cboModelName = ttk.Combobox(leftframe1, font=('Georgia', 10, 'bold'), width=38, state='readonly', textvariable=ModelName)
cboModelName['values'] = (' ', 'Street 750', 'Iron 883', 'SuperLow', 'Forty-Eight', 'Seventy-Two', 'Low Rider', 'Fat Bob', 'Wide Glide', 'Switchback', 'Softail', 'Vrod Muscle', 'CVO', 'Steet Glide', 'Road Glide')
cboModelName.current(0)
cboModelName.grid(row=2, column=1)

lCustomerName = Label(leftframe1, font=('Georgia', 10, 'bold'), text='Customer Name', bd=7, bg='grey')
lCustomerName.grid(row=3, column=0, sticky=W, padx=5)
eCustomerName = Entry(leftframe1, font=('Georgia', 10, 'bold'), bd=5, width=40, justify='left', textvariable=CustomerName)
eCustomerName.grid(row=3, column=1, sticky=W, padx=5)

lMobileNo = Label(leftframe1, font=('Georgia', 10, 'bold'), text='Mobile No.', bd=7, bg='grey')
lMobileNo.grid(row=4, column=0, sticky=W, padx=5)
eMobileNo = Entry(leftframe1, font=('Georgia', 10, 'bold'), bd=5, width=40, justify='left', textvariable=MobileNo)
eMobileNo.grid(row=4, column=1, sticky=W, padx=5)

lCity = Label(leftframe1, font=('Georgia', 10, 'bold'), text='City', bd=7, bg='grey')
lCity.grid(row=5, column=0, sticky=W, padx=5)
eCity = Entry(leftframe1, font=('Georgia', 10, 'bold'), bd=5, width=40, justify='left', textvariable=City)
eCity.grid(row=5, column=1, sticky=W, padx=5)

ldop = Label(leftframe1, font=('Georgia', 10, 'bold'), text='Date of Purchase', bd=7, bg='grey')
ldop.grid(row=6, column=0, sticky=W, padx=5)
edop = Entry(leftframe1, font=('Georgia', 10, 'bold'), bd=5, width=40, justify='left', textvariable=DOP)
edop.grid(row=6, column=1, sticky=W, padx=5)

lPrice = Label(leftframe1, font=('Georgia', 10, 'bold'), text='Price($)', bd=7, bg='grey')
lPrice.grid(row=7, column=0, sticky=W, padx=5)
ePrice = Entry(leftframe1, font=('Georgia', 10, 'bold'), bd=5, width=40, justify='left', textvariable=Price)
ePrice.grid(row=7, column=1, sticky=W, padx=5)

# CREATING SCROLLBAR WHICH DISPLAYS THE OUTPUT IN TKINTER
scroll = Scrollbar(leftframe, orient=VERTICAL)
strecords = ttk.Treeview(leftframe, height=12, columns=('Billno.', 'ModelName', 'Customername', 'MobileNo', 'City', 'DOP', 'Price'), yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)
strecords.heading('Billno.', text='Bill No.')
strecords.heading('ModelName', text='Model Name')
strecords.heading('Customername', text='Customer Name')
strecords.heading('MobileNo', text='Mobile No.')
strecords.heading('City', text='City')
strecords.heading('DOP', text='Date of Purchase')
strecords.heading('Price', text='Price')

strecords['show'] = 'headings'
strecords.column('Billno.', width=70)
strecords.column('ModelName', width=100)
strecords.column('Customername', width=100)
strecords.column('MobileNo', width=100)
strecords.column('City', width=70)
strecords.column('DOP', width=70)
strecords.column('Price', width=70)

strecords.pack(fill=BOTH, expand=1)
strecords.bind('<ButtonRelease-1>', displaydata)

# ADDING BUTTONS IN TKINTER AND ASSIGNING BUTTONS TO VARIABLE AND FUNCTIONS
bAdd = Button(rframe1, font=('Georgia', 16, 'bold'), text='Add', bd=4, bg='gold', pady=1, padx=24, width=8, height=2, command=add)
bAdd.grid(row=0, column=0, padx=1)

bUpdate = Button(rframe1, font=('Georgia', 16, 'bold'), text='Update', bd=4, bg='gold', pady=1, padx=24, width=8, height=2, command=update)
bUpdate.grid(row=1, column=0, padx=1)

bDelete = Button(rframe1, font=('Georgia', 16, 'bold'), text='Delete', bd=4, bg='gold', pady=1, padx=24, width=8, height=2, command=deletedb)
bDelete.grid(row=2, column=0, padx=1)

bsearch = Button(rframe1, font=('Georgia', 16, 'bold'), text='Search', bd=4, bg='gold', pady=1, padx=24, width=8, height=2, command=search)
bsearch.grid(row=3, column=0, padx=1)

bDisplay = Button(rframe1, font=('Georgia', 16, 'bold'), text='Display', bd=4, bg='gold', pady=1, padx=24, width=8, height=2, command=display)
bDisplay.grid(row=4, column=0, padx=1)

bReset = Button(rframe1, font=('Georgia', 16, 'bold'), text='Reset', bd=4, bg='gold', pady=1, padx=24, width=8, height=2, command=Reset)
bReset.grid(row=5, column=0, padx=1)

bExit = Button(rframe1, font=('Georgia', 16, 'bold'), text='Exit', bd=4, bg='gold', pady=1, padx=24, width=8, height=2, command=Exit)
bExit.grid(row=6, column=0, padx=1)

mainloop()

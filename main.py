from tkinter import ttk
from PIL import ImageTk, Image
import tkinter as tk
import mysql.connector


mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='dbLifechoicesOnline', auth_plugin='mysql_native_password')
mycursor = mydb.cursor(buffered=True)


def ViewUser():
    mycursor.execute("SELECT * FROM tblUser")
    rows = mycursor.fetchall()
    for row in rows:
        tblNextOfKin.insert("", tk.END, values=row)


def ViewKin():
    mycursor.execute("SELECT * FROM tblNextOfKin")
    rows = mycursor.fetchall()
    for row in rows:
        # print(row)
        tblNextOfKin.insert("", tk.END, values=row)

def update_item():
    selected = tblNextOfKin.focus()
    temp = tblNextOfKin.item(selected, 'values')
    sal_up = edtname.get()
    tblNextOfKin.item(selected, values=(temp[0], temp[1], sal_up, temp[3]))


root = tk.Tk()
root.geometry("1500x1000")

pic1 = Image.open("Logo-Life-Choices.jpg")
resize = pic1.resize((1500, 90), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(resize)
lbpic = tk.Label(root, image=logo, bg='#f48c06')
lbpic.place(x=0, y=0)

lbHeading = tk.Label(root, text="LOG IN", font='Times 30')
lbHeading.place(x=130, y=120)

tblUser = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')

tblUser.column("#1", anchor=tk.CENTER)
tblUser.heading("#1", text="User_id")

tblUser.column("#2", anchor=tk.CENTER)
tblUser.heading("#2", text="NAME")

tblUser.column("#3", anchor=tk.CENTER)
tblUser.heading("#3", text="SURNAME")

tblUser.column("#4", anchor=tk.CENTER)
tblUser.heading("#4", text="ID NUMBER")

tblUser.column("#5", anchor=tk.CENTER)
tblUser.heading("#5", text="MOBILE")

tblUser.column("#6", anchor=tk.CENTER)
tblUser.heading("#6", text="LOGIN")

tblUser.column("#7", anchor=tk.CENTER)
tblUser.heading("#7", text="LOGOUT")

tblUser.place(x=40, y=190)

tblNextOfKin = ttk.Treeview(root, column=("c1", "c2", "c3", "c4"), show='headings')

tblNextOfKin.column("#1", anchor=tk.CENTER)
tblNextOfKin.heading("#1", text="NAME")

tblNextOfKin.column("#2", anchor=tk.CENTER)
tblNextOfKin.heading("#2", text="SURNAME")

tblNextOfKin.column("#3", anchor=tk.CENTER)
tblNextOfKin.heading("#3", text="MOBILE")

tblNextOfKin.column("#4", anchor=tk.CENTER)
tblNextOfKin.heading("#4", text="User_id")

tblNextOfKin.place(x=40, y=530)

def delete_data():
        row_id = tblNextOfKin.focus()
        tblNextOfKin.delete(row_id)


edtname = tk.Entry(root)
edtname.place(x=570, y=240)
btnKin = tk.Button(text="Display data", command=ViewKin)
btnKin.place(x=100, y=430)
btnUser = tk.Button(text="DISPLAY DATA", command=ViewUser)
btnUser.place(x=100, y=790)
button2 = tk.Button(text="update", command=update_item)
button2.place(x=480, y=230)
button3 = tk.Button(text="extend", command=delete_data)
button3.place(x=300, y=230)
# button1.pack(pady=10)

root.mainloop()

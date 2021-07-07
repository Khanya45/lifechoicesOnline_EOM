import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='dbLifechoicesOnline', auth_plugin='mysql_native_password')
mycursor = mydb.cursor(buffered=True)

root = Tk()
root.title("VISITOR")
root.geometry('400x400')


def login():
    mycursor.execute('SELECT ID FROM tblUser WHERE ID="'+edtID.get()+'"')
    count = 0
    # try:
    for i in mycursor:
        print(i)
        count += 1
    print(count)
    if count > 0:
        mycursor.execute('UPDATE tblUser SET logIn = current_time() WHERE ID="'+edtID.get()+'"')
        mydb.commit()
        messagebox.showerror("", "LOGIN successful")
    else:
        messagebox.showerror("", "the info supplied is incorrect")


def logout():
    mycursor.execute('SELECT ID FROM tblUser WHERE ID="'+edtID.get()+'"')
    count = 0
    # try:
    for i in mycursor:
        print(i)
        count += 1
    print(count)
    if count > 0:
        mycursor.execute('UPDATE tblUser SET logOut = current_time() WHERE ID="'+edtID.get()+'"')
        mydb.commit()
        messagebox.showerror("", "LOGOUT successful")
    else:
        messagebox.showerror("", "the info supplied is incorrect")


def exit():
    root.destroy()


def new_window():
    root.destroy()
    import sign_up


pic1 = Image.open("Logo-Life-Choices.jpg")
resize = pic1.resize((400, 90), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(resize)
lbpic = Label(root, image=logo, bg='#f48c06')
lbpic.place(x=0, y=0)

lbHeading = Label(root, text="LOG IN", font='Times 30')
lbHeading.place(x=130, y=120)

lbID = Label(root, text="ID number")
lbID.place(x=40, y=230)
edtID = Entry(root)
edtID.place(x=150, y=230)

lbSurname = Label(root, text="Visitor Name")
lbSurname.place(x=40, y=190)
edtSurname = Entry(root)
edtSurname.place(x=150, y=190)

btnLogin = Button(root, text="LOG IN", command=login)
btnLogin.place(x=50, y=300)

btnNew = Button(root, text="NEW VISITOR", command=new_window)
btnNew.place(x=225, y=300)

btnLogout = Button(root, text="LOG OUT", command=logout)
btnLogout.place(x=130, y=300)

btnLogin = Button(root, text="EXIT", command=exit)
btnLogin.place(x=160, y=350)


root.mainloop()





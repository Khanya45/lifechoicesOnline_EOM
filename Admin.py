import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='dbLifechoicesOnline', auth_plugin='mysql_native_password')
mycursor = mydb.cursor(buffered=True)


root = Tk()
root.title("ADMINISTRATOR")
root.geometry('400x400')
def login():
    mycursor.execute('SELECT Name, Password FROM tblAdmin WHERE Name="'+edtName.get()+'" AND Password="'+edtPassword.get()+'"')
    count = 0
    try:
        for i in mycursor:
          count += 1
        if count > 0:
            new_window()
        else:
            messagebox.showerror("", "the info supplied is incorrect")
    except:
        messagebox.showerror("", "the info supplied is incorrect")
        edtPassword.delete(0, END)
        edtSurname.delete(0, END)



def new_window():
    root.destroy()
    import administrator


def exit():
    root.destroy()


pic1 = Image.open("Logo-Life-Choices.jpg")
resize = pic1.resize((400, 80), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(resize)
lbpic = Label(root, image=logo, bg='#f48c06')
lbpic.place(x=0, y=0)

lbHeading = Label(root, text="LOG IN", font='Times 30')
lbHeading.place(x=130, y=120)


lbName = Label(root, text="Admin Name")
lbName.place(x=40, y=190)
edtName = Entry(root)
edtName.place(x=150, y=190)

lbSurname = Label(root, text="Admin Surname")
lbSurname.place(x=40, y=230)
edtSurname = Entry(root)
edtSurname.place(x=150, y=230)


lbPassword = Label(root, text="Password")
lbPassword.place(x=40, y=270)
edtPassword = Entry(root)
edtPassword.place(x=150, y=270)

btnLogin = Button(root, text="LOG IN", command=login)
btnLogin.place(x=130, y=330)

btnLogin = Button(root, text="EXIT", command=exit)
btnLogin.place(x=210, y=330)


root.mainloop()


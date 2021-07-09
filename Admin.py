import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='dbLifechoicesOnline', auth_plugin='mysql_native_password')
mycursor = mydb.cursor(buffered=True)


root = Tk()
root.title("ADMINISTRATOR")
root.geometry('400x400')
root.config(bg="#141215")


def login():
    mycursor.execute('SELECT Name, Password FROM tblAdministrator WHERE Name="'+edtName.get()+'" AND Password="'+edtPassword.get()+'"')
    count = 0
    try:
        for i in mycursor:
          count += 1
        if count > 0:
            mycursor.execute('UPDATE tblAdministrator SET logIn=current_time() WHERE Password="'+edtPassword.get()+'"')
            mydb.commit()
            new_window()
        else:
            messagebox.showerror("", "the info supplied is incorrect")
    except:
        messagebox.showerror("", "the info supplied is incorrect")


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

lbHeading = Label(root, text="LOG IN", font='Times 30', bg="#141215", fg="white")
lbHeading.place(x=130, y=120)


lbName = Label(root, text="Admin Name", bg="#141215", fg="white")
lbName.place(x=40, y=190)
edtName = Entry(root)
edtName.place(x=150, y=190)

lbSurname = Label(root, text="Admin Surname", bg="#141215", fg="white")
lbSurname.place(x=40, y=230)
edtSurname = Entry(root)
edtSurname.place(x=150, y=230)


lbPassword = Label(root, text="Password", bg="#141215", fg="white")
lbPassword.place(x=40, y=270)
edtPassword = Entry(root)
edtPassword.place(x=150, y=270)

btnLogin = Button(root, text="LOG IN", command=login, bg="#141215", fg="white")
btnLogin.place(x=130, y=330)

btnLogin = Button(root, text="EXIT", command=exit, bg="#141215", fg="white")
btnLogin.place(x=210, y=330)

# ======================VALIDATIONS===================

# VALIDATION FOR STRINGS
def is_string(name,surname):
    # flag = False
    if name.isdigit() == False and surname.isdigit() == False:
        flag = True
    else:
        flag = False
    return flag


# b1["state"] = DISABLED


# VALIDATION FOR INTEGERS
def is_number(mobile):
    # flag = False
    if mobile.isdigit() == True:
        flag = True
    else:
        flag = False
    return flag


# VALIDATION FOR LENGTH OF MOBILE
def length(mobile):
    # flag = False
    if len(mobile) == 10:
        flag = True
    else:
        flag = False
    return flag


# VALIDATION FOR LENGTH OF STRINGS
def string_length(name, surname):
    flag = False
    if len(name) != 0 and len(surname) != 0:
        flag = True
    else:
        flag = False
    return flag


if is_string("khanya3", "3455") == False or string_length("khan4ya", "534") == False:
    messagebox.showerror("", "Invalid character on name or surname entry")
elif is_number("364uyt498572") == False or length("7678765456") == False:
    messagebox.showerror("", "Invalid mobile number")
else:
    messagebox.showinfo("", "correct")


# if is_number("364uyt498572") == False or length("7678765456") == False:
#     messagebox.showerror("", "Invalid mobile number")
# else:
#     messagebox.showinfo("", "correct")




root.mainloop()


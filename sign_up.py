import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import rsaidnumber

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='dbLifechoicesOnline', auth_plugin='mysql_native_password')
mycursor = mydb.cursor(buffered=True)

root = Tk()
root.title("VISITOR")
root.geometry('700x550')
root.config(bg="#141215")


# ======================VALIDATIONS===================

# VALIDATION FOR STRINGS
def is_string(name,surname):
    # flag = False
    if name.isdigit() == False and surname.isdigit() == False:
        flag = True
    else:
        flag = False
    return flag


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


# FUNCTION FOR ADDING NEW USER TO THE DATABASE
def signup(id):
    if is_string(edtName.get(), edtSurname.get()) == False or string_length(edtName.get(), edtSurname.get()) == False:
        messagebox.showerror("", "Invalid character on name or surname entry")
    elif is_string(edtName_kin.get(), edtSurname_kin.get()) == False or string_length(edtName_kin.get(), edtSurname_kin.get()) == False:
        messagebox.showerror("", "Invalid character on name or surname entry")
    elif is_number(edtMobile.get()) == False or length(edtMobile.get()) == False:
        messagebox.showerror("", "Invalid mobile number")
    elif is_number(edtMobile_kin.get()) == False or length(edtMobile_kin.get()) == False:
        messagebox.showerror("", "Invalid mobile number")
    else:
        id_number = ""
        try:
            id_number = rsaidnumber.parse(id)
            mycursor.execute('INSERT INTO tblUser (Name, Surname, ID,Mobile) VALUES ("'+edtName.get()+'","'+edtSurname.get()+'","'+edtID.get()+'","'+edtMobile.get()+'")')
            mycursor.execute('INSERT INTO tblNextOfKin (Name, Surname,Mobile) VALUES ("'+edtName_kin.get()+'","'+edtSurname_kin.get()+'","'+edtMobile_kin.get()+'")')
            mycursor.execute('UPDATE tblUser SET logIn = current_time() WHERE ID="'+edtID.get()+'"')
            mycursor.execute('UPDATE tblNextOfKin SET User_id = (SELECT last_insert_id()) WHERE Mobile="'+edtMobile_kin.get()+'"')
            messagebox.showinfo("", "successfully added")
            mydb.commit()
        except:
            messagebox.showerror("", "Invalid ID number")


def exit():
    root.destroy()


def clear():
    edtID.delete(0, END)
    edtSurname.delete(0, END)
    edtName.delete(0, END)
    edtMobile_kin.delete(0, END)
    edtMobile.delete(0, END)
    edtName_kin.delete(0, END)
    edtSurname_kin.delete(0, END)


pic1 = Image.open("Logo-Life-Choices.jpg")
resize = pic1.resize((700, 90), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(resize)
lbpic = Label(root, image=logo, bg='#f48c06')
lbpic.place(x=0, y=0)

lbHeading = Label(root, text="NEW VISITOR", font='Times 30', bg="#141215", fg="white")
lbHeading.place(x=180, y=120)


# ========== VISITOR'S FRAME ===========
lbFrame_visitor = LabelFrame(root, text="VISITOR'S DETAILS", width=330, height=200, bg="#141215", fg="white")
lbFrame_visitor.place(x=20, y=200)

lbName = Label(lbFrame_visitor, text="Visitor Name", bg="#141215", fg="white")
lbName.place(x=10, y=20)
edtName = Entry(lbFrame_visitor)
edtName.place(x=130, y=20)

lbSurname = Label(lbFrame_visitor, text="Visitor Surname", bg="#141215", fg="white")
lbSurname.place(x=10, y=60)
edtSurname = Entry(lbFrame_visitor)
edtSurname.place(x=130, y=60)

lbID = Label(lbFrame_visitor, text="ID number", bg="#141215", fg="white")
lbID.place(x=10, y=100)
edtID = Entry(lbFrame_visitor)
edtID.place(x=130, y=100)

lbMobile = Label(lbFrame_visitor, text="Mobile number", bg="#141215", fg="white")
lbMobile.place(x=10, y=140)
edtMobile = Entry(lbFrame_visitor)
edtMobile.place(x=130, y=140)


# =========== VISITOR'S KIN FRAME ============
lbFrame_kin = LabelFrame(root, text="NEXT OF KIN DETAILS", width=310, height=200, bg="#141215", fg="white")
lbFrame_kin.place(x=370, y=200)

lbName_kin = Label(lbFrame_kin, text="Kin's Name", bg="#141215", fg="white")
lbName_kin.place(x=10, y=20)
edtName_kin = Entry(lbFrame_kin)
edtName_kin.place(x=120, y=20)

lbSurname_kin = Label(lbFrame_kin, text="Kin's Surname", bg="#141215", fg="white")
lbSurname_kin.place(x=10, y=70)
edtSurname_kin = Entry(lbFrame_kin)
edtSurname_kin.place(x=120, y=70)

lbMobile_kin = Label(lbFrame_kin, text="Mobile number", bg="#141215", fg="white")
lbMobile_kin.place(x=10, y=120)
edtMobile_kin = Entry(lbFrame_kin)
edtMobile_kin.place(x=120, y=120)

# ======== BUTTONS ON THE ROOT ===============
btnLogin = Button(root, text="SIGN UP", width=10, borderwidth=4, font="Times 15", command=lambda: signup(edtID.get()), bg="#141215", fg="white")
btnLogin.place(x=190, y=430)

btnClear = Button(root, text="CLEAR", width=10, borderwidth=4, font="Times 15", command=clear, bg="#141215", fg="white")
btnClear.place(x=350, y=430)

btnLogin = Button(root, text="EXIT", width=10, borderwidth=4, font="Times 15", command=exit, bg="#141215", fg="white")
btnLogin.place(x=270, y=490)


root.mainloop()

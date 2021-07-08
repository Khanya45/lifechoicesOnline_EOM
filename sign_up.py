import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='dbLifechoicesOnline', auth_plugin='mysql_native_password')
mycursor = mydb.cursor(buffered=True)

root = Tk()
root.title("VISITOR")
root.geometry('700x550')



def signup():
    mycursor.execute('INSERT INTO tblUser (Name, Surname, ID,Mobile) VALUES ("'+edtName.get()+'","'+edtSurname.get()+'","'+edtID.get()+'","'+edtMobile.get()+'")')
    mycursor.execute('INSERT INTO tblNextOfKin (Name, Surname,Mobile) VALUES ("'+edtName_kin.get()+'","'+edtSurname_kin.get()+'","'+edtMobile_kin.get()+'")')
    mycursor.execute('UPDATE tblNextOfKin SET User_id = (SELECT last_insert_id()) WHERE Mobile="'+edtMobile_kin.get()+'"')
    messagebox.showinfo("", "successfully added")
    mydb.commit()


def exit():
    root.destroy()


pic1 = Image.open("Logo-Life-Choices.jpg")
resize = pic1.resize((700, 90), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(resize)
lbpic = Label(root, image=logo, bg='#f48c06')
lbpic.place(x=0, y=0)

lbHeading = Label(root, text="NEW VISITOR", font='Times 30')
lbHeading.place(x=180, y=120)


# ========== VISITOR'S FRAME ===========
lbFrame_visitor = LabelFrame(root, text="VISITOR'S DETAILS", width=330, height=200)
lbFrame_visitor.place(x=20, y=180)

lbName = Label(lbFrame_visitor, text="Visitor Name")
lbName.place(x=10, y=20)
edtName = Entry(lbFrame_visitor)
edtName.place(x=130, y=20)

lbSurname = Label(lbFrame_visitor, text="Visitor Surname")
lbSurname.place(x=10, y=60)
edtSurname = Entry(lbFrame_visitor)
edtSurname.place(x=130, y=60)

lbID = Label(lbFrame_visitor, text="ID number")
lbID.place(x=10, y=100)
edtID = Entry(lbFrame_visitor)
edtID.place(x=130, y=100)

lbMobile = Label(lbFrame_visitor, text="Mobile number")
lbMobile.place(x=10, y=140)
edtMobile = Entry(lbFrame_visitor)
edtMobile.place(x=130, y=140)


# =========== VISITOR'S KIN FRAME ============
lbFrame_kin = LabelFrame(root, text="NEXT OF KIN DETAILS", width=310, height=200)
lbFrame_kin.place(x=370, y=180)

lbName_kin = Label(lbFrame_kin, text="Kin's Name")
lbName_kin.place(x=10, y=20)
edtName_kin = Entry(lbFrame_kin)
edtName_kin.place(x=120, y=20)

lbSurname_kin = Label(lbFrame_kin, text="Kin's Surname")
lbSurname_kin.place(x=10, y=70)
edtSurname_kin = Entry(lbFrame_kin)
edtSurname_kin.place(x=120, y=70)

lbMobile_kin = Label(lbFrame_kin, text="Mobile number")
lbMobile_kin.place(x=10, y=120)
edtMobile_kin = Entry(lbFrame_kin)
edtMobile_kin.place(x=120, y=120)

# ======== BUTTONS ON THE ROOT ===============
btnLogin = Button(root, text="SIGN UP", command=signup)
btnLogin.place(x=290, y=400)

# btnLogin = Button(root, text="NEW VISITOR")
# btnLogin.place(x=300, y=400)

btnLogin = Button(root, text="EXIT", command=exit)
btnLogin.place(x=290, y=450)


root.mainloop()

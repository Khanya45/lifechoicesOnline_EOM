import mysql.connector
from tkinter import ttk
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from tkinter import messagebox

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='dbLifechoicesOnline', auth_plugin='mysql_native_password')
mycursor = mydb.cursor(buffered=True)

root = Tk()
root.title("VISITOR")
root.geometry('1100x850')


# ===============Adding tabs on the window========================
tabControl = ttk.Notebook()
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="tblUser")
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="tblNextOfKin")
tabControl.pack(expan=1, fill="both")

# ==================ADDING COMPONENTS ON THE TABS==================

#  FUNCTION FOR DISPLAYING DATA ON THE WINDOW
def ViewUser():
    for i in tblUser.get_children():
        tblUser.delete(i)
    mycursor.execute("SELECT * FROM tblUser")
    rows = mycursor.fetchall()
    for row in rows:
        tblUser.insert("", tk.END, values=row)


def ViewKin():
    for i in tblNextOfKin.get_children():
        tblNextOfKin.delete(i)
    mycursor.execute("SELECT * FROM tblNextOfKin")
    rows = mycursor.fetchall()
    for row in rows:
        # print(row)
        tblNextOfKin.insert("", tk.END, values=row)


# ======================DISPLAYING TREEVIEW ON TAB2===========================
tblNextOfKin = ttk.Treeview(tab2, column=("c1", "c2", "c3", "c4"), show='headings')

sbt1 = Scrollbar(tab2, orient=VERTICAL)
sbt1.pack(side=RIGHT, fill=Y)
tblNextOfKin.config(yscrollcommand=sbt1.set)
sbt1.config(command=tblNextOfKin.yview)

tblNextOfKin.column("#1", anchor=tk.CENTER)
tblNextOfKin.heading("#1", text="NAME")
tblNextOfKin.column("#2", anchor=tk.CENTER)
tblNextOfKin.heading("#2", text="SURNAME")
tblNextOfKin.column("#3", anchor=tk.CENTER)
tblNextOfKin.heading("#3", text="MOBILE")
tblNextOfKin.column("#4", anchor=tk.CENTER)
tblNextOfKin.heading("#4", text="User_id")
tblNextOfKin.place(x=40, y=190)
btnKin = tk.Button(tab2, text="Display data", command=ViewKin)
btnKin.place(x=100, y=430)
style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

# ============================DISPLAYING TREEVIEW ON TAB1============================
tblUser = ttk.Treeview(tab1, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')
sbt2 = Scrollbar(tab1, orient=VERTICAL)
sbt2.pack(side=RIGHT, fill=Y)

tblNextOfKin.config(yscrollcommand=sbt2.set)
sbt2.config(command=tblNextOfKin.yview)

tblUser.column("#7", anchor=tk.CENTER, width=100)
tblUser.heading("#7", text="User_id")
tblUser.column("#1", anchor=tk.CENTER, width=150)
tblUser.heading("#1", text="NAME")
tblUser.column("#2", anchor=tk.CENTER, width=150)
tblUser.heading("#2", text="SURNAME")
tblUser.column("#3", anchor=tk.CENTER, width=150)
tblUser.heading("#3", text="ID NUMBER")
tblUser.column("#4", anchor=tk.CENTER, width=150)
tblUser.heading("#4", text="MOBILE")
tblUser.column("#5", anchor=tk.CENTER, width=150)
tblUser.heading("#5", text="LOGIN")
tblUser.column("#6", anchor=tk.CENTER, width=150)
tblUser.heading("#6", text="LOGOUT")
tblUser.place(x=40, y=190)
btnKin = tk.Button(tab1, text="Display data", command=ViewUser)
btnKin.place(x=100, y=430)

#  ==============================FUNCTIONS FOR ADDING DELETING AND DISPLAYING DATA IN TAB1=======================
def fetch_dataUser():
    clear()
    selected = tblUser.focus()
    temp = tblUser.item(selected, 'values')
    edtNamet1.insert(0, temp[0],)
    edtSurnamet1.insert(0, temp[1])
    edtIDt1.insert(0, temp[2])
    edtMobilet1.insert(0, temp[3])
    edtUser_idt1.insert(0, temp[6])


def delete():
    try:
        row_id = tblUser.focus()
        tblUser.delete(row_id)
        mycursor.execute('DELETE FROM tblUser WHERE ID="'+edtIDt1.get()+'"')
        mycursor.execute('DELETE FROM tblNextOfKin WHERE Mobile="'+edtMobilet2.get()+'"')
        mydb.commit()
        messagebox.showinfo("", "successfully deleted")
    except:
        messagebox.showerror("", "Failed to delete the record")


def insertUser():
    try:
        mycursor.execute('INSERT INTO tblUser (Name, Surname, ID,Mobile) VALUES ("'+edtNamet1.get()+'","'+edtSurnamet1.get()+'","'+edtIDt1.get()+'","'+edtMobilet1.get()+'")')
        tblUser.insert("", 'end', values=(edtNamet1.get(), edtSurnamet1.get(), edtIDt1.get(), edtMobilet1.get()))
        mydb.commit()
        mycursor.execute('SELECT User_id FROM tblUser WHERE ID="'+edtIDt1.get()+'"')
        row = mycursor.fetchall()
        edtUser_idt1.insert(0, row)
        messagebox.showinfo("", "Successfully added")
    except:
        messagebox.showerror("", "Failed to add the record")


def updateUser():
    try:
        selected = tblUser.focus()
        temp = tblUser.item(selected, 'values')
        tblUser.item(selected, values=(edtNamet1.get(), edtSurnamet1.get(), edtIDt1.get(), edtMobilet1.get(), temp[4], temp[5], temp[6]))
        mycursor.execute('UPDATE tblUser SET Name="'+edtNamet1.get()+'", Surname="'+edtSurnamet1.get()+'", Mobile="'+edtMobilet1.get()+'", ID="'+edtIDt1.get()+'" WHERE User_id='+edtUser_idt1.get())
        mydb.commit()
        messagebox.showinfo("", "Successfully updated")
    except:
        messagebox.showerror("", "Failed to insert")


#  ==============================FUNCTIONS FOR ADDING DELETING AND DISPLAYING DATA IN TAB2=======================



def fetch_dataKin():
    clear_kin()
    selected = tblNextOfKin.focus()
    temp = tblNextOfKin.item(selected, 'values')
    edtNamet2.insert(0, temp[0],)
    edtSurnamet2.insert(0, temp[1])
    edtMobilet2.insert(0, temp[2])
    edtUser_idt2.insert(0, temp[3])


def insertKin():
    try:
        mycursor.execute('INSERT INTO tblNextOfKin (Name, Surname,Mobile) VALUES ("'+edtNamet2.get()+'","'+edtSurnamet2.get()+'","'+edtMobilet2.get()+'")')
    # mycursor.execute('UPDATE tblNextOfKin SET User_id = (SELECT last_insert_id()) WHERE Mobile="'+edtMobilet2.get()+'"')
        mydb.commit()
        mycursor.execute('UPDATE tblNextOfKin SET User_id = (SELECT last_insert_id()) WHERE Mobile="'+edtMobilet2.get()+'"')
        mycursor.execute('SELECT User_id FROM tblNextOfKin WHERE Mobile="'+edtMobilet2.get()+'"')
        row = mycursor.fetchall()
        tblNextOfKin.insert("", 'end', values=(edtNamet2.get(), edtSurnamet2.get(), edtMobilet2.get(), row))
        messagebox.showinfo("", "Successfully added")
    except:
        messagebox.showerror("", "Failed to add")


def updateKin():
    try:
        selected = tblNextOfKin.focus()
        temp = tblNextOfKin.item(selected, 'values')
        tblNextOfKin.item(selected, values=(edtNamet2.get(), edtSurnamet2.get(), edtMobilet2.get(), temp[3]))
        mycursor.execute('UPDATE tblNextOfKin SET Name="'+edtNamet2.get()+'", Surname="'+edtSurnamet2.get()+'", Mobile="'+edtMobilet2.get()+'" WHERE User_id='+edtUser_idt2.get())
        mydb.commit()
        messagebox.showinfo("", "Successfully updated")
    except:
        messagebox.showerror("", "Failed to update")


def clear():
    edtIDt1.delete(0, END)
    edtMobilet1.delete(0, END)
    edtNamet1.delete(0, END)
    edtSurnamet1.delete(0, END)
    edtUser_idt1.delete(0, END)


def clear_kin():
    edtMobilet2.delete(0, END)
    edtNamet2.delete(0, END)
    edtSurnamet2.delete(0, END)
    edtUser_idt2.delete(0, END)


# FUNCTIONS TO COUNT AND DISPLAY THE PEOPLE WHO LOGGED IN AND LOGGED OUT
def count_in():
    edtCount_in.delete(0, END)
    count = 0
    for i in tblUser.get_children():
        tblUser.delete(i)
    mycursor.execute('SELECT * FROM tblUser WHERE logIn IS NOT NULL')
    rows = mycursor.fetchall()
    for row in rows:
        count += 1
        tblUser.insert("", tk.END, values=row)
    edtCount_in.insert(0, count)


def count_out():
    edtCount_out.delete(0, END)
    count = 0
    for i in tblUser.get_children():
        tblUser.delete(i)
    mycursor.execute('SELECT * FROM tblUser WHERE logOut IS NOT NULL')
    rows = mycursor.fetchall()
    for row in rows:
        count += 1
        tblUser.insert("", tk.END, values=row)
    edtCount_out.insert(0, count)


def absent():
    edtAbsent.delete(0, END)
    count = 0
    for i in tblUser.get_children():
        tblUser.delete(i)
    mycursor.execute('SELECT * FROM tblUser WHERE logIn IS NULL')
    rows = mycursor.fetchall()
    for row in rows:
        count += 1
        tblUser.insert("", tk.END, values=row)
    edtAbsent.insert(0, count)


def still_here():
    edtHere.delete(0, END)
    count = 0
    for i in tblUser.get_children():
        tblUser.delete(i)
    mycursor.execute('SELECT * FROM tblUser WHERE logOut IS NULL')
    rows = mycursor.fetchall()
    for row in rows:
        count += 1
        tblUser.insert("", tk.END, values=row)
    edtHere.insert(0, count)


def get_notsigned():
    mycursor.execute('SELECT Name, Surname FROM tblUser WHERE logOut IS NULL')
    people = mycursor.fetchall()
    list = []
    for person in people:
        user = f'{person[0]} {person[1]}'
        list.append(user)
    return list



def get_email():
    mycursor.execute('SELECT Email FROM tblAdmin')
    emails = mycursor.fetchone()
    return emails[0]


#  =================SENDING EMAIL TO THE ADMIN============
def send_email(email):
    try:
        sender_email_id = 'lottowinners957@gmail.com'
        receiver_email_id = email
        password = "GETRICHWITHLOTTO"
        subject = "People who have not signed out"
        msg = MIMEMultipart()
        msg['From'] = sender_email_id
        msg['To'] = receiver_email_id
        msg['Subject'] = subject
        people = ""
        for i in get_notsigned():
            people = f'{people}\n {i}'
        body = f'Dear Admin\n \n This is a list of people who have not signed out today:\n {people}'
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email_id, password)
        s.sendmail(sender_email_id, receiver_email_id, text)
        s.quit()
    except ValueError:
        messagebox.showinfo("", "Invalid email")


# send_email(get_email())


# =========================DISPLAYING IMAGE ON TAB1=====================
pic1 = Image.open("Logo-Life-Choices.jpg")
resize1 = pic1.resize((1100, 90), Image.ANTIALIAS)
logo1 = ImageTk.PhotoImage(resize1)
lbpic1 = Label(tab1, image=logo1)
lbpic1.place(x=0, y=0)

# ======================DISPLAYING IMAGE ON TAB2========================
pic2 = Image.open("Logo-Life-Choices.jpg")
resize2 = pic1.resize((1100, 90), Image.ANTIALIAS)
logo2 = ImageTk.PhotoImage(resize2)
lbpic2 = Label(tab2, image=logo2)
lbpic2.place(x=0, y=0)


#  ==========================================ADDING COMPONENTS ON A FRAME IN TAB1=================================================
lbFrame_visitor = LabelFrame(tab1, text="DATA", width=570, height=200)
lbFrame_visitor.place(x=40, y=500)
# x=240, y=520

lbNamet1 = Label(lbFrame_visitor, text="Name")
lbNamet1.place(x=10, y=20)
edtNamet1 = Entry(lbFrame_visitor)
edtNamet1.place(x=80, y=20)

lbSurnamet1 = Label(lbFrame_visitor, text="Surname")
lbSurnamet1.place(x=10, y=60)
edtSurnamet1 = Entry(lbFrame_visitor)
edtSurnamet1.place(x=80, y=60)

lbIDt1 = Label(lbFrame_visitor, text="ID number")
lbIDt1.place(x=270, y=20)
edtIDt1 = Entry(lbFrame_visitor)
edtIDt1.place(x=350, y=20)

lbMobilet1 = Label(lbFrame_visitor, text="Mobile")
lbMobilet1.place(x=270, y=60)
edtMobilet1 = Entry(lbFrame_visitor)
edtMobilet1.place(x=350, y=60)

# ==========BUTTON TO DISPLAY DATA TO ENTRIES==========
btnDisplayt1 = Button(lbFrame_visitor, text="data", command=fetch_dataUser)
btnDisplayt1.place(x=40, y=130)

# ==========BUTTON TO DELETE RECORD=================
btnDeletet1 = Button(lbFrame_visitor, text="DELETE", command=delete)
btnDeletet1.place(x=100, y=130)

# ==========BUTTON TO EDIT/UPDATE RECORD============
btnUpdatet1 = Button(lbFrame_visitor, text="UPDATE", command=updateUser)
btnUpdatet1.place(x=180, y=130)

# ==========BUTTON TO INSERT A NEW RECORD==========
btnInsertt1 = Button(lbFrame_visitor, text="INSERT", command=insertUser)
btnInsertt1.place(x=265, y=130)

btnCleart1 = Button(lbFrame_visitor, text="CLEAR", command=clear)
btnCleart1.place(x=370, y=130)

lbUser_idt1 = Label(lbFrame_visitor, text="User_id")
lbUser_idt1.place(x=10, y=100)
edtUser_idt1 = Entry(lbFrame_visitor, width=10)
edtUser_idt1.place(x=80, y=100)

# ============BUTTON TO DISPLAY PEOPLE WHO LOGGED IN AND LOGGED OUT===============
btnCheck_int1 = Button(tab1, text="LOGGED IN", command=count_in)
btnCheck_int1.place(x=220, y=430)
edtCount_in = Entry(tab1, width=5)
edtCount_in.place(x=325, y=433)

btnCheck_outt1 = Button(tab1, text="LOGGED OUT", command=count_out)
btnCheck_outt1.place(x=380, y=430)
edtCount_out = Entry(tab1, width=5)
edtCount_out.place(x=500, y=433)

btnHERE = Button(tab1, text="STILL HERE", command=still_here)
btnHERE.place(x=555, y=430)
edtHere = Entry(tab1, width=5)
edtHere.place(x=660, y=433)

btnAbsent = Button(tab1, text="ABSENT", command=absent)
btnAbsent.place(x=720, y=430)
edtAbsent = Entry(tab1, width=5)
edtAbsent.place(x=800, y=433)

#  ==========================================ADDING COMPONENTS ON A FRAME IN TAB2=================================================
lbFrame_kin = LabelFrame(tab2, text="DATA", width=570, height=200)
lbFrame_kin.place(x=40, y=500)

lbNamet2 = Label(lbFrame_kin, text="Name")
lbNamet2.place(x=10, y=20)
edtNamet2 = Entry(lbFrame_kin)
edtNamet2.place(x=80, y=20)

lbSurnamet2 = Label(lbFrame_kin, text="Surname")
lbSurnamet2.place(x=10, y=60)
edtSurnamet2 = Entry(lbFrame_kin)
edtSurnamet2.place(x=80, y=60)

lbUser_idt2 = Label(lbFrame_kin, text="User_id")
lbUser_idt2.place(x=270, y=20)
edtUser_idt2 = Entry(lbFrame_kin, width=10)
edtUser_idt2.place(x=350, y=20)


lbMobilet2 = Label(lbFrame_kin, text="Mobile")
lbMobilet2.place(x=270, y=60)
edtMobilet2 = Entry(lbFrame_kin)
edtMobilet2.place(x=350, y=60)

# ==========BUTTON TO DISPLAY DATA TO ENTRIES==========
btnDisplayt2 = Button(lbFrame_kin, text="data", command=fetch_dataKin)
btnDisplayt2.place(x=40, y=130)

# ==========BUTTON TO EDIT/UPDATE RECORD============
btnUpdatet2 = Button(lbFrame_kin, text="UPDATE", command=updateKin)
btnUpdatet2.place(x=100, y=130)

# ==========BUTTON TO INSERT A NEW RECORD==========
btnInsertt2 = Button(lbFrame_kin, text="INSERT", command=insertKin)
btnInsertt2.place(x=185, y=130)

btnCleart1 = Button(lbFrame_kin, text="CLEAR", command=clear_kin)
btnCleart1.place(x=370, y=130)


def exit():
    root.destroy()


btnExit = Button(tab1, text="EXIT", borderwidth=7, command=exit)
btnExit.place(x=370, y=740)

btnSend = Button(tab1, text="SEND EMAIL", borderwidth=5, font="Times 10", command=lambda: send_email(get_email()))
btnSend.place(x=470, y=740)


root.mainloop()

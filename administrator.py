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
root.config(bg="#141215")


# ===============================Adding tabs on the window======================================
tab_control = ttk.Notebook()
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="tblUser")
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="tblNextOfKin")
tab_control.pack(expan=1, fill="both")


# ===========================================VALIDATIONS==========================================


# VALIDATION FOR STRINGS
def is_string(name, surname):
    if name.isdigit() == False and surname.isdigit() == False:
        flag = True
    else:
        flag = False
    return flag


# VALIDATION FOR INTEGERS
def is_number(mobile):
    if mobile.isdigit() == True:
        flag = True
    else:
        flag = False
    return flag


# VALIDATION FOR LENGTH OF MOBILE
def length(mobile):
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


# ======================================================ADDING COMPONENTS ON THE TABS======================================================


# FUNCTION FOR DISPLAYING ALL DATA ON TREEVIEW
def view_user():
    for i in tblUser.get_children():
        tblUser.delete(i)
    mycursor.execute("SELECT * FROM tblUser")
    rows = mycursor.fetchall()
    for row in rows:
        tblUser.insert("", tk.END, values=row)


# ======================DISPLAYING TREEVIEW ON TAB2===========================
sb_frame2 = Frame(tab2, bg="black")
sb_frame2.place(x=130, y=180)
tblNextOfKin = ttk.Treeview(sb_frame2, selectmode="browse", column=("c1", "c2", "c3", "c4"), show='headings')
tblNextOfKin.pack(side=LEFT)
sbt1 = Scrollbar(sb_frame2, orient=VERTICAL)
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

#  FUNCTION FOR DISPLAYING DATA ON TREEVIEW
mycursor.execute("SELECT * FROM tblNextOfKin")
rows = mycursor.fetchall()
for row in rows:
    tblNextOfKin.insert("", tk.END, values=row)

# STYLING TREEVIEW
style = ttk.Style()
style.theme_use("alt")
style.map("Treeview")

style.configure("Treeview", rowheight=25)
style.map("Treeview")


# ============================DISPLAYING TREEVIEW ON TAB1============================

sb_frame = Frame(tab1, bg="black")
sb_frame.place(x=40, y=150)

tblUser = ttk.Treeview(sb_frame, selectmode="browse", column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')
tblUser.pack(side=LEFT)

sbt2 = Scrollbar(sb_frame, orient=VERTICAL)
sbt2.pack(side=RIGHT, fill=Y)
tblUser.config(yscrollcommand=sbt2.set)
sbt2.config(command=tblUser.yview)

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

btnKin = tk.Button(tab1, text="Display all", command=view_user)
btnKin.place(x=100, y=430)

#  FUNCTION FOR DISPLAYING DATA ON TREEVIEW
mycursor.execute("SELECT * FROM tblUser")
rows = mycursor.fetchall()
for row in rows:
    tblUser.insert("", tk.END, values=row)


#  =============================================FUNCTIONS FOR ALL THE BUTTONS ON THE WINDOW==============================

# FUNCTION FOR DISPLAYING SELECTED RECORD TO THE ENTRIES
def fetch_data_user():
    clear()
    try:
        selected = tblUser.focus()
        temp = tblUser.item(selected, 'values')
        edtNamet1.insert(0, temp[0],)
        edtSurnamet1.insert(0, temp[1])
        edtIDt1.insert(0, temp[2])
        edtMobilet1.insert(0, temp[3])
        edtUser_idt1.insert(0, temp[6])
    except:
        messagebox.showerror("", "Select a record then click the data button")


# FUNCTION FOR DELETING A RECORD FROM BOTH TABLES
def delete():
    if string_length(edtUser_idt1.get(), edtUser_idt1.get()) == False:
        messagebox.showerror("", "Please select a record you want to delete, then click the data button")
    else:
        try:
            mycursor.execute('DELETE FROM tblNextOfKin WHERE User_id='+edtUser_idt1.get())
            mycursor.execute('DELETE FROM tblUser WHERE User_id='+edtUser_idt1.get())
            mydb.commit()
            row_id = tblUser.focus()
            tblUser.delete(row_id)
            messagebox.showinfo("", "successfully deleted")
        except:
            messagebox.showerror("", "Failed to delete the record")


# FUNCTION FOR ADDING A NEW RECORD OF A USER
def insert_user():
    if is_string(edtNamet1.get(), edtSurnamet1.get()) == False or string_length(edtNamet1.get(), edtSurnamet1.get()) == False:
        messagebox.showerror("", "Invalid character on name or surname entry")
    elif is_number(edtMobilet1.get()) == False or length(edtMobilet1.get()) == False:
        messagebox.showerror("", "Invalid mobile number")
    else:
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


# FUNCTION FOR EDITING A RECORD OF A USER
def update_user():
    if is_string(edtNamet1.get(), edtSurnamet1.get()) == False or string_length(edtNamet1.get(), edtSurnamet1.get()) == False:
        messagebox.showerror("", "Invalid character on name or surname entry")
    elif is_number(edtMobilet1.get()) == False or length(edtMobilet1.get()) == False:
        messagebox.showerror("", "Invalid mobile number")
    else:
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


# FUNCTION FOR DISPLAYING SELECTED RECORD TO THE ENTRIES
def fetch_data_kin():
    clear_kin()
    try:
        selected = tblNextOfKin.focus()
        temp = tblNextOfKin.item(selected, 'values')
        edtNamet2.insert(0, temp[0],)
        edtSurnamet2.insert(0, temp[1])
        edtMobilet2.insert(0, temp[2])
        edtUser_idt2.insert(0, temp[3])
    except:
        messagebox.showerror("", "Select a record, then click the data button")


# FUNCTION FOR ADDING A NEXT OF KIN TO THE DATABASE
def insert_kin():
    if is_string(edtNamet2.get(), edtSurnamet2.get()) == False or string_length(edtNamet2.get(), edtSurnamet2.get()) == False:
        messagebox.showerror("", "Invalid character on name or surname entry")
    elif is_number(edtMobilet2.get()) == False or length(edtMobilet2.get()) == False:
        messagebox.showerror("", "Invalid mobile number")
    else:
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


# FUNCTION FOR EDITING A RECORD OF A NEXT OF KIN
def update_kin():
    if is_string(edtNamet2.get(), edtSurnamet2.get()) == False or string_length(edtNamet2.get(), edtSurnamet2.get()) == False:
        messagebox.showerror("", "Invalid character on name or surname entry")
    elif is_number(edtMobilet2.get()) == False or length(edtMobilet2.get()) == False:
        messagebox.showerror("", "Invalid mobile number")
    else:
        try:
            selected = tblNextOfKin.focus()
            temp = tblNextOfKin.item(selected, 'values')
            tblNextOfKin.item(selected, values=(edtNamet2.get(), edtSurnamet2.get(), edtMobilet2.get(), temp[3]))
            mycursor.execute('UPDATE tblNextOfKin SET Name="'+edtNamet2.get()+'", Surname="'+edtSurnamet2.get()+'", Mobile="'+edtMobilet2.get()+'" WHERE User_id='+edtUser_idt2.get())
            mydb.commit()
            messagebox.showinfo("", "Successfully updated")
        except:
            messagebox.showerror("", "Failed to update")


# FUNCTION FOR CLEARING ENTRIES OF THE USER FRAME ON TAB1
def clear():
    edtIDt1.delete(0, END)
    edtMobilet1.delete(0, END)
    edtNamet1.delete(0, END)
    edtSurnamet1.delete(0, END)
    edtUser_idt1.delete(0, END)


# FUNCTION FOR CLEARING ENTRIES OF THE KIN FRAME ON TAB2
def clear_kin():
    edtMobilet2.delete(0, END)
    edtNamet2.delete(0, END)
    edtSurnamet2.delete(0, END)
    edtUser_idt2.delete(0, END)


# FUNCTION FOR CLEARING ENTRIES OF THE ADMIN FRAME ON TAB2
def clear_admin():
    edtEmailf2.delete(0, END)
    edtPasswordf2.delete(0, END)
    edtSurnamef2.delete(0, END)
    edtNamef2.delete(0, END)


# ==============FUNCTIONS TO COUNT AND DISPLAY THE PEOPLE WHO LOGGED IN AND LOGGED OUT==================
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


# FUNCTION TO GET AN EMAIL OF AN ADMIN THAT LAST LOGGED IN
def get_email():
    mycursor.execute('SELECT Email FROM tblAdministrator ORDER BY logIn DESC')
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
        messagebox.showinfo("", "Successfully sent an email")
    except:
        messagebox.showinfo("", "Invalid email")


def exit():
    root.destroy()


#  FUNCTION FOR ADDING NEW ADMIN
def new_admin():
    if is_string(edtNamef2.get(), edtSurnamef2.get()) == False or string_length(edtNamef2.get(), edtSurnamef2.get()) == False:
        messagebox.showerror("", "Invalid character on name or surname entry")
    elif string_length(edtPasswordf2.get(), edtEmailf2.get()) == False:
        messagebox.showerror("", "Invalid character on name or surname entry")
    else:
        try:
            mycursor.execute('INSERT INTO tblAdministrator (Name, Surname, Password, Email) VALUES ("'+edtNamef2.get()+'","'+edtSurnamef2.get()+'","'+edtPasswordf2.get()+'","'+edtEmailf2.get()+'")')
            # mycursor.execute('DELETE FROM tblNextOfKin WHERE Name="'+edtNamef2.get()+'" AND Surname="'+edtNamef2.get()+'"')
            # mycursor.execute('DELETE FROM tblUser WHERE Name="'+edtNamef2.get()+'" AND Surname="'+edtNamef2.get()+'"')
            mydb.commit()
            messagebox.showinfo("", "Successfully added")
        except:
            messagebox.showerror("", "Failed to add the record")


# =========================DISPLAYING IMAGE ON TAB1=====================
pic1 = Image.open("Logo-Life-Choices.jpg")
resize1 = pic1.resize((1100, 120), Image.ANTIALIAS)
logo1 = ImageTk.PhotoImage(resize1)
lbpic1 = Label(tab1, image=logo1)
lbpic1.place(x=0, y=0)

# ======================DISPLAYING IMAGE ON TAB2========================
pic2 = Image.open("Logo-Life-Choices.jpg")
resize2 = pic1.resize((1100, 120), Image.ANTIALIAS)
logo2 = ImageTk.PhotoImage(resize2)
lbpic2 = Label(tab2, image=logo2)
lbpic2.place(x=0, y=0)


#  ==========================================ADDING COMPONENTS ON A FRAME IN TAB1=================================================
lbFrame_visitor = LabelFrame(tab1, text="DATA", width=570, height=200)
lbFrame_visitor.place(x=40, y=500)

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
btnDisplayt1 = Button(lbFrame_visitor, text="data", command=fetch_data_user)
btnDisplayt1.place(x=40, y=130)

# ==========BUTTON TO DELETE RECORD=================
btnDeletet1 = Button(lbFrame_visitor, text="DELETE", command=delete)
btnDeletet1.place(x=100, y=130)

# ==========BUTTON TO EDIT/UPDATE RECORD============
btnUpdatet1 = Button(lbFrame_visitor, text="UPDATE", command=update_user)
btnUpdatet1.place(x=180, y=130)

# ==========BUTTON TO INSERT A NEW RECORD==========
btnInsertt1 = Button(lbFrame_visitor, text="INSERT", command=insert_user)
btnInsertt1.place(x=265, y=130)

btnCleart1 = Button(lbFrame_visitor, text="CLEAR", command=clear)
btnCleart1.place(x=350, y=130)

lbUser_idt1 = Label(lbFrame_visitor, text="User_id")
lbUser_idt1.place(x=10, y=100)
edtUser_idt1 = Entry(lbFrame_visitor, width=10)
edtUser_idt1.place(x=80, y=100)


#  =========================FRAME2 FOR NEW ADMIN =====================
lbFrame_admin = LabelFrame(tab1, text="NEW ADMIN", width=350, height=200)
lbFrame_admin.place(x=650, y=500)

lbNamef2 = Label(lbFrame_admin, text="Name")
lbNamef2.place(x=20, y=10)
edtNamef2 = Entry(lbFrame_admin)
edtNamef2.place(x=90, y=10)

lbSurnamef2 = Label(lbFrame_admin, text="Surname")
lbSurnamef2.place(x=20, y=40)
edtSurnamef2 = Entry(lbFrame_admin)
edtSurnamef2.place(x=90, y=40)

lbEmailf2 = Label(lbFrame_admin, text="Email")
lbEmailf2.place(x=20, y=70)
edtEmailf2 = Entry(lbFrame_admin)
edtEmailf2.place(x=90, y=70)

lbPasswordf2 = Label(lbFrame_admin, text="Password")
lbPasswordf2.place(x=20, y=100)
edtPasswordf2 = Entry(lbFrame_admin)
edtPasswordf2.place(x=90, y=100)

btnGrant = Button(lbFrame_admin, text="Add as admin", command=new_admin)
btnGrant.place(x=70, y=140)

btnClearf2 = Button(lbFrame_admin, text="CLEAR", command=clear_admin)
btnClearf2.place(x=200, y=140)


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
lbFrame_kin.place(x=220, y=500)

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
btnDisplayt2 = Button(lbFrame_kin, text="data", command=fetch_data_kin)
btnDisplayt2.place(x=95, y=130)

# ==========BUTTON TO EDIT/UPDATE RECORD============
btnUpdatet2 = Button(lbFrame_kin, text="UPDATE", command=update_kin)
btnUpdatet2.place(x=155, y=130)

# ==========BUTTON TO INSERT A NEW RECORD==========
btnInsertt2 = Button(lbFrame_kin, text="INSERT", command=insert_kin)
btnInsertt2.place(x=240, y=130)

btnCleart1 = Button(lbFrame_kin, text="CLEAR", command=clear_kin)
btnCleart1.place(x=320, y=130)

btnExit = Button(tab1, text="EXIT", borderwidth=7, command=exit)
btnExit.place(x=370, y=740)

btnSend = Button(tab1, text="SEND EMAIL", borderwidth=5, font="Times 10", command=lambda: send_email(get_email()))
btnSend.place(x=470, y=740)

messagebox.showinfo("IMPORTANT!!!", "Please select a record on the database, then click the data button. And remember to do the same thing on the second tab")


root.mainloop()

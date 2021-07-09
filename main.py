from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("MAIN")
root.geometry('550x500')

pic1 = Image.open("Logo-Life-Choices.jpg")
resize = pic1.resize((550, 90), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(resize)
lbpic = Label(root, image=logo, bg='black')
lbpic.place(x=0, y=0)

pic2 = Image.open("lifechoices.png")
resize2 = pic2.resize((550, 500), Image.ANTIALIAS)
logo2 = ImageTk.PhotoImage(resize2)
lbpic2 = Label(root, image=logo2, bg='black')
lbpic2.place(x=0, y=90)



def admin():
    root.destroy()
    import Admin


def visitor():
    root.destroy()
    import user_login


btnAdmin = Button(root, text="ADMINISTRATOR", width=20, height=5, font="TIMES 15", command=admin, bg="#141215", fg="white")
# btnAdmin.bind("<Control-a>", admin)
btnAdmin.place(x=40, y=220)

btnUser = Button(root, text="LS VISITOR", width=20, height=5, font="TIMES 15", command=visitor, bg="#141215", fg="white")
btnUser.place(x=300, y=220)



root.mainloop()

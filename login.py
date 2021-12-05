from tkinter import * 
from tkinter import ttk 
from user import user_window
from PIL import Image,ImageTk
import mysql.connector
from logging import NullHandler
from tkinter import messagebox
from room import room_booking
from view import view_booking
from cancel import cancel_booking
from home import classroombookingsystem

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1550x800+0+0")




        img1=Image.open("F:\code\oops_project\muj.jpg")
        img1=img1.resize((1550,740),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=740)


        frame1 = Frame(root,bg="white")
        root.config(bg="lightgray")



        frame1.place(x=530,y=150,width=500,height=500)
        Label(frame1,text="LOGIN" , font=("times 30 bold"),bg="white",fg="black").place(x=180,y=20)

        #label
        type_user = Label(frame1,text="User Type",font=("times 18 bold"),bg="white",fg="black")
        type_user.place(x=20,y=100)
        id_user = Label(frame1,text="User Id",font=("times 18 bold"),bg="white",fg="black")
        id_user.place(x=20,y=175)
        pass_user = Label(frame1,text = "Password",font=("times 18 bold"),bg="white",fg="black")
        pass_user.place(x=20,y=250)


        type_val = StringVar()
        id_val = StringVar()
        pass_val = StringVar()

        self.mycombo = ttk.Combobox(frame1,textvariable=type_val,font=("times 18 bold"),width=20,state="read")
        self.mycombo['values'] = ["Student","Faculty"]
        self.mycombo.current()
        self.mycombo.place(x=140,y=100)



        self.pass_box = Entry(frame1,textvariable=pass_val,font=("times 18 bold"),bg="lightgray",fg="black",width=22)
        self.pass_box.place(x=140,y=175)

        self.id_box = Entry(frame1,textvariable=id_val,font=("times 18 bold"),bg="lightgray",fg="black",width=22)
        self.id_box.place(x=140,y=250)

        login=Button(text="Submit",command=self.login,font=("times 16 bold"),bg="red",fg="black").place(x=580,y=505,width=400)


    def login(self):
        if self.id_box.get()=="" or self.pass_box.get()=="":
            messagebox.showerror("Error","Please fill all the fields")
            
        

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="saymyname@2",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from registered where IDNumber=%s and pass=%s",(self.id_box.get(),
                                                                                    self.pass_box.get(),))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                self.new_window=Toplevel(self.root)
                self.app=classroombookingsystem(self.new_window)
            conn.commit()
            conn.close


            

        









if __name__=="__main__":
    root=Tk()
    obj=login_window(root)
    root.mainloop()
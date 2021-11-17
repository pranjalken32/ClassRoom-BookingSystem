from tkinter import *
from PIL import Image,ImageTk


class classroombookingsystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Classroom Booking System")
        self.root.geometry("1550x800+0+0")

#================= 1st Image============#
        img1=Image.open("muj.jpg")
        img1=img1.resize((1550,145),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=145)


#================= 2nd Image============#
        img2=Image.open("logo.png")
        img2=img2.resize((210,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=240,height=140)
        
#================= Titile============#
        lbl_title=Label(self.root,text=" ClassRoom Booking System", font=("times new roman",30,"bold"),bg="black",fg="orange",bd=4,relief=RIDGE)
        lbl_title.place(x=-50,y=130,width=1550,height=70)

#============= main frame============#
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

#=========== menu========#
        lbl_menu=Label(main_frame,text="Portal", font=("times new roman",30,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=240,height=50)
#========= button Frame=======
        lbl_frame=Frame(main_frame,bd=0,relief=RIDGE)
        lbl_frame.place(x=0,y=50,width=240,height=300)

        user_btn=Button(lbl_frame,text="User Details",width=16,font=("times new roman",20,"bold"),bg="grey",fg="gold",bd=4,relief=RIDGE)
        user_btn.grid(row=0,column=0,pady=1)

        rm_btn=Button(lbl_frame,text="Room Booking",width=16,font=("times new roman",20,"bold"),bg="grey",fg="gold",bd=4,relief=RIDGE)
        rm_btn.grid(row=1,column=0,pady=1)

        v_btn=Button(lbl_frame,text="View",width=16,font=("times new roman",20,"bold"),bg="grey",fg="gold",bd=4,relief=RIDGE)
        v_btn.grid(row=2,column=0,pady=1)

        extra_btn=Button(lbl_frame,text="Extra",width=16,font=("times new roman",20,"bold"),bg="grey",fg="gold",bd=4,relief=RIDGE)
        extra_btn.grid(row=4,column=0,pady=1)

        logout_btn=Button(lbl_frame,text="Log Out",width=16,font=("times new roman",20,"bold"),bg="grey",fg="gold",bd=4,relief=RIDGE)
        logout_btn.grid(row=3,column=0,pady=1)


#========== nind aarha bhai=====####
        img3=Image.open("class.jpg")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        
        lblimg=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=240,y=190,width=1200,height=590)

        img4=Image.open("the-batman.jpg")
        img4=img4.resize((210,190),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        
        lblimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=350,width=240,height=290)

if __name__ == "__main__":
    root=Tk()
    obj=classroombookingsystem(root)
    root.mainloop()

        
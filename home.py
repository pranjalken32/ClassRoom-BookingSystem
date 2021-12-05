from tkinter import * 
from user import user_window
from PIL import Image,ImageTk
from room import room_booking
from view import view_booking
from cancel import cancel_booking


class classroombookingsystem:
        def __init__(self,root):
                self.root=root
                self.root.title("Classroom Booking System")
                self.root.geometry("1550x800+0+0")
                
    

#================= 1st Image============#
                img1=Image.open("F:\code\oops_project\muj.jpg")
                img1=img1.resize((1550,240),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
                lblimg.place(x=0,y=0,width=1550,height=240)


#================= 2nd Image============#
                img2=Image.open("logo.png")
                img2=img2.resize((220,180),Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(img2)

                lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
                lblimg.place(x=0,y=0,width=242,height=200)
        
#================= Titile============#
               # lbl_title=Label(self.root,text=" ClassRoom Booking System", font=("times new roman",30,"bold"),bg="black",fg="orange",bd=4,relief=RIDGE)
                #lbl_title.place(x=-50,y=130,width=1550,height=70)

#============= main frame============#
                main_frame=Frame(self.root,bd=4,relief=RIDGE)
                main_frame.place(x=0,y=190,width=1550,height=620)

#=========== menu========#
                lbl_menu=Label(main_frame,text="Portal", font=("Sans serif",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
                lbl_menu.place(x=0,y=0,width=240,height=55)
#========= button Frame=======
                lbl_frame=Frame(main_frame,bd=0,relief=RIDGE)
                lbl_frame.place(x=0,y=50,width=240,height=370)

                user_btn=Button(lbl_frame,text="User Details",command=self.user_details,width=22,font=("Comic Sans MS",15, "bold"),bg="white",fg="black",bd=4,relief=FLAT, justify="center", activebackground="grey")
                user_btn.grid(row=0,column=0,pady=1)

                rm_btn=Button(lbl_frame,text="Book Room",command=self.room_details,width=22,font=("Comic Sans MS",15, "bold"),bg="white",fg="black",bd=4,relief=FLAT, justify="center", activebackground="grey")
                rm_btn.grid(row=1,column=0,pady=1,padx=0)

                v_btn=Button(lbl_frame,text="View Details",command=self.view_booking,width=22,font=("Comic Sans MS",15, "bold"),bg="white",fg="black",bd=4,relief=FLAT, justify="center", activebackground="grey")
                v_btn.grid(row=2,column=0,pady=1)

                cancel_btn=Button(lbl_frame,text="Cancel Booking",command=self.cancel_booking,width=22,font=("Comic Sans MS",15, "bold"),bg="white",fg="black",bd=4,relief=FLAT, justify="center", activebackground="grey")
                cancel_btn.grid(row=3,column=0,pady=1)

                logout_btn=Button(lbl_frame,text="Log Out",command=self.logout,width=22,font=("Comic Sans MS",15, "bold"),bg="white",fg="black",bd=4,relief=FLAT, justify="center", activebackground="grey")
                logout_btn.grid(row=4,column=0,pady=1)


#========== nind aarha bhai=====####
                img3=Image.open("plainbackgrounds.png")
                img3=img3.resize((1310,590),Image.ANTIALIAS)
                self.photoimg3=ImageTk.PhotoImage(img3)

        
                lblimg=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
                lblimg.place(x=240,y=190,width=1200,height=590)

                #img4=Image.open("the-batman.jpg")
                #img4=img4.resize((210,190),Image.ANTIALIAS)
                #self.photoimg4=ImageTk.PhotoImage(img4)

        
                #lblimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
                #lblimg.place(x=0,y=350,width=240,height=290) 
        def user_details(self):
           self.new_window= Toplevel(self.root) 
           self.app=user_window(self.new_window) 

        def room_details(self):
                self.new_window= Toplevel(self.root) 
                self.app=room_booking(self.new_window) 
        
        def view_booking(self):
                self.new_window= Toplevel(self.root) 
                self.app=view_booking(self.new_window)

        def cancel_booking(self):
                self.new_window=Toplevel(self.root)
                self.app=cancel_booking(self.new_window)

        def logout(self):
                self.root.destroy()
           

if __name__ == "__main__":
        root=Tk()
        obj=classroombookingsystem(root)
        root.mainloop()
        
from logging import NullHandler
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import calendar
class cancel_booking:
        def __init__(self,root):
                self.root=root
                self.root.title("Classroom Booking System")
                self.root.geometry("1280x550+245+220")


                self.var_id=StringVar()
                self.var_slot=StringVar()
                self.var_room=StringVar()
                self.var_type=StringVar()
                self.var_day=StringVar()




                lbl_title=Label(self.root,text="ClassRoom Booking", font=("Comic Sans MS",15, "bold"),bg="white",fg="black",bd=4,relief=FLAT, justify="center", activebackground="grey")
                lbl_title.place(x=-30,y=0,width=1380,height=50)


                lblframeleft=LabelFrame(self.root, text="Cancel Booking :",padx=2,pady=10, font=("Comic Sans MS",30, "bold"),bg="grey",fg="black",bd=2,relief=FLAT)
                lblframeleft.place(x=0,y=60,width=625,height=490)

               


                







                lbl_id=Label(lblframeleft,padx=4,pady=8,text="Id Number",font=("Comic Sans MS",20),bg="grey",bd=4)
                lbl_id.grid(row=0,column=0,sticky=W,pady=3)

                id=ttk.Entry(lblframeleft,textvariable=self.var_id,width=26,font=("Comic Sans MS",15))
                id.grid(row=0,column=1,sticky=W)


                lbl_day=Label(lblframeleft,padx=2,pady=8,text="Day",font=("Comic Sans MS",20,),bg="grey",bd=4)
                lbl_day.grid(row=4,column=0,sticky=W)

                combo_day=ttk.Combobox(lblframeleft,textvariable=self.var_day,font=("Comic Sans MS",15),width=25,state="read")
                combo_day["value"]=("Monday","Tuesday","Wednesday","Thursday","Friday")
                combo_day.current()
                combo_day.grid(row=4,column=1,sticky=W,pady=3)



                lbl_room_sc=Label(lblframeleft,padx=2,pady=8,text="Room Type",font=("Comic Sans MS",20, ),bg="grey",bd=4)
                lbl_room_sc.grid(row=2,column=0,sticky=W)

                combo_room_sc=ttk.Combobox(lblframeleft,textvariable=self.var_type,font=("Comic Sans MS",15),width=25,state="read")
                combo_room_sc["value"]=("Projector","Capacity>50","Capacity<50")
                combo_room_sc.current()
                combo_room_sc.grid(row=2,column=1,sticky=W,pady=3)
                #available room
                lbl_room_av=Label(lblframeleft,padx=2,pady=8,text="Room No",font=("Comic Sans MS",20, ),bg="grey",bd=4)
                lbl_room_av.grid(row=3,column=0,sticky=W)

                combo_room_av=ttk.Combobox(lblframeleft,textvariable=self.var_room,font=("Comic Sans MS",15),width=25,state="read")
                combo_room_av["value"]=("100","101","102","103","104","105","200","201","202","203","204","205")
                combo_room_av.current()
                combo_room_av.grid(row=3,column=1,sticky=W,pady=3)


                #time slot

                lbl_room_av=Label(lblframeleft,padx=2,pady=8,text="Time Slot",font=("Comic Sans MS",20, ),bg="grey",bd=4)
                lbl_room_av.grid(row=1,column=0,sticky=W)

                combo_room_av=ttk.Combobox(lblframeleft,textvariable=self.var_slot,font=("Comic Sans MS",15),width=25,state="read")
                combo_room_av["value"]=("09:00-09:45","09:40-10:35","10:40-11:25","11:30-12:15","12:20-13:05","13:05-13:50","13:55-14:40","14:45-15:30","15:35-16:20","16:25-17:00","17:15-18:00")
                combo_room_av.current()
                combo_room_av.grid(row=1,column=1,sticky=W,pady=3)



                btn_frame11= Frame(lblframeleft,bd=2,relief=FLAT)
                btn_frame11.place(x=-10,y=330,width=660,height=80)


                btnAdd1=Button(btn_frame11,width=20,command=self.mdelete,text="Cancel",font=("Comic Sans MS",15),bg="red",fg="white",relief=FLAT, justify="center", activebackground="grey")
                btnAdd1.grid(row=0,column=4,padx=175)




        def mdelete(self):
                mdelete=messagebox.askyesno("Delete","Do you want to cancel this Booking",parent=self.root)
                if mdelete>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="saymyname@2",database="management")
                        my_cursor=conn.cursor()
                        query="delete from room101 where IDNumber=%s and Timeslot=%s and roomno=%s"
                        value=(self.var_id.get(),self.var_slot.get(),self.var_room.get(),)
                        my_cursor.execute(query,value)
                else:
                        if not mdelete:
                                        return
                conn.commit()
                conn.close()








if __name__ == "__main__":
    root=Tk()
    obj=cancel_booking(root)
    root.mainloop()
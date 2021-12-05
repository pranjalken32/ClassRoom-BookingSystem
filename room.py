from logging import NullHandler
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import calendar


class room_booking:
        def __init__(self,root):
                self.root=root
                self.root.title("Classroom Booking System")
                self.root.geometry("1280x550+245+220")


                #variables
                self.var_id=StringVar()
                self.var_slot=StringVar()
                self.var_room=StringVar()
                self.var_type=StringVar()
                self.var_day=StringVar()



                #title frame
                lbl_title=Label(self.root,text="ClassRoom Booking", font=("Comic Sans MS",15, "bold"),bg="white",fg="black",bd=4,relief=FLAT, justify="center", activebackground="grey")
                lbl_title.place(x=-30,y=0,width=1380,height=50)


                lblframeleft=LabelFrame(self.root, text=" Room Details :",padx=2,pady=10, font=("Comic Sans MS",30, "bold"),bg="grey",fg="black",bd=2,relief=FLAT)
                lblframeleft.place(x=0,y=60,width=625,height=490)



                #room booking
                 # labels and frames
                lbl_id=Label(lblframeleft,padx=4,pady=8,text="Id Number",font=("Comic Sans MS",20),bg="grey",bd=4)
                lbl_id.grid(row=0,column=0,sticky=W,pady=3)

                id=ttk.Entry(lblframeleft,textvariable=self.var_id,width=26,font=("Comic Sans MS",15))
                id.grid(row=0,column=1,sticky=W)

                #date of booking
                #lbl_book=Label(lblframeleft,padx=2,pady=10,text="Purpose",font=("Comic Sans MS",15),bg="grey",bd=4)
                #lbl_book.grid(row=1,column=0,sticky=W,pady=3)

                #txt_book=ttk.Entry(lblframeleft,width=20,font=("Comic Sans MS",15))
                #txt_book.grid(row=1,column=1)


                #day of booking
                lbl_day=Label(lblframeleft,padx=2,pady=8,text="Day",font=("Comic Sans MS",20,),bg="grey",bd=4)
                lbl_day.grid(row=4,column=0,sticky=W)

                combo_day=ttk.Combobox(lblframeleft,textvariable=self.var_day,font=("Comic Sans MS",15),width=25,state="read")
                combo_day["value"]=("Monday","Tuesday","Wednesday","Thursday","Friday")
                combo_day.current()
                combo_day.grid(row=4,column=1,sticky=W,pady=3)


                #room booking
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


                #fetch data
                btn_fetch= Frame(lblframeleft,bd=2,relief=FLAT)
                btn_fetch.place(x=365,y=-40,width=110,height=35)


                btnAdd=Button(btn_fetch,command=self.fetch_id,width=13,text="Get",font=("Comic Sans MS",12),bg="white",fg="black",relief=FLAT,justify="center", activebackground="grey")
                btnAdd.grid(row=0,column=0)

                #buttons
                btn_frame11= Frame(lblframeleft,bd=2,relief=FLAT)
                btn_frame11.place(x=-10,y=330,width=660,height=80)


                btnAdd1=Button(btn_frame11,width=20,command=self.add_data,text="Book",font=("Comic Sans MS",15),bg="green",fg="white",relief=FLAT, justify="center", activebackground="grey")
                btnAdd1.grid(row=0,column=4,padx=175)

             


                #table frame search system
                
                #Table_Frame=LabelFrame(self.root,bd=2,relief=FLAT,text="View Details and Search",font=("Comic Sans MS",20),bg="grey",fg="black")
                #Table_Frame.place(x=428,y=200,width=725,height=290)

                #btn_search=Button(Table_Frame,width=7,bd=4,text="Search By",font=("Comic Sans MS",10),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                #btn_search.grid(row=0,column=0,padx=2,pady=2)

                #self.search_var=StringVar()
                #combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("Comic Sans MS",15),width=15,state="read")
                #combo_search["value"]=("Room")
                #combo_search.current()
                #combo_search.grid(row=0,column=1,sticky=W,pady=5,padx=2)


                #self.txt_search=StringVar()
                #txtse=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=20,font=("Comic Sans MS",15))
                #txtse.grid(row=0,column=3,sticky=W,pady=5,padx=2)

                #btnsearch=Button(Table_Frame,width=7,bd=4,text="Search",font=("Comic Sans MS",10),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                #btnsearch.grid(row=0,column=4,padx=2,pady=2)

                #btn_show=Button(Table_Frame,width=7,bd=4,text="Show all",font=("Comic Sans MS",10),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                #btn_show.grid(row=0,column=5,padx=2,pady=2)


                #details_table=Frame(Table_Frame, bd=4,relief=FLAT)
                #details_table.place(x=10,y=60,width=650,height=180)


                #scrollbar
                #scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
                #scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)


                #table

                #self.User_Details_Table=ttk.Treeview(details_table,columns=("Id","slot","Room","room type","day"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                #scroll_x.pack(side=BOTTOM,fill=X)
                #scroll_y.pack(side=RIGHT,fill=Y)

                #scroll_x.config(command=self.User_Details_Table.xview)
                #scroll_y.config(command=self.User_Details_Table.yview)

                ##heading 

               # self.User_Details_Table.heading("slot",text="Time slot")
                #self.User_Details_Table.heading("Room",text="Room Type")
                #self.User_Details_Table.heading("room type",text="Room")
                #self.User_Details_Table.heading("day",text="Day")
                

               # self.User_Details_Table["show"]="headings"
                #self.User_Details_Table.pack(fill=BOTH,expand=1)
                
                #adjust width
                #self.User_Details_Table.column("Id",width=100)
                #self.User_Details_Table.column("slot",width=100)
                #self.User_Details_Table.column("Room",width=100)
                #self.User_Details_Table.column("room type",width=100)
                #self.User_Details_Table.column("day",width=100)

                #self.User_Details_Table.pack(fill=BOTH,expand=1)
                #self.fetch_data()
        #add data


        def add_data(self):
                if self.var_id.get()=="" or self.var_room.get()=="" or self.var_day.get()=="":
                        messagebox.showerror("Error","Please Fill All the Details")
                else:
                        try:
                                
                                
                
                                conn=mysql.connector.connect(host="localhost",username="root",password="saymyname@2",database="management")
                                my_cursor=conn.cursor()

                                
                                my_cursor.execute("insert into room101 values(%s,%s,%s,%s,%s)",(
                                                                                        self.var_id.get(),
                                                                                        self.var_slot.get(),
                                                                                        self.var_type.get(),
                                                                                        self.var_room.get(),
                                                                                        self.var_day.get()))
                                conn.commit()
                                
                                conn.close()
                                messagebox.showinfo("Success","Room Booked",parent=self.root)
                                

                                
                        except Exception as es:
                                messagebox.showwarning("Warning",f"Room Already Booked:{str(es)}",parent=self.root)
        # data fetch
        def fetch_id(self):
                if self.var_id.get()=="":
                        messagebox.showerror("Error","Please Enter Id Number",parent=self.root)
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="saymyname@2",database="management")
                        my_cursor=conn.cursor()
                        query=("select Name from user where IDNumber=%s")
                        value=(self.var_id.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()


                        if row == None:
                                messagebox.showerror("Error","Invalid ID Number",parent=self.root)

                        else:
                                conn.commit()
                                conn.close()
                                showDataframe=Frame(self.root,bd=4,relief=FLAT,padx=2)
                                showDataframe.place(x=655,y=80,width=600,height=600)

                                lblname=Label(showDataframe,text="Name",font=("Comic Sans MS",20))
                                lblname.place(x=0,y=0)

                                lblname=Label(showDataframe,text=row,font=("Comic Sans MS",20))
                                lblname.place(x=200,y=0)
                                conn=mysql.connector.connect(host="localhost",username="root",password="saymyname@2",database="management")
                                
                                my_cursor=conn.cursor()
                                query=("select UserType from user where IDNumber=%s")
                                value=(self.var_id.get(),)
                                my_cursor.execute(query,value)
                                row=my_cursor.fetchone()

                                lbltype=Label(showDataframe,text="User Type",font=("Comic Sans MS",20))
                                lbltype.place(x=0,y=50)

                                lbltype=Label(showDataframe,text=row,font=("Comic Sans MS",20))
                                lbltype.place(x=200,y=50)


                                conn=mysql.connector.connect(host="localhost",username="root",password="saymyname@2",database="management")
                                
                                my_cursor=conn.cursor()
                                query=("select OutlookID from user where IDNumber=%s")
                                value=(self.var_id.get(),)
                                my_cursor.execute(query,value)
                                row=my_cursor.fetchone()

                                lblemail=Label(showDataframe,text="Outlook ID",font=("Comic Sans MS",20))
                                lblemail.place(x=0,y=100)

                                lblemail=Label(showDataframe,text=row,font=("Comic Sans MS",12))
                                lblemail.place(x=170,y=100)


                                conn=mysql.connector.connect(host="localhost",username="root",password="saymyname@2",database="management")
                                
                                my_cursor=conn.cursor()
                                query=("select Gender from user where IDNumber=%s")
                                value=(self.var_id.get(),)
                                my_cursor.execute(query,value)
                                row=my_cursor.fetchone()

                                lblgender=Label(showDataframe,text="Gender",font=("Comic Sans MS",20))
                                lblgender.place(x=0,y=150)

                                lblgender=Label(showDataframe,text=row,font=("Comic Sans MS",20))
                                lblgender.place(x=200,y=150)



                                self.fetch_data()
        
        #fetch data
        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="saymyname@2",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("select *from room101")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.User_Details_Table.delete(*self.User_Details_Table.get_children())
                        for i in rows:
                                self.User_Details_Table.insert("",END,values=i)
                        conn.commit()
                conn.close()











if __name__ == "__main__":
    root=Tk()
    obj=room_booking(root)
    root.mainloop()

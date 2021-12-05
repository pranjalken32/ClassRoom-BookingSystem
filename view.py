from logging import NullHandler
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class view_booking:
        def __init__(self,root):
                self.root=root
                self.root.title("Classroom Booking System")
                self.root.geometry("1280x550+245+220")


                


                Table_Frame=LabelFrame(self.root,bd=2,relief=FLAT,text="View Details and Search",font=("Comic Sans MS",20),bg="grey",fg="black")
                Table_Frame.place(x=20,y=20,width=1225,height=790)

                btn_search=Button(Table_Frame,width=7,bd=4,text="Search By",font=("Comic Sans MS",10),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btn_search.grid(row=0,column=0,padx=2,pady=2)

                self.search_var=StringVar()
                combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("Comic Sans MS",15),width=15,state="read")
                combo_search["value"]=("Room")
                combo_search.current()
                combo_search.grid(row=0,column=1,sticky=W,pady=5,padx=2)


                self.txt_search=StringVar()
                txtse=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=20,font=("Comic Sans MS",15))
                txtse.grid(row=0,column=3,sticky=W,pady=5,padx=2)


                #label frame
                lbl_title=Label(self.root,text="ClassRoom Booking", font=("Comic Sans MS",15, "bold"),bg="white",fg="black",bd=4,relief=FLAT, justify="center", activebackground="grey")
                lbl_title.place(x=-30,y=0,width=1380,height=50)


                

                btnsearch=Button(Table_Frame,width=7,bd=4,text="Search",font=("Comic Sans MS",10),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btnsearch.grid(row=0,column=4,padx=2,pady=2)

                btn_show=Button(Table_Frame,width=7,bd=4,text="Show all",font=("Comic Sans MS",10),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btn_show.grid(row=0,column=5,padx=2,pady=2)


                details_table=Frame(Table_Frame, bd=4,relief=FLAT)
                details_table.place(x=0,y=60,width=1050,height=350)


                #scrollbar
                scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)


                #table

                self.User_Details_Table=ttk.Treeview(details_table,columns=("Id","slot","Room","room type","day"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.User_Details_Table.xview)
                scroll_y.config(command=self.User_Details_Table.yview)

                ##heading 

                self.User_Details_Table.heading("Id",text="Id Number")
                self.User_Details_Table.heading("slot",text="Time slot")
                self.User_Details_Table.heading("Room",text="Room Type")
                self.User_Details_Table.heading("room type",text="Room")
                self.User_Details_Table.heading("day",text="Day")
                

                self.User_Details_Table["show"]="headings"
                self.User_Details_Table.pack(fill=BOTH,expand=1)
                
                #adjust width
                self.User_Details_Table.column("Id",width=100)
                self.User_Details_Table.column("slot",width=100)
                self.User_Details_Table.column("Room",width=100)
                self.User_Details_Table.column("room type",width=100)
                self.User_Details_Table.column("day",width=100)

                self.User_Details_Table.pack(fill=BOTH,expand=1)
                self.fetch_data()


                #search button
                btn_search1=Button(Table_Frame,width=7,bd=4,text="Search By",font=("Comic Sans MS",10),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btn_search1.grid(row=0,column=0,padx=2,pady=2)

                self.search_var=StringVar()
                combo_search1=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("Comic Sans MS",15),width=15,state="read")
                combo_search1["value"]=("IDNumber",)
                combo_search1.current()
                combo_search1.grid(row=0,column=1,sticky=W,pady=5,padx=2)


                self.txt_search1=StringVar()
                txtse1=ttk.Entry(Table_Frame,textvariable=self.txt_search1,width=20,font=("Comic Sans MS",15))
                txtse1.grid(row=0,column=3,sticky=W,pady=5,padx=2)

                btnsearch1=Button(Table_Frame,command=self.search_new,width=7,bd=4,text="Search",font=("Comic Sans MS",10),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btnsearch1.grid(row=0,column=4,padx=2,pady=2)

                btn_show1=Button(Table_Frame,command=self.fetch_data,width=7,bd=4,text="Show all",font=("Comic Sans MS",10),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btn_show1.grid(row=0,column=5,padx=2,pady=2)

        def fetch_id(self):
                if self.var_id.get()=="":
                        messagebox.showerror("Error","Please enter Id Number",parent=self.root)
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="saymyname@2",database="management")
                        my_cursor=conn.cursor()
                        query=("select Name from user where IDNumber=%s")
                        value=(self.var_id.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()


                        if row == None:
                                messagebox.showerror("Error","Invalid Number",parent=self.root)

                        else:
                                conn.commit()
                                conn.close()
                                showDataframe=Frame(self.root,bd=4,relief=FLAT,padx=2)
                                showDataframe.place(x=455,y=80,width=400,height=100)

                                lblname=Label(showDataframe,text="Name",font=("Comic Sans MS",10))
                                lblname.place(x=0,y=0)

                                lblname=Label(showDataframe,text=row,font=("Comic Sans MS",10))
                                lblname.place(x=90,y=0)
                                conn=mysql.connector.connect(host="localhost",username="root",password="saymyname@2",database="management")
                                
                                my_cursor=conn.cursor()
                                query=("select UserType from user where IDNumber=%s")
                                value=(self.var_id.get(),)
                                my_cursor.execute(query,value)
                                row=my_cursor.fetchone()

                                lbltype=Label(showDataframe,text="User Type",font=("Comic Sans MS",10))
                                lbltype.place(x=0,y=30)

                                lbltype=Label(showDataframe,text=row,font=("Comic Sans MS",10))
                                lbltype.place(x=90,y=30)


                                conn=mysql.connector.connect(host="localhost",username="root",password="saymyname@2",database="management")
                                
                                my_cursor=conn.cursor()
                                query=("select OutlookID from user where IDNumber=%s")
                                value=(self.var_id.get(),)
                                my_cursor.execute(query,value)
                                row=my_cursor.fetchone()

                                lblemail=Label(showDataframe,text="Outlook ID",font=("Comic Sans MS",10))
                                lblemail.place(x=0,y=60)

                                lblemail=Label(showDataframe,text=row,font=("Comic Sans MS",10))
                                lblemail.place(x=90,y=60)


                                self.fetch_data()



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


        def search_new(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="saymyname@2",database="management")
                my_cursor=conn.cursor()

                my_cursor.execute("select * from room101 where "+ str(self.search_var.get())+" LIKE '%"+str(self.txt_search1.get())+"%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.User_Details_Table.delete(*self.User_Details_Table.get_children())
                        for i in rows:
                                self.User_Details_Table.insert("",END,values=i)
                        conn.commit()
                conn.close()
        



if __name__ == "__main__":
    root=Tk()
    obj=view_booking(root)
    root.mainloop()
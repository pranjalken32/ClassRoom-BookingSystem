from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class user_window:
        def __init__(self,root):
                self.root=root
                self.root.title("Classroom Booking System")
                self.root.geometry("1280x550+245+220")




        #variables for database
                self.var_utype=StringVar()
                self.var_uid=StringVar()
                self.var_uname=StringVar()
                self.var_uemail=StringVar()
                self.var_ugender=StringVar()



#======================== title ==============#


                lbl_title=Label(self.root,text="ADD User Details", font=("Comic Sans MS",15, "bold"),bg="white",fg="black",bd=4,relief=FLAT, justify="center", activebackground="grey")
                lbl_title.place(x=-30,y=0,width=1380,height=50)
                #img3=Image.open("class.jpg")
                #img3=img3.resize((1310,590),Image.ANTIALIAS)
                #self.photoimg3=ImageTk.PhotoImage(img3)
                lblframeleft=LabelFrame(self.root, text=" User Details :",padx=2,pady=10, font=("Comic Sans MS",20, "bold"),bg="grey",fg="black",bd=2,relief=FLAT)
                lblframeleft.place(x=0,y=60,width=425,height=490)


#label and entry
        #user type
                lbl_user_type=Label(lblframeleft,padx=2,pady=10,text="User Type",font=("Comic Sans MS",15, ),bg="grey",bd=4)
                lbl_user_type.grid(row=0,column=0,sticky=W)

                combo_user=ttk.Combobox(lblframeleft,textvariable=self.var_utype,font=("Comic Sans MS",15),width=19,state="read")
                combo_user["value"]=("Faculty","Student")
                combo_user.current()
                combo_user.grid(row=0,column=1,sticky=W,pady=3)


                #User id type
                lbl_user_id=Label(lblframeleft,padx=2,pady=10,text="Id",font=("Comic Sans MS",15),bg="grey",bd=4)
                lbl_user_id.grid(row=1,column=0,sticky=W,pady=3)

                txtid=ttk.Entry(lblframeleft,textvariable=self.var_uid,width=20,font=("Comic Sans MS",15))
                txtid.grid(row=1,column=1)



                #user name
                lbl_user_name=Label(lblframeleft,padx=2,pady=10,text="User Name",font=("Comic Sans MS",15),bg="grey",bd=4)
                lbl_user_name.grid(row=2,column=0,sticky=W,pady=3)

                txtuname=ttk.Entry(lblframeleft,textvariable=self.var_uname,width=20,font=("Comic Sans MS",15))
                txtuname.grid(row=2,column=1)

                #email
                
                lbl_email=Label(lblframeleft,padx=2,pady=10,text="Outlook Id",font=("Comic Sans MS",15),bg="grey",bd=4)
                lbl_email.grid(row=3,column=0,sticky=W,pady=3)

                email=ttk.Entry(lblframeleft,textvariable=self.var_uemail,width=20,font=("Comic Sans MS",15))
                email.grid(row=3,column=1)

                #gender
                lbl_gender=Label(lblframeleft,padx=2,pady=10,text="Gender",font=("Comic Sans MS",15),bg="grey",bd=4)
                lbl_gender.grid(row=4,column=0,sticky=W,pady=3)

                combo_gender=ttk.Combobox(lblframeleft,textvariable=self.var_ugender,font=("Comic Sans MS",15),width=19,state="read")
                combo_gender["value"]=("Male","Female","Others")
                combo_gender.current()
                combo_gender.grid(row=4,column=1,sticky=W,pady=3)

                # btn 

                btn_frame1= Frame(lblframeleft,bd=2,relief=FLAT)
                btn_frame1.place(x=-10,y=330,width=460,height=80)


                btnAdd=Button(btn_frame1,command=self.add_data,width=7,text="Add",font=("Comic Sans MS",15),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btnAdd.grid(row=0,column=0,padx=5)

                btn_update=Button(btn_frame1,command=self.update,width=7,text="Update",font=("Comic Sans MS",15),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btn_update.grid(row=0,column=1,padx=5)

                btn_delete=Button(btn_frame1,command=self.mdelete,width=7,text="Delete",font=("Comic Sans MS",15),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btn_delete.grid(row=0,column=2,padx=5)


                btn_rese=Button(btn_frame1,command=self.reset,width=7,text="Reset",font=("Comic Sans MS",15),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btn_rese.grid(row=0,column=3,padx=5)


                # Table Frame search system
               
                Table_Frame=LabelFrame(self.root,bd=2,relief=FLAT,text="View Details and Search",font=("Comic Sans MS",20),bg="grey",fg="black")
                Table_Frame.place(x=428,y=60,width=725,height=490)

                #search by button
                
                btn_search=Button(Table_Frame,width=7,bd=4,text="Search By",font=("Comic Sans MS",10),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btn_search.grid(row=0,column=0,padx=2,pady=2)

                self.search_var=StringVar()
                combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("Comic Sans MS",15),width=15,state="read")
                combo_search["value"]=("Name","IDNumber")
                combo_search.current()
                combo_search.grid(row=0,column=1,sticky=W,pady=5,padx=2)


                self.txt_search=StringVar()
                txtse=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=20,font=("Comic Sans MS",15))
                txtse.grid(row=0,column=3,sticky=W,pady=5,padx=2)

                btnsearch=Button(Table_Frame,command=self.search,width=7,bd=4,text="Search",font=("Comic Sans MS",10),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btnsearch.grid(row=0,column=4,padx=2,pady=2)

                btn_show=Button(Table_Frame,command=self.fetch_data,width=7,bd=4,text="Show all",font=("Comic Sans MS",10),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btn_show.grid(row=0,column=5,padx=2,pady=2)


        #======== show data table==========######
                details_table=Frame(Table_Frame, bd=4,relief=FLAT)
                details_table.place(x=10,y=60,width=650,height=300)


                #scrollbar
                scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)


                #table

                self.User_Details_Table=ttk.Treeview(details_table,columns=("user","Id","name","email","gender"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.User_Details_Table.xview)
                scroll_y.config(command=self.User_Details_Table.yview)

                ##heading 

                self.User_Details_Table.heading("user",text="User Type")
                self.User_Details_Table.heading("Id",text="Id Number")
                self.User_Details_Table.heading("name",text="User Name")
                self.User_Details_Table.heading("email",text="Outlook Id")
                self.User_Details_Table.heading("gender",text="Gender")

                self.User_Details_Table["show"]="headings"
                self.User_Details_Table.pack(fill=BOTH,expand=1)
                
                #adjust width
                self.User_Details_Table.column("user",width=100)
                self.User_Details_Table.column("Id",width=100)
                self.User_Details_Table.column("name",width=100)
                self.User_Details_Table.column("email",width=100)
                self.User_Details_Table.column("gender",width=100)

                self.User_Details_Table.pack(fill=BOTH,expand=1)
                self.User_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
                self.fetch_data()


        def add_data(self):
                if self.var_uid.get()=="" or self.var_uname.get()=="" or self.var_uemail.get()=="":
                        messagebox.showerror("Error","Please Fill All the Details")
                else:
                        try:
                
                                conn=mysql.connector.connect(host="localhost",username="root",password="saymyname@2",database="management")
                                my_cursor=conn.cursor()
                                my_cursor.execute("insert into user values(%s,%s,%s,%s,%s)",(
                                                                                        self.var_utype.get(),
                                                                                        self.var_uid.get(),
                                                                                        self.var_uname.get(),
                                                                                        self.var_uemail.get(),
                                                                                        self.var_ugender.get()))
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Success","User Added",parent=self.root)
                        except Exception as es:
                                messagebox.showwarning("Warning",f"Something went Wrong:{str(es)}",parent=self.root)

        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="saymyname@2",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("select *from user")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.User_Details_Table.delete(*self.User_Details_Table.get_children())
                        for i in rows:
                                self.User_Details_Table.insert("",END,values=i)
                        conn.commit()
                        conn.close()

        def get_cursor(self,event=""):
                cursor_row=self.User_Details_Table.focus()
                content=self.User_Details_Table.item(cursor_row)
                row=content["values"]

                self.var_utype.set(row[0]),
                self.var_uid.set(row[1]),
                self.var_uname.set(row[2]),
                self.var_uemail.set(row[3]),
                self.var_ugender.set(row[4])



        def update(self):
                if self.var_uid.get()=="":
                        messagebox.showerror("Error","Please fil Id Number",parent=self.root)
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="saymyname@2",database="management")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update user set UserType=%s,Name=%s,OutlookID=%s,Gender=%s where IDNumber=%s",(
                                                                                        self.var_utype.get(),
                                                                                        self.var_uname.get(),
                                                                                        self.var_uemail.get(),
                                                                                        self.var_ugender.get(),
                                                                                        self.var_uid.get()
                                                                                        ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Updated","User Details has been Updated Successully",parent=self.root)
                        
                               
        def mdelete(self):
                mdelete=messagebox.askyesno("Delete","Do you want to delete this User",parent=self.root)
                if mdelete>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="saymyname@2",database="management")
                        my_cursor=conn.cursor()
                        query="delete from user where IDNumber=%s"
                        value=(self.var_uid.get(),)
                        my_cursor.execute(query,value)
                else:
                        if not mdelete:
                                        return
                conn.commit()
                self.fetch_data()
                conn.close()

        def reset(self,event=""):
                cursor_row=self.User_Details_Table.focus()
                content=self.User_Details_Table.item(cursor_row)
                row=content["values"]

                self.var_utype.set(""),
                self.var_uid.set(""),
                self.var_uname.set(""),
                self.var_uemail.set(""),
                self.var_ugender.set("")



        def search(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="saymyname@2",database="management")
                my_cursor=conn.cursor()

                my_cursor.execute("select * from user where "+ str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.User_Details_Table.delete(*self.User_Details_Table.get_children())
                        for i in rows:
                                self.User_Details_Table.insert("",END,values=i)
                        conn.commit()
                conn.close()


                        




        





if __name__ == "__main__":
    root=Tk()
    obj=user_window(root)
    root.mainloop()

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
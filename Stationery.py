from tkinter import *
import mysql.connector
from mysql.connector import MySQLConnection,Error
try:
    print("Connecting...")
    conn=mysql.connector.connect(host='localhost',database='prachi',user='root',password='root')
    if conn.is_connected():
        print("Connected")
        c=conn.cursor()
        c.execute('drop table if exists product')
        c.execute('create table product (pro_id int(4), pro_name char(10), quantity int(4));')
        print("Table Created")
        
        p=Tk()
        p.title('DBMSinPY')
        def add():
            def insert():
                x=m.get()
                y=n.get()
                z=o.get()
                c.execute("insert into product(pro_id,pro_name,quantity) values('{}','{}','{}')".format(x,y,z))
                print("Record Entered successfully.")

            m=StringVar()
            n=StringVar()
            o=StringVar()
            Label(p,text='Enter the records.').grid(row=2,column=0)
            Label(p,text='Pro_id=').grid(row=3,column=0)
            Entry(p,textvariable=m).grid(row=3,column=1)
            Label(p,text='Pro_Name=').grid(row=4,column=0)
            Entry(p,textvariable=n).grid(row=4,column=1)
            Label(p,text='Quantity=').grid(row=5,column=0)
            Entry(p,textvariable=o).grid(row=5,column=1)
            Button(p,text='insert',command=insert).grid(row=6,column=0)
            
        def delete():
            def removeit():
                q=m.get()
                c.execute("delete from product where pro_id='{}'".format(q))
                print("1 Row deleted.")

            m=StringVar()
            Label(p,text='Enter the records.').grid(row=2,column=0)
            Label(p,text='Pro_id=').grid(row=3,column=2)
            Entry(p,textvariable=m).grid(row=3,column=3)
            Button(p,text='remove',command=removeit).grid(row=6,column=3)
        def modify():
            def modify():
                q=m.get()
                w=n.get()
                c.execute("update product set pro_name='{}' where pro_id='{}'".format(w,q))
                print("1 Row updated.")

            m=StringVar()
            n=StringVar()
            Label(p,text='Enter the records.').grid(row=2,column=0)
            Label(p,text='Pro_id=').grid(row=3,column=4)
            Entry(p,textvariable=m).grid(row=3,column=5)
            Label(p,text='Pro_Name=').grid(row=4,column=4)
            Entry(p,textvariable=n).grid(row=4,column=5)
            Button(p,text='Update',command=modify).grid(row=6,column=4)
        def see():
            c.execute('select * from product')
            result=c.fetchall()
            print("Pro_id\tPro_name\tQuantity")
            for row in result:
                pid=row[0]
                name=row[1]
                quant=row[2]
                print(pid,'\t',name,'\t\t',quant,'\t')
        def close():
            p.destroy()
        
        Label(p,text='Choose the following').grid(row=0,column=1)
        Button(p,text='close',command=close).grid(row=0,column=2)
        Button(p,text='ADD',command=add).grid(row=1,column=0)
        Button(p,text='DELETE',command=delete).grid(row=1,column=2)
        Button(p,text='MODIFY',command=modify).grid(row=1,column=4)
        Button(p,text='SEE-REC',command=see).grid(row=1,column=5)
        p.mainloop()
    else:
        print("Error in connection:")
except Error as e:
    print(e)
finally:
    conn.commit()
    print("Work committed.")
    conn.close()
    print("Connection closed.")
    print("End of program.")

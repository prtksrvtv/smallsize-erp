#!/usr/bin/env python
# coding: utf-8

# In[6]:


import mysql.connector
from datetime import datetime,date

def dbin(a,d,bill):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "12345",
        database="prikaway"
    )
    cursor = mydb.cursor()
    for x in d:
        if x not in ['Roll No.','Name','Class','House','Date']:
            for y in a.iterrows():
                if y[1][0] == x:
                    break
            render=tuple([d['Roll No.'],d['Name'],d['Class'],d['House'],x,d[x][1],int(d[x][0]),y[1][1]*int(d[x][0]),False,str(d['Date'].strftime("%Y-%m-%d")),bill])
            sql='insert into master_data(roll_no,student_name,class,house,item_purchased,item_size,item_quantity,total_price,tc_leave,date_of_purchase,bill_no) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql,render)
    mydb.commit()
    mydb.close()
    
def rem():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "12345",
        database="prikaway"
    )
    cursor = mydb.cursor()
    cursor.execute("""update inventory i,master_data m
                        set i.item_present=i.item_present-m.item_quantity
                        where m.item_purchased=i.item_name and m.item_size=i.item_size""")
    mydb.commit()
    mydb.close()

def pay_d(r):
    
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "12345",
        database="prikaway"
    )
    cursor = mydb.cursor()
    cursor.execute("""update school_invoices 
                        set payment_amount=%s, payment_date=%s,work_order_no=%s
                        where bill_no=%s""",(r[2],datetime.strptime(r[1],"%d-%m-%Y"),r[3],('PWPL/RW/23/'+str(r[0]))))
    
    mydb.commit()
    mydb.close()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[12]:


import mysql.connector

def bill_principal_entry():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "12345",
        database="prikaway"
    )
    cursor = mydb.cursor()
    cursor.execute("""select 
                        concat('PWPL/RW/',right(year(curdate()),2),'/',max(bill_id)+1) as name_id 
                        from school_invoices """)
    rec=cursor.fetchall()
    mydb.commit()
    mydb.close()
    return rec[0][0]

def bill_entry(memory):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "12345",
        database="prikaway"
    )
    cursor = mydb.cursor()
    query="""insert into school_invoices(bill_no,bill_amount,submission_date) values(%s,%s,%s) """
    cursor.execute(query,memory)
    mydb.commit()
    mydb.close()


# In[ ]:





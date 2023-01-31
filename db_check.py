#!/usr/bin/env python
# coding: utf-8

# In[5]:


import mysql.connector
import pandas as pd

def check(t):
    
    connection = mysql.connector.connect(
                                        host = "localhost",
                                        user = "root",
                                        password = "12345",
                                        database="prikaway")

    sql_select_Query = "select * from master_data where bill_no=%s"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query,t)
    # get all records
    records = cursor.fetchall()
    a=pd.DataFrame(records)
    print(a)
    if len(a)>0:
        print("Found")
    else:
        print("Not Found")
    connection.commit()
    connection.close()


# In[ ]:





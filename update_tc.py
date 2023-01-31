#!/usr/bin/env python
# coding: utf-8

# In[4]:


import mysql.connector
import pandas as pd

def upd(bill):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "12345",
        database="prikaway"
    )
    cursor = mydb.cursor()
    query = """update master_data m
                set m.tc_leave= True
                where bill_no=%s"""
    cursor.execute(query,bill)
    mydb.commit()
    mydb.close()
    return True


# In[ ]:





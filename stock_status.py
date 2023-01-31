#!/usr/bin/env python
# coding: utf-8

# In[4]:


import mysql.connector
import pandas as pd

def status():
    
    connection = mysql.connector.connect(
                                        host = "localhost",
                                        user = "root",
                                        password = "12345",
                                        database="prikaway")

    sql_select_Query = "select * from inventory order by item_name"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    a=pd.DataFrame(records)
    connection.commit()
    connection.close()
    return a


# In[ ]:





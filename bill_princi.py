#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mysql.connector
import pandas as pd
from summary_window import *

def checker(l1,l2):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "12345",
        database="prikaway"
    )
    cursor = mydb.cursor()
    query = """select item_purchased, sum(item_quantity), sum(total_price)
                from 
                    master_data
                where
                    (extract(month from date_of_purchase) =%s or extract(month from date_of_purchase) =%s) and tc_leave=False
                group by
                    item_purchased"""
    cursor.execute(query,(l1,l2))
    records=cursor.fetchall()
    a=pd.DataFrame(records)
    query1 = """select house, count(distinct student_name) as no_of_student,sum(item_quantity), sum(total_price)
                from 
                    master_data
                where
                    (extract(month from date_of_purchase) =%s or extract(month from date_of_purchase) =%s) and tc_leave=False
                group by
                    house
                order by 
                    house"""
    cursor.execute(query1,(l1,l2))
    records1=cursor.fetchall()
    b=pd.DataFrame(records1)
    query1 = """select *
                from 
                    master_data
                where
                    (extract(month from date_of_purchase) =%s or extract(month from date_of_purchase) =%s) and tc_leave=False
                """
    cursor.execute(query1,(l1,l2))
    records2=cursor.fetchall()
    c=pd.DataFrame(records2,columns=cursor.column_names)
    mydb.commit()
    mydb.close()
    gen_win(a,b,c)
    
def checker_tc(l1,l2):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "12345",
        database="prikaway"
    )
    cursor = mydb.cursor()
    query = """select item_purchased, sum(item_quantity), sum(total_price)
                from 
                    master_data
                where
                    (extract(month from date_of_purchase) =%s or extract(month from date_of_purchase) =%s) and tc_leave=True
                group by
                    item_purchased"""
    cursor.execute(query,(l1,l2))
    records=cursor.fetchall()
    a=pd.DataFrame(records)
    query1 = """select house, count(distinct student_name) as no_of_student,sum(item_quantity), sum(total_price)
                from 
                    master_data
                where
                    (extract(month from date_of_purchase) =%s or extract(month from date_of_purchase) =%s) and tc_leave=True
                group by
                    house
                order by 
                    house"""
    cursor.execute(query1,(l1,l2))
    records1=cursor.fetchall()
    b=pd.DataFrame(records1)
    query1 = """select *
                from 
                    master_data
                where
                    (extract(month from date_of_purchase) =%s or extract(month from date_of_purchase) =%s) and tc_leave=True
                """
    cursor.execute(query1,(l1,l2))
    records2=cursor.fetchall()
    c=pd.DataFrame(records2,columns=cursor.column_names)
    mydb.commit()
    mydb.close()
    gen_win(a,b,c)


# In[ ]:





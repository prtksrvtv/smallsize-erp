#!/usr/bin/env python
# coding: utf-8

# In[3]:


import mysql.connector
from datetime import datetime,date

def roger(a,d):
    lamb=date.today()
    mydb = mysql.connector.connect(
                                        host = "localhost",
                                        user = "root",
                                        password = "12345",
                                        database="prikaway")
    
    
    cursor=mydb.cursor()
    cursor.execute("""drop table if exists ana""")
    cursor.execute("""create table if not exists ana(
                    item_name varchar(55),
                    item_quan int,
                    item_size varchar(5),
                    seller_name varchar(255),
                    date_ordered date)""")
    for x in d:
        render=tuple([x,d[x][0],d[x][1],d[x][2],str(lamb.strftime("%Y-%m-%d"))])
        sql="""insert into ana(item_name,item_quan,item_size,seller_name,date_ordered) values(%s,%s,%s,%s,%s)"""
        cursor.execute(sql,render)
        
    for y in d:
        for x in a.iterrows():              
            if y==x[1][0]: #checking for name
                if d[y][1]==x[1][2]: #checking for size
                    
                    cursor.execute("""update inventory
                        set item_present=%s, seller_name=%s, date_ordered=%s
                        where item_name=%s and item_size=%s""",((x[1][1]+d[y][0]),d[y][2],str(lamb.strftime("%Y-%m-%d")),x[1][0],x[1][2]))
                    break
                else:       
                    if d[y][0]>0:
                        render=tuple([y,d[y][0],d[y][1],str(lamb.strftime("%Y-%m-%d"))])
                        sql='insert into inventory(item_name,item_present,item_size,seller_name,date_ordered) values(%s,%s,%s,%s,%s)'
                        cursor.execute(sql,render)
                        break

    mydb.commit()
    mydb.close()


# In[ ]:





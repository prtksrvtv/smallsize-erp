#!/usr/bin/env python
# coding: utf-8

# In[4]:


from tkinter import *
import tkinter as tk
from tkinter import ttk
import pandas as pd
from invpro import *
from dbin import *
from tkinter.ttk import *
import mysql.connector
from datetime import date
import os

connection = mysql.connector.connect(
                                        host = "localhost",
                                        user = "root",
                                        password = "12345",
                                        database="prikaway")

sql_select_Query = "select * from price_list"
cursor = connection.cursor()
cursor.execute(sql_select_Query)
# get all records
records = cursor.fetchall()
a=pd.DataFrame(records)


items=['Roll No.','Name','Class','House','Date']
d={}

for y in items:
    d[y]=''
for y in a.iterrows():
    d[y[1][0]] = 0
   


root=Tk()
root.title("Input the item qunatity")
# setting the windows size
root.geometry("600x600")
main_frame=Frame(root)
main_frame.pack(fill=BOTH, expand=1)
my_canvas=Canvas(main_frame)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL,command=my_canvas.yview)
scrollbar.pack(side=RIGHT,fill=Y)
my_canvas.configure(yscrollcommand=scrollbar.set)
my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
second_frame=Frame(my_canvas)
my_canvas.create_window((0,0),window=second_frame, anchor='nw')
count=0

for x in d:
    
    if x not in ['Roll No.','Name','Class','House','Date']:
        name_label = tk.Label(second_frame, text = x, font=('calibre',10, 'bold'))
        name_entry = tk.Entry(second_frame, font=('calibre',10,'normal'))
        size_label=tk.Label(second_frame, text = 'Size', font=('calibre',10, 'bold'))
        size_entry = tk.Entry(second_frame, font=('calibre',10,'normal'))
        size_label.grid(row=count,column=2)
        size_entry.grid(row=count,column=3)
        d[x]=[name_entry,size_entry]
        name_label.grid(row=count,column=0)
        name_entry.grid(row=count,column=1)
    else:
        
        name_label = tk.Label(second_frame, text = x, font=('calibre',10, 'bold'))
        name_entry = tk.Entry(second_frame, font=('calibre',10,'normal'))
        d[x]=name_entry
        name_label.grid(row=count,column=0)
        name_entry.grid(row=count,column=1)
    
    count+=1
    
submit = Button(
    second_frame,
    text='Print', command= lambda : rty(d)
    )
submit.grid(row=count,column=0)

def rty(d):
    
    for x in d:
        if x not in ['Roll No.','Name','Class','House','Date']:
            if d[x][0].get()=='':
                d[x][0]=0
                d[x][1]=''
            else:
                d[x][0]=d[x][0].get()
                d[x][1]=d[x][1].get()
        else:
            d[x]=d[x].get()
            
    d['Date']=date.today()
    z=proc(a,d)
    dbin(a,d,z)
    rem()
    os.system('python done_window.py')
root.mainloop()


# In[ ]:





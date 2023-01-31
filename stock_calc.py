#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *
import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter.ttk import *
import mysql.connector
from stock_mod import *
import os

def rty(d):
    
    for x in d:
        if d[x][0].get()=='':
            d[x][0]=0
            d[x][1]= None
            d[x][2]= None
            d[x][3]= None
        else:
            d[x][0]=int(d[x][0].get())
            d[x][1]=d[x][1].get()
            d[x][2]=d[x][2].get()
            d[x][3]=d[x][3].get()
    roger(a,d)
    os.system('python done_window.py')
                
connection = mysql.connector.connect(
                                        host = "localhost",
                                        user = "root",
                                        password = "12345",
                                        database="prikaway")

sql_select_Query = "select * from inventory"
cursor = connection.cursor()
cursor.execute(sql_select_Query)
# get all records
records = cursor.fetchall()
a=pd.DataFrame(records)

d={}

for y in a.iterrows():
    d[y[1][0]] = 0


root=Tk()
root.title("Input the item qunatity")
# setting the windows size
root.geometry("800x500")
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

    name_label = tk.Label(second_frame, text = x, font=('calibre',10, 'bold'))
    name_entry = tk.Entry(second_frame, font=('calibre',10,'normal'))
    size_label=tk.Label(second_frame, text = 'Size', font=('calibre',10, 'bold'))
    size_entry = tk.Entry(second_frame, font=('calibre',10,'normal'))
    size_label.grid(row=count,column=2)
    size_entry.grid(row=count,column=3)
    name_label.grid(row=count,column=0)
    name_entry.grid(row=count,column=1)
    vendor_label = tk.Label(second_frame, text = 'Vendor Name', font=('calibre',10, 'bold'))
    vendor_entry = tk.Entry(second_frame, font=('calibre',10,'normal'))
    date_label = tk.Label(second_frame, text = 'Date', font=('calibre',10, 'bold'))
    date_entry = tk.Entry(second_frame, font=('calibre',10,'normal'))
    d[x]=[name_entry,size_entry,vendor_entry,date_entry]
    vendor_label.grid(row=count,column=4)
    vendor_entry.grid(row=count,column=5)
    date_label.grid(row=count,column=6)
    date_entry.grid(row=count,column=7)
    count+=1
    
submit = Button(
    second_frame,
    text='SUBMIT', command= lambda: rty(d)
    )
submit.grid(row=count,column=0)

root.mainloop()


# In[ ]:





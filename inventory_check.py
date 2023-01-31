#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import mysql.connector
from stock_status import *
import pandas as pd

a=status()
b=pd.DataFrame(a)
root=Tk()
root.title("Current Stock In Inventory")
# setting the windows size
root.geometry("700x700")
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

name_label = tk.Label(second_frame, text = 'Item Name', font=('calibre',10, 'bold'))
name_label.grid(row=count,column=0)
size_label=tk.Label(second_frame, text = 'Item Size', font=('calibre',10, 'bold'))
size_label.grid(row=count,column=1)
stock_label=tk.Label(second_frame, text = 'Present Stock', font=('calibre',10, 'bold'))
stock_label.grid(row=count,column=2)
vendor_label = tk.Label(second_frame, text = 'Vendor Name', font=('calibre',10, 'bold'))
date_label = tk.Label(second_frame, text = 'Date of Entry', font=('calibre',10, 'bold'))
vendor_label.grid(row=count,column=3)
date_label.grid(row=count,column=4)
count+=1
for x in b.iterrows():
    
    name_label = tk.Label(second_frame, text = x[1][0], font=('calibre',10, 'bold'))
    name_label.grid(row=count,column=0)
    size_label=tk.Label(second_frame, text = x[1][2], font=('calibre',10, 'bold'))
    size_label.grid(row=count,column=1)
    stock_label=tk.Label(second_frame, text = x[1][1], font=('calibre',10, 'bold'))
    stock_label.grid(row=count,column=2)
    vendor_label = tk.Label(second_frame, text = x[1][3], font=('calibre',10, 'bold'))
    date_label = tk.Label(second_frame, text = x[1][4].strftime("%d-%m-%Y"), font=('calibre',10, 'bold'))
    vendor_label.grid(row=count,column=3)
    date_label.grid(row=count,column=4)
    count+=1

root.mainloop()


# In[ ]:





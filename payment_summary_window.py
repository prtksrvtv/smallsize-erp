#!/usr/bin/env python
# coding: utf-8

# In[4]:


from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import pandas as pd
import mysql.connector
from datetime import date

mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "12345",
        database="prikaway"
    )
cursor = mydb.cursor()
cursor.execute(""" select * from school_invoices""")
records=cursor.fetchall()
a=pd.DataFrame(records,columns=cursor.column_names)
a['payment_amount']=a['payment_amount'].fillna(0)

root=Tk()
root.title("Prikaway Pvt. Ltd. - Client - Sainik School Rewari - Payment Summary")
# setting the windows size
root.geometry("1000x500")
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
s=q=count=0
name_label = tk.Label(second_frame, text = 'BILL NO.', font=('calibre',10, 'bold'))
name_label.grid(row=count,column=0)
name_label = tk.Label(second_frame, text = 'BILL AMOUNT', font=('calibre',10, 'bold'))
name_label.grid(row=count,column=1)
size_label=tk.Label(second_frame, text = 'SUBMISSION DATE', font=('calibre',10, 'bold'))
size_label.grid(row=count,column=2)
stock_label=tk.Label(second_frame, text = 'AMOUNT CREDITED', font=('calibre',10, 'bold'))
stock_label.grid(row=count,column=3)
stock_label=tk.Label(second_frame, text = 'PAYMENT DATE', font=('calibre',10, 'bold'))
stock_label.grid(row=count,column=4)
stock_label=tk.Label(second_frame, text = 'PAYMENT CYCLE', font=('calibre',10, 'bold'))
stock_label.grid(row=count,column=5)
stock_label=tk.Label(second_frame, text = 'WORK ORDER NO.', font=('calibre',10, 'bold'))
stock_label.grid(row=count,column=6)
count+=1

for x in a.iterrows():

    name_label = tk.Label(second_frame, text = x[1][1], font=('calibre',10, 'bold'))
    name_label.grid(row=count,column=0)
    quan_label=tk.Label(second_frame, text = x[1][2], font=('calibre',10, 'bold'))
    quan_label.grid(row=count,column=1)
    price_label=tk.Label(second_frame, text = x[1][3].strftime("%d-%m-%Y"), font=('calibre',10, 'bold'))
    price_label.grid(row=count,column=2)        
    price_label=tk.Label(second_frame, text = x[1][4], font=('calibre',10, 'bold'))
    price_label.grid(row=count,column=3)
    if x[1][5] == None:
        price_label=tk.Label(second_frame, text = 'Payment Not Recevied', font=('calibre',10, 'bold'))
        price_label.grid(row=count,column=4)
        price_label=tk.Label(second_frame, text = str(((date.today())-x[1][3]).days)+" days", font=('calibre',10, 'bold'))
        price_label.grid(row=count,column=5)
    else:    
        price_label=tk.Label(second_frame, text = x[1][5].strftime("%d-%m-%Y"), font=('calibre',10, 'bold'))
        price_label.grid(row=count,column=4)
        price_label=tk.Label(second_frame, text = str((x[1][5]-x[1][3]).days)+" days", font=('calibre',10, 'bold'))
        price_label.grid(row=count,column=5)
    price_label=tk.Label(second_frame, text = x[1][6], font=('calibre',10, 'bold'))
    price_label.grid(row=count,column=6)
    s=s+x[1][2]
    q=q+x[1][4]
    count+=1
t_label = tk.Label(second_frame, text = 'Grand Total', font=('calibre',10, 'bold'))
t_label.grid(row=count,column=0)
tq_label = tk.Label(second_frame, text = s, font=('calibre',10, 'bold'))
tq_label.grid(row=count,column=1)
tp_label = tk.Label(second_frame, text = q, font=('calibre',10, 'bold'))
tp_label.grid(row=count,column=3)

root.mainloop()


# In[ ]:





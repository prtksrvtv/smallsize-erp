#!/usr/bin/env python
# coding: utf-8

# In[8]:


from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk
from dbin import *
import os

def do2():
    r=[]
    for x in temp:
        r.append(x.get())
    pay_d(r)
    os.system('python done_window.py')
    
ws = Tk()
ws.title('Prikaway Pvt. Ltd.')
ws.geometry('300x500')
ws.config(bg='#345')
lbl=tk.Label(ws, text="ENTER WORKORDER PAYMENT DETAILS",font=('calibre',10, 'bold'))
lbl.pack(padx=10,pady=10)
name_label=tk.Label(ws, text="BILL NO. SUBMITTED TO PRINCIPAL",font=('calibre',10, 'bold'))
name_label.pack(padx=10,pady=10)
name_label=tk.Label(ws, text="PWPL/RW/23/_",font=('calibre',10, 'bold'))
name_label.pack(padx=10,pady=10)
name_entry = tk.Entry(ws, font=('calibre',10,'normal'))
name_entry.pack(padx=10,pady=10)
name_label=tk.Label(ws, text="DATE OF PAYMENT (DD-MM-YYYY)",font=('calibre',10, 'bold'))
name_label.pack(padx=10,pady=10)
name_entry2 = tk.Entry(ws, font=('calibre',10,'normal'))
name_entry2.pack(padx=10,pady=10)
name_label=tk.Label(ws, text="AMOUNT CREDITED IN BANK",font=('calibre',10, 'bold'))
name_label.pack(padx=10,pady=10)
name_entry3 = tk.Entry(ws, font=('calibre',10,'normal'))
name_entry3.pack(padx=10,pady=10)
name_label=tk.Label(ws, text="WORK ORDER NO.",font=('calibre',10, 'bold'))
name_label.pack(padx=10,pady=10)
name_entry4 = tk.Entry(ws, font=('calibre',10,'normal'))
name_entry4.pack(padx=10,pady=10)
temp=[name_entry,name_entry2,name_entry3,name_entry4]
submit = Button(
    ws,
    text='SUBMIT', command= do2
    )
submit.pack(padx=10,pady=10)
ws.mainloop()


# In[ ]:





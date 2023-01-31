#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk  
from update_tc import *
import os

def do2():
    
    n=['PWPL/RW/23/'+name_entry.get()]
    r=upd(n)
    if r==True:
        os.system('python done_window.py')

ws = Tk()
ws.title('Prikaway Pvt. Ltd.')
ws.geometry('300x300')
ws.config(bg='#345')
lbl=tk.Label(ws, text="MARK BILL FOR TC/LEAVE",font=('calibre',10, 'bold'))
lbl.pack(padx=10,pady=10)
name_label=tk.Label(ws, text="ENTER BILL NO. PWPL/RW/23/_",font=('calibre',10, 'bold'))
name_label.pack(padx=10,pady=10)
name_entry = tk.Entry(ws, font=('calibre',10,'normal'))
name_entry.pack(padx=10,pady=10)
z=name_entry.get()
submit = Button(
    ws,
    text='SUBMIT', command= do2
    )
submit.pack(padx=10,pady=10)
name_label=tk.Label(ws, text="WARNING: BE CAREFUL! CHANGES ",font=('calibre',10, 'bold'))
name_label.pack()
name_label=tk.Label(ws, text="ONCE DONE CANNOT BE REVERTED BACK",font=('calibre',10, 'bold'))
name_label.pack()


ws.mainloop()


# In[ ]:





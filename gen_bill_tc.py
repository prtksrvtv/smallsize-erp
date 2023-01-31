#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk
from bill_princi import *

def do2():
    n=name_entry.get().split(",")
    n[0]=int(n[0])
    n[1]=int(n[1])
    checker_tc(n[0],n[1])

ws = Tk()
ws.title('Prikaway Pvt. Ltd.')
ws.geometry('300x300')
ws.config(bg='#345')
lbl=tk.Label(ws, text="ENTER MONTHS FOR PROCESSING",font=('calibre',10, 'bold'))
lbl.pack(padx=10,pady=10)
lbl=tk.Label(ws, text="SEPERATED BY COMMA",font=('calibre',10, 'bold'))
lbl.pack(padx=10,pady=10)
name_label=tk.Label(ws, text="MONTH 1, MONTH 2",font=('calibre',10, 'bold'))
name_label.pack(padx=10,pady=10)
name_entry = tk.Entry(ws, font=('calibre',10,'normal'))
name_entry.pack(padx=10,pady=10)

submit = Button(
    ws,
    text='SUBMIT', command= do2
    )
submit.pack(padx=10,pady=10)
name_label=tk.Label(ws, text="CHECK SUMMARY IN NEXT WINDOW ",font=('calibre',10, 'bold'))
name_label.pack()
name_label=tk.Label(ws, text="AND PRESS PRINT",font=('calibre',10, 'bold'))
name_label.pack()
ws.mainloop()


# In[ ]:





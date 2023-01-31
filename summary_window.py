#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import pandas as pd
from report_process import *

def gen_win(a,b,p):
    
    root=Tk()
    root.title("Summary")
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
    s=q=count=0
    name_label = tk.Label(second_frame, text = 'ITEM SUMMARY', font=('calibre',10, 'bold'))
    name_label.grid(row=count,column=0)
    count+=1
    name_label = tk.Label(second_frame, text = 'Item Name', font=('calibre',10, 'bold'))
    name_label.grid(row=count,column=0)
    size_label=tk.Label(second_frame, text = 'Total Items', font=('calibre',10, 'bold'))
    size_label.grid(row=count,column=1)
    stock_label=tk.Label(second_frame, text = 'Total Quantity', font=('calibre',10, 'bold'))
    stock_label.grid(row=count,column=2)
    count+=1
    
    for x in a.iterrows():

        name_label = tk.Label(second_frame, text = x[1][0], font=('calibre',10, 'bold'))
        name_label.grid(row=count,column=0)
        quan_label=tk.Label(second_frame, text = x[1][1], font=('calibre',10, 'bold'))
        quan_label.grid(row=count,column=1)
        price_label=tk.Label(second_frame, text = x[1][2], font=('calibre',10, 'bold'))
        price_label.grid(row=count,column=2)
        s=s+x[1][2]
        q=q+x[1][1]
        count+=1
    t_label = tk.Label(second_frame, text = 'Grand Total', font=('calibre',10, 'bold'))
    t_label.grid(row=count,column=0)
    tq_label = tk.Label(second_frame, text = q, font=('calibre',10, 'bold'))
    tq_label.grid(row=count,column=1)
    tp_label = tk.Label(second_frame, text = s, font=('calibre',10, 'bold'))
    tp_label.grid(row=count,column=2)
    count+=1
    t_label = tk.Label(second_frame, text = ' ', font=('calibre',10, 'bold'))
    t_label.grid(row=count,column=0)
    count+=1
    t_label = tk.Label(second_frame, text = 'HOUSE SUMMARY ', font=('calibre',10, 'bold'))
    t_label.grid(row=count,column=0)
    count+=1
    name_label = tk.Label(second_frame, text = 'House Name', font=('calibre',10, 'bold'))
    name_label.grid(row=count,column=0)
    size_label=tk.Label(second_frame, text = 'Total Students', font=('calibre',10, 'bold'))
    size_label.grid(row=count,column=1)
    stock_label=tk.Label(second_frame, text = 'Total Items', font=('calibre',10, 'bold'))
    stock_label.grid(row=count,column=2)
    quan_label=tk.Label(second_frame, text = 'Total Quantity', font=('calibre',10, 'bold'))
    quan_label.grid(row=count,column=3)
    count+=1
    s=q=c=0
    for x in b.iterrows():

        name_label = tk.Label(second_frame, text = x[1][0], font=('calibre',10, 'bold'))
        name_label.grid(row=count,column=0)
        stu_label=tk.Label(second_frame, text = x[1][1], font=('calibre',10, 'bold'))
        stu_label.grid(row=count,column=1)
        quan_label=tk.Label(second_frame, text = x[1][2], font=('calibre',10, 'bold'))
        quan_label.grid(row=count,column=2)
        price_label=tk.Label(second_frame, text = x[1][3], font=('calibre',10, 'bold'))
        price_label.grid(row=count,column=3)
        c=c+x[1][1]
        q=q+x[1][2]
        s=s+x[1][3]
        count+=1
    t_label = tk.Label(second_frame, text = 'Grand Total', font=('calibre',10, 'bold'))
    t_label.grid(row=count,column=0)
    tq_label = tk.Label(second_frame, text = c, font=('calibre',10, 'bold'))
    tq_label.grid(row=count,column=1)
    tp_label = tk.Label(second_frame, text = q, font=('calibre',10, 'bold'))
    tp_label.grid(row=count,column=2)
    tp1_label = tk.Label(second_frame, text = s, font=('calibre',10, 'bold'))
    tp1_label.grid(row=count,column=3)
    count+=1
    submit = Button(
    second_frame,
    text='GENERATE BILL', command= lambda:invoice_processing(p)
    )
    submit.grid(row=count,column=2)
    root.mainloop()


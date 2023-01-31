#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
from fpdf import FPDF
from prettytable import PrettyTable
from PIL import Image, ImageDraw, ImageFont
from numtoword import *
import os
from datetime import date
from principal_bill_entry_in_db import *

def invoice_processing(a):

    pdf=FPDF()
    pdf.set_font("Arial", style="B",size = 10)
    path= r'C:\Users\ayush\Downloads\Prikaway\Invoice Generating Program\PRIKAWAY_REWARI_LOGO.png'   
    names=[]
    #printing all the invoices
    b=a.pivot_table(index='roll_no',values=['student_name','house','class','date_of_purchase','bill_no'],aggfunc='first')
    for x in b.iterrows():
        pdf.add_page()
        pdf.image(path, w=190, h=15)
        c=a[a['roll_no'].isin([x[0]])]
        j=PrettyTable()
        j.add_column('Name',[x[1][4]])
        j.add_column('Roll No.',[x[0]])
        j.add_column('House',[x[1][3]])
        j.add_column('Class',[x[1][1]])
        j.add_column('Purchase Date',[(x[1][2]).strftime("%d-%m-%Y")])
        j.add_column('Invoice No.',[x[1][0]])
        im = Image.new("RGB", (600, 70), "white")
        draw = ImageDraw.Draw(im)
        font = ImageFont.load_default()
        draw.text((0, 0), str(j), font=font, fill="black")
        im.save("header for roll no_"+str(x[0])+".png")
        names.append("header for roll no_"+str(x[0])+".png")
        pdf.image("header for roll no_"+str(x[0])+".png", w=193, h=20)
        d=c.pivot_table(index='item_purchased', values= ['item_quantity','total_price'], aggfunc='sum', margins=True, margins_name="Grand Total")
        i=PrettyTable(['Item Purchased','Quantity','Total Price'])
        for y in d.iterrows():
            i.add_row([y[0],y[1][0],"{:,}".format(y[1][1])])
        i.align["Item Purchased"]="l"
        i.align["Quantity"]="r"
        i.align["Total Price"]="r"
        ip = Image.new("RGB", (480, 900), "white")
        draw = ImageDraw.Draw(ip)
        font = ImageFont.load_default()
        draw.text((0, 0), str(i), font=font, fill="black")
        ip.save("table for roll no_"+str(x[0])+".png")
        names.append("table for roll no_"+str(x[0])+".png")
        pdf.image("table for roll no_"+str(x[0])+".png", w=195, h=224)
        pdf.set_font("Arial", style="B",size = 10)
        pdf.cell(200, 3, txt = "AMOUNT PAYABLE(In Words):"+'\t'*5+number_to_word(d.loc['Grand Total'][1]),ln = 1, align = 'L')
        pdf.set_font("Arial", size = 8)
        pdf.cell(200, 2, txt = "-"*200,ln = 1, align = 'L')
        pdf.cell(200, 2, txt = "CADET'S SIGNATURE"+'\t'*55+"HOUSE MASTER SIGNATURE"+'\t'*50+"AUTHORISED SIGNATURE",ln = 1, align = 'L')

    pdf.output("Invoices.pdf")

    
    d=a.pivot_table(index=['house','student_name','roll_no'], values=['item_quantity','total_price'], aggfunc='sum')
    e=d.groupby(by='house', axis=0, level=1)
    b=a.pivot_table(index=['item_purchased'], values=['item_quantity','total_price'], aggfunc='sum', margins=True, margins_name='Grand Total')

    pdf=FPDF()
    pdf.set_font("Arial", style="B",size = 10)
    pdf.add_page()
    #creating the main cover page of the bill
    i=PrettyTable(['Item Purchased','Quantity','Total Price'])
    for y in b.iterrows():
        i.add_row([y[0],"{:,}".format(y[1][0]),formatINR(y[1][1])])
    i.align["Item Purchased"]="l"
    i.align["Quantity"]="r"
    i.align["Total Price"]="r"
    ip = Image.new("RGB", (500, 1000), "white")
    draw = ImageDraw.Draw(ip)
    font = ImageFont.load_default()
    draw.text((0, 0), str(i), font=font, fill="black")
    ip.save("table for item list bill.png")
    names.append("table for item list bill.png")
    pdf.image(path, w=190, h=15)
    rem=date.today()
    tep=bill_principal_entry()
    pdf.cell(200, 2, txt = "-"*160,ln = 1, align = 'L')
    pdf.cell(w=80, h = 4, txt = 'To,'+'\t'*142+'BILL DATE: '+(rem.strftime("%d-%m-%Y")), ln = 1, align = 'L')
    pdf.cell(w=80, h = 4, txt = 'The Principal'+'\t'*120+'BILL NO.:'+tep, ln = 1, align = 'L')
    pdf.cell(w=80, h = 4, txt = 'Sainik School Rewari', ln = 1, align = 'L')
    pdf.cell(200, 2, txt = "-"*160,ln = 1, align = 'L')
    pdf.image("table for item list bill.png", w=193, h=224)
    pdf.cell(200, 3, txt = "AMOUNT PAYABLE(In Words):"+'\t'*5+number_to_word(b.loc['Grand Total'][1]),ln = 1, align = 'L')
    pdf.set_font("Arial", size = 8)
    memory=tuple([tep,float(b.loc['Grand Total'][1]),date.today()])
    bill_entry(memory)
    pdf.cell(200, 2, txt = "-"*200,ln = 1, align = 'L')
    pdf.cell(w=80, h = 4, txt = "PRINCIPAL'S SIGNATURE"+'\t'*150+"AUTHORISED SIGNATURE",ln = 1, align = 'L')
    
    #creating the house-wise summary view
    pdf.add_page()
    b=a.pivot_table(index=['house'], values=['item_quantity','total_price'], aggfunc='sum', margins=True, margins_name='Grand Total')
    i=PrettyTable(['House','Quantity','Total Price'])
    for y in b.iterrows():
        i.add_row([y[0],"{:,}".format(y[1][0]),formatINR(y[1][1])])
    i.align["House"]="l"
    i.align["Quantity"]="r"
    i.align["Total Price"]="r"
    ip = Image.new("RGB", (300, 200), "white")
    draw = ImageDraw.Draw(ip)
    font = ImageFont.load_default()
    draw.text((0, 0), str(i), font=font, fill="black")
    ip.save("table for summary.png")
    names.append("table for summary.png")
    pdf.image(path, w=190, h=15)
    pdf.ln(10)
    pdf.set_font("Arial", style="B",size = 40)
    pdf.cell(200, 10, txt = " Summary",ln = 2, align = 'C')
    pdf.image("table for summary.png",x=40, y=120,  w=150, h=100)
    
    #creating the summary page for each house
    for x in e.groups:
        d=e.get_group(x).pivot_table(index=['roll_no','student_name'], values=['item_quantity','total_price'], aggfunc='sum', margins=True, margins_name='Grand Total')
        i=PrettyTable(['Roll No.','Name','Quantity','Total Price'])
        pdf.add_page()
        for y in d.iterrows():
            i.add_row([y[0][0],y[0][1],"{:,}".format(y[1][0]),formatINR(y[1][1])])
        i.align["Roll No."]="r"
        i.align["Name"]="l"
        i.align["Quantity"]="r"
        i.align["Total Price"]="r"    
        ip = Image.new("RGB", (500, 1000), "white")
        draw = ImageDraw.Draw(ip)
        font = ImageFont.load_default()
        draw.text((0, 0), str(i), font=font, fill="black")
        ip.save("table for house_"+str(x)+".png")
        names.append("table for house_"+str(x)+".png")
        pdf.image(path, w=190, h=15)
        pdf.ln(10)
        pdf.set_font("Arial", style="B",size = 40)
        pdf.cell(200, 10, txt = x+" House",ln = 2, align = 'C')
        pdf.image("table for house_"+str(x)+".png",x=25, y=60,  w=200, h=240)
    
    for x in names:
        os.remove(x)
    pdf.output("Covers.pdf")
    
    if os.path.exists(r'C:\Users\ayush\Downloads\Prikaway\Invoice Generating Program\New App\Result\Covers.pdf'):
        os.remove(r'C:\Users\ayush\Downloads\Prikaway\Invoice Generating Program\New App\Result\Covers.pdf')
    if os.path.exists(r'C:\Users\ayush\Downloads\Prikaway\Invoice Generating Program\New App\Result\Invoices.pdf'):
        os.remove(r'C:\Users\ayush\Downloads\Prikaway\Invoice Generating Program\New App\Result\Invoices.pdf')    
    os.rename(r'C:\Users\ayush\Downloads\Prikaway\Invoice Generating Program\New App\Covers.pdf' , r'C:\Users\ayush\Downloads\Prikaway\Invoice Generating Program\New App\Result\Covers.pdf')
    os.rename(r'C:\Users\ayush\Downloads\Prikaway\Invoice Generating Program\New App\Invoices.pdf' , r'C:\Users\ayush\Downloads\Prikaway\Invoice Generating Program\New App\Result\Invoices.pdf')
    os.system('python done_window.py')


# In[ ]:





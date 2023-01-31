#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def proc(a,d):
    from numtoword import number_to_word
    from fpdf import FPDF
    from prettytable import PrettyTable
    from PIL import Image, ImageDraw, ImageFont
    import datetime
    import os
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial", style="B",size = 10)
    path= r'C:\Users\ayush\Downloads\Prikaway\Invoice Generating Program\PRIKAWAY_REWARI_LOGO.png'
    j=PrettyTable()
    j.add_column('Roll No.',[d['Roll No.']])
    j.add_column('Name.',[d['Name']])
    j.add_column('Class',[d['Class']])
    j.add_column('House',[d['House']])
    j.add_column('Date',[d['Date'].strftime("%d-%m-%Y")])
    currentMonth = datetime.datetime.now()
    bill="PWPL/RW/"+currentMonth.strftime("%y")+"/"+currentMonth.strftime("%b")+"/"+str(d['Roll No.'])
    j.add_column('Invoice No.',[bill])
    im = Image.new("RGB", (600, 70), "white")
    draw = ImageDraw.Draw(im)
    font = ImageFont.load_default()
    draw.text((0, 0), str(j), font=font, fill="black")
    im.save("header for roll no_"+str(d['Roll No.'])+".png")
    pdf.image(path, w=190, h=15)
    pdf.image("header for roll no_"+str(d['Roll No.'])+".png", w=193, h=20)
    
    j=PrettyTable(['Item Purchased','Size','Price','Quantity','Total'])
    price=count=0
    
    for x in d:
        if x not in ['Roll No.','Name','Class','House','Date']:
            for y in a.iterrows():
                if y[1][0] == x:
                    j.add_row([x,d[x][1],"{:,}".format(y[1][1]),d[x][0],"{:,}".format(y[1][1]*int(d[x][0]))])
                    break
            count=count+int(d[x][0])
            price=price+(y[1][1]*int(d[x][0]))
    j.add_row(['-'*38,'-'*4,'-'*5,'-'*8,'-'*6])
    j.add_row(['Grand Total','','',count,"{:,}".format(price)])
    j.align["Item Purchased"]="l"
    j.align["Size"]="l"
    j.align["Quantity"]="r"
    j.align["Price"]="r"
    j.align["Total"]="r"
    ip = Image.new("RGB", (480, 900), "white")
    draw = ImageDraw.Draw(ip)
    font = ImageFont.load_default()
    draw.text((0, 0), str(j), font=font, fill="black")
    ip.save("table for roll no_"+str(d['Roll No.'])+".png")
    pdf.image("table for roll no_"+str(d['Roll No.'])+".png", w=195, h=224)
    pdf.set_font("Arial", style="B",size = 10)
    pdf.cell(200, 3, txt = "AMOUNT PAYABLE(In Words):"+'\t'*5+number_to_word(price),ln = 1, align = 'L')
    pdf.set_font("Arial", size = 8)
    pdf.cell(200, 2, txt = "-"*200,ln = 1, align = 'L')
    pdf.cell(200, 2, txt = "CADET'S SIGNATURE"+'\t'*55+"HOUSE MASTER SIGNATURE"+'\t'*50+"AUTHORISED SIGNATURE",ln = 1, align = 'L')
    pdf.output("Invoice for roll_no_"+d['Roll No.']+".pdf")
    pa_check="Invoice for roll_no_"+d['Roll No.']+".pdf"
    os.remove("header for roll no_"+str(d['Roll No.'])+".png")
    os.remove("table for roll no_"+str(d['Roll No.'])+".png")
    if os.path.exists('C:\\Users\\ayush\\Downloads\\Prikaway\\Invoice Generating Program\\New App\\Result\\Invoice for roll_no_'+d['Roll No.']+'.pdf'):
        os.remove('C:\\Users\\ayush\\Downloads\\Prikaway\\Invoice Generating Program\\New App\\Result\\Invoice for roll_no_'+d['Roll No.']+'.pdf')
    os.rename('C:\\Users\\ayush\\Downloads\\Prikaway\\Invoice Generating Program\\New App\\Invoice for roll_no_'+d['Roll No.']+'.pdf', 'C:\\Users\\ayush\\Downloads\\Prikaway\\Invoice Generating Program\\New App\\Result\\Invoice for roll_no_'+d['Roll No.']+'.pdf')
    return bill


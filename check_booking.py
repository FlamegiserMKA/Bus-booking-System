from tkinter import *
from tkinter.messagebox import*
import sqlite3
con=sqlite3.Connection('Python_bus.db')
cur=con.cursor()
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

Label(root,text='Online Bus Booking System',font='Arial 20',fg='Red',bg='Sky Blue').grid(row=1,column=0,columnspan=3)
Label(root,text='Check Your Booking',font='Arial 15',fg='Green3',bg='Pale Green').grid(row=2,column=0,columnspan=3,pady=10)
Label(root,text='Enter your Mobile No.',font='Arial 10',width=15).grid(row=3,column=0,pady=10,sticky='E')
E1=Entry(root)
E1.grid(row=3,column=1)

bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=3,padx=w/2.5)
def fun():
    root.destroy()
    import home

def check_book():
    cur.execute(" select * from Booking_history where mobile='{}'".format(E1.get()))
    res=cur.fetchall()
    if len(res)==0:
        showerror('valueerror','Enter valid mobile number')
    else:
        frame4=LabelFrame(root,relief='groove',bd=5)
        frame4.grid(row=4,column=0,columnspan=11,padx=w//2.5)
        Label(frame4,text="Passenger:").grid(row=6,column=1)
        Label(frame4,text=res[0][1]).grid(row=6,column=2)
        Label(frame4,text="Gender:").grid(row=6,column=3)
        Label(frame4,text=res[0][2]).grid(row=6,column=4)
        Label(frame4,text="No of seat:").grid(row=7,column=1)
        Label(frame4,text=res[0][4]).grid(row=7,column=2)
        Label(frame4,text="Phone:").grid(row=7,column=3)
        Label(frame4,text=res[0][0]).grid(row=7,column=4)
        Label(frame4,text="Age:").grid(row=8,column=1)
        Label(frame4,text=res[0][3]).grid(row=8,column=2)
        Label(frame4,text="Fare Rs:").grid(row=8,column=3)
        Label(frame4,text=res[0][9]).grid(row=8,column=4)
        Label(frame4,text="Booking Ref:").grid(row=9,column=1)
        Label(frame4,text=res[0][12]).grid(row=9,column=2)
        Label(frame4,text="Bus Deatil:").grid(row=9,column=3)
        Label(frame4,text=res[0][8]).grid(row=9,column=4)
        Label(frame4,text="Travel On:").grid(row=10,column=1)
        Label(frame4,text=res[0][6]).grid(row=10,column=2)
        Label(frame4,text="Booked On:").grid(row=10,column=3)
        Label(frame4,text=res[0][7]).grid(row=10,column=4)
        Label(frame4,text="Bus Id:").grid(row=11,column=1)
        Label(frame4,text=res[0][11]).grid(row=11,column=2)
        Label(frame4,text="Boarding Point:").grid(row=11,column=3)
        Label(frame4,text=res[0][5]).grid(row=11,column=4)
        temp=res[0][9]*res[0][4]
        Label(frame4,text='Total amount Rs {} to be paid at the time of boarding the bus'.format(temp),font="arial 9 italic").grid(row=12,column=1,columnspan=10)
        
        Button(root,image=home,bg='Pale Green',command=fun).grid(row=5,column=0,columnspan=11)
home=PhotoImage(file='.\\home.png')
Button(root,text='Check Booking',font='Arial 10',command=check_book).grid(row=3,column=2,sticky='W')




























root.mainloop()

from tkinter import *
from tkinter.messagebox import *
import sqlite3
root=Tk()
con=sqlite3.Connection('Python_bus.db')
cur=con.cursor()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus=PhotoImage(file='.\\Bus_for_project.png')
frame1=Frame(root)
frame1.grid(row=1)
Label(frame1,image=bus).grid(row=1,column=1,padx=w/2.3,pady=5)
cur.execute("""select * from Booking_history where Reference_Id IN(select max(Reference_Id) from Booking_history) """)
res=cur.fetchall()
frame2=Frame(root)
frame2.grid(row=2,pady=5)
Label(frame2,text="Online Bus Booking System",font="arial 18 bold",bg="light blue",fg="red").grid(row=2,column=1)

frame3=Frame(root)
frame3.grid(row=3,pady=10)
Label(frame3,text="Bus Ticket").grid(row=3,column=1)

frame4=LabelFrame(root,relief='groove',bd=5)
frame4.grid()
Label(frame4,text="Passenger:").grid(row=4,column=1)
Label(frame4,text=res[0][1]).grid(row=4,column=2)
Label(frame4,text="Gender:").grid(row=4,column=3)
Label(frame4,text=res[0][2]).grid(row=4,column=4)
Label(frame4,text="No of seat:").grid(row=5,column=1)
Label(frame4,text=res[0][4]).grid(row=5,column=2)
Label(frame4,text="Phone:").grid(row=5,column=3)
Label(frame4,text=res[0][0]).grid(row=5,column=4)
Label(frame4,text="Age:").grid(row=6,column=1)
Label(frame4,text=res[0][3]).grid(row=6,column=2)
Label(frame4,text="Fare Rs:").grid(row=6,column=3)
Label(frame4,text=res[0][9]).grid(row=6,column=4)
Label(frame4,text="Booking Ref:").grid(row=7,column=1)
Label(frame4,text=res[0][12]).grid(row=7,column=2)
Label(frame4,text="Bus Deatil:").grid(row=7,column=3)
Label(frame4,text=res[0][8]).grid(row=7,column=4)
Label(frame4,text="Travel On:").grid(row=8,column=1)
Label(frame4,text=res[0][6]).grid(row=8,column=2)
Label(frame4,text="Booked On:").grid(row=8,column=3)
Label(frame4,text=res[0][7]).grid(row=8,column=4)
Label(frame4,text="Bus Id:").grid(row=9,column=1)
Label(frame4,text=res[0][11]).grid(row=9,column=2)
Label(frame4,text="Boarding Point:").grid(row=9,column=3)
Label(frame4,text=res[0][5]).grid(row=9,column=4)
temp=res[0][9]*res[0][4]
Label(frame4,text='Total amount Rs {} to be paid at the time of boarding the bus'.format(temp),font="arial 9 italic").grid(row=10,column=1,columnspan=10)
showinfo('status',"seat booked")


#showinfo('Success','Seat Booked...')
root.mainloop()

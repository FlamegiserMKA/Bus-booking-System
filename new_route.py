from tkinter import *
from tkinter.messagebox import*
import sqlite3
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=12,padx=w/2.5)

Label(root,text='Online Bus Booking System',font='Arial 20',fg='Red',bg='Sky Blue').grid(row=1,column=0,columnspan=12)
Label(root,text='Add Bus Route Details',font='Arial 18',fg='Green2').grid(row=2,columnspan=12,pady=20)

Label(root,text='Route ID',font='Arial 10').grid(row=3,column=2)
E1=Entry(root)
E1.grid(row=3,column=3)
Label(root,text='Station Name',font='Arial 10').grid(row=3,column=4)
E2=Entry(root)
E2.grid(row=3,column=5)
Label(root,text='Station ID',font='Arial 10').grid(row=3,column=6)
E3=Entry(root)
E3.grid(row=3,column=7)
def fun1():
    root.destroy()
    import home
def add():
    if(E1.get()==''):
        showerror('value error',"enter route ID")
    elif(E2.get()==''):
        showerror('value error',"enter station name")
    elif(E3.get()==''):
        showerror('value error',"enter station id")
    else:
        con=sqlite3.Connection("Python_bus.db")
        cur=con.cursor()
        if E1.get()!="" and E2.get()!="" and E3.get()!="" :
            cur.execute("insert into Route values('"+E1.get()+"','"+E2.get()+"','"+E3.get()+"')")
            con.commit()
            display()
            con.close()
            messagebox.showinfo("","Route details added successfully")

def display():
    Label(root,text=E1.get()+" "+E2.get()+" "+E3.get()).grid(row=3,column=8)

Button(root,text='Add Route',font='Arial 10',bg='Pale Green',command=add).grid(row=3,column=8)
Button(root,text='Delete Route',font='Arial 10',bg='Pale Green',fg='Red').grid(row=3,column=9)
home=PhotoImage(file='.\\home.png')
Button(root,image=home,bg='Pale Green',command=fun1).grid(row=4,column=8,pady=50)









root.mainloop()

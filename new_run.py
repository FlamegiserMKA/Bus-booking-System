from tkinter import *
from tkinter import messagebox
import sqlite3
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=16,padx=w/2.5)

Label(root,text='Online Bus Booking System',font='Arial 20',fg='Red',bg='Sky Blue').grid(row=1,column=0,columnspan=16)
Label(root,text='Add Bus Running Details',font='Arial 18',fg='Green2').grid(row=2,columnspan=16,pady=20)

Label(root,text='Bus ID',font='Arial 10').grid(row=3,column=4)
E1=Entry(root)
E1.grid(row=3,column=5)
Label(root,text='Running Date',font='Arial 10').grid(row=3,column=6)
E2=Entry(root)
E2.grid(row=3,column=7)
Label(root,text='Seat Available',font='Arial 10').grid(row=3,column=8)
E3=Entry(root)
E3.grid(row=3,column=9)
def fun():
    root.destroy()
    import project_home
def add():
    if(E1.get()==''):
        messagebox.showerror('valueerror',"enter bus ID")
    elif(E2.get()==''):
        messagebox.showerror('valueerror',"enter Running Date")
    elif(E3.get()==''):
        messagebox.showerror('valueerror',"enter Seat Available")
    else:
        con=sqlite3.Connection("Python_bus.db")
        cur=con.cursor()
        if E1.get()!="" and E2.get()!="" and E3.get()!="" :
            cur.execute("insert into Runs values('"+E1.get()+"','"+ E2.get()+"','"+E3.get()+"')")
            con.commit()
            displaY()
            messagebox.showinfo("","Bus Running details added successfully")
            con.close()  
def displaY():
    Label(root,text=E1.get()+" "+E2.get()+" "+E3.get()).grid(row=2,column=10)

def delete():
    if(E1.get()==''):
        messagebox.showerror('valueerror',"enter bus ID")
    elif(E2.get()==''):
        messagebox.showerror('valueerror',"enter Running Date")
    elif(E3.get()==''):
        messagebox.showerror('valueerror',"enter Seat Available")
Button(root,text='Add Run',font='Arial 10',bg='Pale Green',command=add).grid(row=3,column=10)
Button(root,text='Delete Run',font='Arial 10',bg='Pale Green',command=delete).grid(row=3,column=11)

home=PhotoImage(file='.\\home.png')
Button(root,image=home,bg='Pale Green',command=fun).grid(row=4,column=10,pady=50)






root.mainloop()

from tkinter import *
from tkinter import messagebox
import sqlite3
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=14,padx=w/2.5)

Label(root,text='Online Bus Booking System',font='Arial 20',fg='Red',bg='Sky Blue').grid(row=1,column=0,columnspan=14)
Label(root,text='Add Bus Operator Details',font='Arial 18',fg='Green2').grid(row=2,columnspan=14,pady=20)

Label(root,text='Operator_Id',font='Arial 10').grid(row=3,column=1)
Op=Entry(root)
Op.grid(row=3,column=2)
Label(root,text='Name',font='Arial 10').grid(row=3,column=3)
E1=Entry(root)
E1.grid(row=3,column=4)
Label(root,text='Address',font='Arial 10').grid(row=3,column=5)
E2=Entry(root)
E2.grid(row=3,column=6)
Label(root,text='Phone',font='Arial 10').grid(row=3,column=7)
E3=Entry(root)
E3.grid(row=3,column=8)
Label(root,text='Email',font='Arial 10').grid(row=3,column=9)
E4=Entry(root)
E4.grid(row=3,column=10)
def fun():
    root.destroy()
    import home
def add():
    if(E1.get()==''):
        showerror('valueerror',"enter name")
    elif(Op.get()==""):
        showerror('valueerror',"enter Operator_id")
    elif(E2.get()==''):
        showerror('valueerror',"enter address")
    elif(E3.get()==''):
        showerror('valueerror',"enter phone")
    elif(E4.get()==''):
        showerror('valueerror',"enter email")
    else:
        con=sqlite3.Connection("Python_bus.db")
        cur=con.cursor()
        if Op.get()!="" and E1.get()!="" and E2.get()!="" and E3.get()!="" and E4.get()!="" :
            cur.execute("insert into Operator values('"+Op.get()+"','"+E1.get()+"','"+E2.get()+"','"+E3.get()+"','"+E4.get()+"')")
            con.commit()
            display()
            con.close()
def display():
    Label(root,text=Op.get()+" "+E1.get()+" "+E2.get()+" "+E3.get()+" "+E4.get()).grid(row=3,column=11)

def edit():
    if(E1.get()==''):
        showerror('valueerror',"enter name")
    elif(Op.get()==""):
        showerror('valueerror',"enter Operator_id")
    elif(E2.get()==''):
        showerror('valueerror',"enter address")
    elif(E3.get()==''):
        showerror('valueerror',"enter phone")
    elif(E4.get()==''):
        showerror('valueerror',"enter email") 
    else:
        con=sqlite3.Connection("Python_bus.db")
        cur=con.cursor()
        if Op.get()!="" and E1.get()!="" and E2.get()!="" and E3.get()!="" and E4.get()!="":
            cur.execute("update Operator values('"+Op.get()+"','"+E1.get()+"','"+E2.get()+"','"+E3.get()+"','"+E4.get()+"')")
            con.commit()
            con.close()
            messagebox.showinfo("","Bus operator updated successfully")   

Button(root,text='Add',font='Arial 10',bg='Pale Green',command=add).grid(row=3,column=11)
Button(root,text='Edit',font='Arial 10',bg='Pale Green',command=edit).grid(row=3,column=12)

home=PhotoImage(file='.\\home.png')
Button(root,image=home,bg='Pale Green',command=fun).grid(row=4,column=11,pady=50)











root.mainloop()

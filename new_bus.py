from tkinter import *
from tkinter.messagebox import*
import sqlite3
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=16,padx=w/2.5)

Label(root,text='Online Bus Booking System',font='Arial 20',fg='Red',bg='Sky Blue').grid(row=1,column=0,columnspan=16)
Label(root,text='Add Bus Details',font='Arial 18',fg='Green2').grid(row=2,columnspan=16,pady=20)

Label(root,text='Bus ID',font='Arial 10').grid(row=3,column=2)
E1=Entry(root)
E1.grid(row=3,column=3)
Label(root,text='Bus Type',font='Arial 10').grid(row=3,column=4)
a=StringVar()
a.set('Bus Type')
OptionMenu(root,a,'AC 2X2','AC 3X2','Non AC 2X2','Non AC 3X2','AC-Sleeper 2X1','Non-AC Sleeper 2X1').grid(row=3,column=5)
Label(root,text='Capacity',font='Arial 10').grid(row=3,column=6)
E2=Entry(root)
E2.grid(row=3,column=7)
Label(root,text='Fare Rs',font='Arial 10').grid(row=3,column=8)
E3=Entry(root)
E3.grid(row=3,column=9)
Label(root,text='Operator ID',font='Arial 10').grid(row=3,column=10)
E4=Entry(root)
E4.grid(row=3,column=11)
Label(root,text='Route ID',font='Arial 10').grid(row=3,column=12)
E5=Entry(root)
E5.grid(row=3,column=13)
def fun():
    root.destroy()
    import project_home
def add():
    if(E1.get()==''):
        showerror('valueerror',"enter bus ID")
    elif(a.get()=='Bus Type'):
        showerror('valueerror',"enter bus type")
    elif(E2.get()==''):
        showerror('valueerror',"enter bus capacity")
    elif(E3.get()==''):
        showerror('valueerror',"enter bus fare")
    elif(E4.get()==''):
        showerror('valueerror',"enter operator ID")
    elif(E5.get()==''):
        showerror('valueerror',"enter Route ID.")
    else:
        con=sqlite3.Connection("Python_bus.db")
        cur=con.cursor()
        cur.execute("insert into Bus values('"+E1.get()+"','"+a.get()+"','"+E2.get()+"','"+E3.get()+"','"+E4.get()+"','"+E5.get()+"')")
        con.commit()
        display()
        con.close()
        showinfo("","Bus details added successfully")

def display():
    Label(root,text=E1.get()+" "+a.get()+" "+E2.get()+" "+E3.get()+" "+E4.get()+" "+E5.get()).grid(row=4,column=7)

def edit():
    if(E1.get()==''):
        showerror('valueerror',"enter bus ID")
    elif(a.get()=='Bus Type'):
        showerror('valueerror',"enter bus type")
    elif(E2.get()==''):
        showerror('valueerror',"enter bus capacity")
    elif(E3.get()==''):
        showerror('valueerror',"enter bus fare")
    elif(E4.get()==''):
        showerror('valueerror',"enter operator ID")
    elif(E5.get()==''):
        showerror('valueerror',"enter Route ID.")
    else:
        con=sqlite3.Connection("Python_bus.db")
        cur=con.cursor()
        if E1.get()=="" and a.get()=="" and E2.get()=="" and E3.get()=="" and E4.get()=="" and E5.get()=="":
            cur.execute("insert into Bus values('"+E1.get()+"','"+a.get()+"','"+E2.get()+"','"+E3.get()+"','"+E4.get()+"','"+E5.get()+"')")
            con.commit()
            con.close()
            messagebox.showinfo("","Bus details added successfully")  

Button(root,text='Add Bus',font='Arial 10',bg='Pale Green',command=add).grid(row=6,column=7,pady=40)
Button(root,text='Edit Bus',font='Arial 10',bg='Pale Green',command=edit).grid(row=6,column=8)
home=PhotoImage(file='.\\home.png')
  
Button(root,image=home,bg='Pale Green',command=fun).grid(row=6,column=9)






root.mainloop()

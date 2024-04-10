from tkinter import *
from tkinter.messagebox import*
import sqlite3
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
conn=sqlite3.Connection('Python_bus.db')
def show_bus():
   
    if(X1.get()==''):
        showerror('value error',"Enter destination")
    elif(X2.get()==''):
        showerror('value error',"enter starting point")
    elif(X3.get()==''):
        showerror('value error',"Enter journey date")
    else:
        Label(root,text='Select Bus',font='Arial 10',fg='Forest Green').grid(row=7,column=1)
        Label(root,text='Operator',font='Arial 10',fg='Forest Green').grid(row=7,column=2)
        Label(root,text='Bus Type',font='Arial 10',fg='Forest Green').grid(row=7,column=3)
        Label(root,text='Available/Capacity',font='Arial 10',fg='Forest Green').grid(row=7,column=4)
        Label(root,text='Fare',font='Arial 10',fg='Forest Green').grid(row=7,column=5)
        cur=conn.cursor()
        cur.execute("""select op.Name,b.type,r.Seat_Available,b.fare,b.Bus_Id from Operator as op, Bus as b,runs as r, route as f,route as t
        where b.op_id=op.op_id and b.bus_id=r.bus_id and f.Route_id=b.Route_id and f.sname="{}" and t.sname="{}" and f.Route_id = t.route_id
        and F.s_id<T.s_id and r.date="{}" """.format(X2.get(),X1.get(),X3.get()))
        res=cur.fetchall()
        print(res)
        cur.execute(' select SUM(no_of_seats) from Booking_history where dot="{}" '.format(X3.get()))
        r1=cur.fetchall()
        temp=res[0][2]- r1[0][0]
        Label(root,text=res[0][0]).grid(row=8,column=2)
        Label(root,text=res[0][1]).grid(row=8,column=3)
        Label(root,text=str(temp)+'/'+str(res[0][2])).grid(row=8,column=4)
        Label(root,text=res[0][3]).grid(row=8,column=5)
        Radiobutton(root,text='Bus 1',font='Arial 8',fg='Black',variable=bus,value=1).grid(row=8,column=1)
        
        conn.commit()

        def proceed_book():
            if(bus.get()==0):
                showerror('value missing',"please select bus")
                return
            Label(root,text='Fill Passenger Details to Book the Bus Ticket',font='Arial 18',fg='Red',bg='Sky Blue').grid(row=9,columnspan=11,pady=5)
            Label(root,text='Name',font='Arial 10').grid(row=11,column=0)
            E1=Entry(root)
            E1.grid(row=11,column=1)
            Label(root,text='Gender',font='Arial 10',width=5).grid(row=11,column=2)
            c=StringVar()
            c.set('Select')
            OptionMenu(root,c,'Male','Female','Others').grid(row=11,column=3)
            Label(root,text='No. of Seats',font='Arial 10',width=8).grid(row=11,column=4)
            E2=Entry(root,width=5)
            E2.grid(row=11,column=5)
            Label(root,text='Mobile  No.',font='Arial 10',width=10).grid(row=11,column=6)
            E3=Entry(root)
            E3.grid(row=11,column=7,sticky='W')
            Label(root,text='Age',font='Arial 10',width=5).grid(row=11,column=8)
            E4=Entry(root,width=5)
            E4.grid(row=11,column=9)
            def warnings2():
                if(E1.get()==''):
                    showerror('value error',"name can't be empty")
                elif(c.get()=='Select'):
                    showerror('value error',"select gender")
                elif(E2.get()==''):
                    showerror('value error',"fill number of seats")
                elif(int(E2.get())>res[0][2]- r1[0][0]):
                    showerror('value error',"Exceeding availability")
                elif(E3.get()==''):
                    showerror('value error',"Enter Mobile No.")
                elif(len(str(E3.get()))!=10):
                    showerror('value error',"Enter Valid Mobile No.")
                elif(E4.get()==''):
                    showerror('value error',"Enter Your Age")
                elif(int(E4.get())>99 or int(E4.get())<12):
                    showerror('value error',"Enter Valid Age")
                else:


                    conn=sqlite3.Connection('python_bus.db')
                    cur=conn.cursor()
                    
                    cur.execute(""" insert into booking_history(mobile,pname, gender,age,no_of_seats,bfrom,dot,dob,bname,fare,bto,Bus_Id)
                    values({},"{}","{}",{},{},
                    "{}","{}",current_date,"{}","{}","{}","{}")""".format(int(E3.get()),E1.get(),c.get(),int(E4.get()),int(E2.get()),X2.get(),X3.get(),res[0][0],res[0][3],X1.get(),res[0][4]))
                    cur.execute('select* from booking_history')
                    res1=cur.fetchall()
                    print(res1)
                    conn.commit()
                    cur.execute("""select fare,no_of_seats from Booking_history where Reference_Id IN(select max(Reference_Id) from Booking_history) """)
                    res2=cur.fetchall()
                    temp=res2[0][0]*res2[0][1]
                    b=askyesno('seat booking',"Do You Wish to proceed with payment of Rs.{}".format(temp))
                    if(b==1):
                        root.destroy()
                        import ticket_detail
                    else:
                        show_bus()
            Button(root,text='Book Seat',command=warnings2,font='Arial 10',bg='Pale Green').grid(row=11,column=10)        
        Button(root,text='Proceed to Book',font='Arial 10',bg='Pale Green',command=proceed_book).grid(row=8,column=6,pady=10)       
            
def see():
    root.destroy()
    import home


bus=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=bus).grid(row=0,column=0,columnspan=11,padx=w/2.5)
Label(root,text='Online Bus Booking System',font='Arial 20',fg='Red',bg='Sky Blue').grid(row=1,column=0,columnspan=11,pady=2)
Label(root,text='Enter Journey Details',font='Arial 15',fg='Green3',bg='Pale Green').grid(row=3,column=0,columnspan=11,pady=2)
Label(root,text='To',font='Arial 10').grid(row=5,column=1)
X1=Entry(root)
X1.grid(row=5,column=2)
Label(root,text='From',font='Arial 10').grid(row=5,column=3)
X2=Entry(root)
X2.grid(row=5,column=4)
Label(root,text='Journey Date',font='Arial 10').grid(row=5,column=5)
X3=Entry(root)
X3.grid(row=5,column=6) 
Button(root,text='Show Bus',command=show_bus,font='Arial 10',bg='Sea Green').grid(row=5,column=7)
home=PhotoImage(file='.\\home.png')
bus=IntVar()
Button(root,image=home,bg='Green',command=see).grid(row=5,column=8,pady=2)


   

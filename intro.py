from tkinter import*
root=Tk()
root.config(background='light grey')
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img = PhotoImage(file='.\\Bus_for_project.png')
bus=Label(root,image=img).grid(row=0,column=0,columnspan=100,padx=w//3)
name=Label(root,text='Online Bus Booking System',font='Ariel 30',fg='Red',bg='sky blue').grid(row=1,column=0,padx=w//3)
name=Label(root,text='Name: Madhur Krishna Agarwal',fg='Blue',bg='light grey',font='Ariel 16').grid(row=2,column=0,padx=w//3,pady=80)
name=Label(root,text='Name: Er: 211B170',fg='Blue',bg='light grey',font='Ariel 16').grid(row=3,column=0,padx=w//3,pady=20)
name=Label(root,text='Mobile: 9170579983',fg='Blue',bg='light grey',font='Ariel 16').grid(row=4,column=0,padx=w//3,pady=80)
name=Label(root,text='Submitted To: Dr. Mahesh Kumar',font='Ariel 20',fg='Red',bg='sky blue').grid(row=5,column=0,padx=w//3)
name=Label(root,text='Project Based Learning',fg='Red',bg='light grey',font='Ariel 16').grid(row=6,column=0,padx=w//3)
def close():
    root.destroy()
    import home
root.after(5000,close)

    cur=con.cursor()
        if E1.get()=="" and a.get()=="" and E2.get()=="" and E3.get()=="" and E4.get()=="" and E5.get()=="":
            cur.execute("insert into Bus values('"+E1.get()+"','"+a.get()+"','"+E2.get()+"','"+E3.get()+"','"+E4.get()+"','"+E5.get()+"')")
            
            con.commit()
            con.close()
            messagebox.showinfo("","Bus details added successfully")  
import sqlite3
con = sqlite3.connect('Python_bus.db')
cur=con.cursor()
cur.execute("""create table Operator(Op_Id int PRIMARY KEY, Name varchar(20), Address varchar(20), Phone numeric(12), Email varchar(50));""")
cur.execute("""create table Route(Route_Id int(10), S_Id int(10), Sname varchar(10), PRIMARY KEY(Route_Id,S_Id));""")
cur.execute("""create table Bus(Bus_Id int PRIMARY KEY, Type varchar(10),Capacity int(5),Fare numeric(10),Op_Id int(10),Route_Id int(10),
CONSTRAINT fk_route FOREIGN KEY(Route_Id) REFERENCES Route(Route_Id),CONSTRAINT fk_opID FOREIGN KEY(Op_Id) REFERENCES operator(op_Id));""")
cur.execute("""create table Runs(Bus_Id int(10),Date varchar(10),
Seat_Available int(5),CONSTRAINT fk_bus FOREIGN KEY(bus_Id) REFERENCES BUS(Bus_Id));""")
cur.execute("""create table Booking_history(mobile numeric(10),pname varchar(20),
gender varchar(10),age int(3), no_of_seats int(10),bfrom varchar(20),
dot varchar(12),dob varchar(12),bname varchar(20),fare numeric(10),bto varchar(20),
Bus_Id int,
Reference_Id INTEGER primary key AUTOINCREMENT ,CONSTRAINT fk_bus1 FOREIGN KEY(Bus_Id) REFERENCES BUS(Bus_Id));""")

cur.execute('insert into Operator values(01,"Samay Shatabdi","Delhi",8871003559,"samayshtbd@gmail.com");');

cur.execute('insert into Route values(31,1,"Lucknow");')
cur.execute('insert into Route values(31,2,"Kanpur");')
cur.execute('insert into Route values(31,3,"Mathura")')
cur.execute('insert into Route values(31,4,"Agra");')
cur.execute('insert into Route values(31,5,"New Delhi");')

cur.execute('insert into Bus values(21,"AC-Sleeper 2X1",50,1000,01,31)')

cur.execute('insert into Runs values(21,"18/12/22",50)')


res=cur.fetchall();
print("Completed")
con.commit()
con.close()
   

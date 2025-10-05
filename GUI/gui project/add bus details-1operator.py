from tkinter import *
from tkinter.messagebox import *
import sqlite3
con=sqlite3.Connection('MyDB')
cur=con.cursor()
#print('Database Connected')
cur.execute('create table if not exists operator(opid int,name varchar(20),address varchar(30),phone int(10),email varchar(20))')
#print('table created')
#cur.execute('Show tables')
#for table_name in cur:
#    print(table_name)
root=Tk()
root.geometry('900x800')
Label(root,text=" ").grid(row=0,column=0)#.pack()

img=PhotoImage(file='python_bus.png')
Label(root,image=img).grid(row=0,column=2,columnspan=8)#.pack()

Label(root,text="Online Bus Booking System",font='arial 30 bold ',bg='bisque').grid(row=1,column=2,columnspan=8)#.pack()#.grid(row=0,column=0,columnspan=3)
Label(root,text=" ").grid(row=2,column=0)#.pack()
Label(root,text=" ").grid(row=3,column=0)#.pack()
Label(root,text="Add Bus Operator Details",bg='grey88',fg='green',padx=10).grid(row=4,column=2,columnspan=7)#.pack()
Label(root,text=" ").grid(row=5,column=0)#.pack()


Label(root,text='Operator ID').grid(row=13,column=0)
o=Entry(root)
o.grid(row=13,column=1)

Label(root,text='Name').grid(row=13,column=2)
n=Entry(root)
n.grid(row=13,column=4)

Label(root,text='Address').grid(row=13,column=5)
ad=Entry(root)
ad.grid(row=13,column=6)

Label(root,text='Phone').grid(row=13,column=7)
ph=Entry(root)
ph.grid(row=13,column=8)

Label(root,text='Email').grid(row=13,column=9)
em=Entry(root)
em.grid(row=13,column=10)

def enter_detail():
    op_id=o.get()
    name=n.get()
    addr=ad.get()
    phn=ph.get()
    email=em.get()
    cur.execute("insert into operator(opid,name,address,phone,email) values(?,?,?,?,?)",(op_id,name,addr,phn,email))
    showinfo("Data","Operator Added")
    print('Operator Details Added Successfully')
    #print(*cur.execute('select * from operator'))
    con.commit()

def show():
    print(*cur.execute('select * from operator'))
    Label(root,text=" ").grid(row=16,column=0)
    Label(root,text=cur.execute('select * from operator')).grid(row = 17,column=3,columnspan=8)

ed=Entry(root)
def delete():
    cur.execute('delete from operator where opid =?',(ed.get(),))
    showinfo("delete","Record Deleted")
    con.commit()

def update():
    op_id=o.get()
    name=n.get()
    addr=ad.get()
    phn=ph.get()
    email=em.get()
    cur.execute("update operator set name=?,address=?,phone=?,email=? where opid=?",(name,addr,phn,email,op_id))
    showinfo("Modify","Record Modified")
    print(*cur.execute('select * from operator'))
    con.commit()

def edit():
    
    ed.grid(row=15,column=9,columnspan=10)
    Label(root,text='Enter OperatorID:').grid(row=15,column=8)
    Button(root,text='Delete',bg='green',command=delete).grid(row=16,column=9,columnspan=10)

    Label(root,text=" ").grid(row=17,column=0)
    #Label(root,text=" ").grid(row=18,column=0)
    
    Label(root,text='Operator ID').grid(row=19,column=0)
    o=Entry(root)
    o.grid(row=19,column=1)

    Label(root,text='Name').grid(row=19,column=2)
    n=Entry(root)
    n.grid(row=19,column=4)

    Label(root,text='Address').grid(row=19,column=5)
    ad=Entry(root)
    ad.grid(row=19,column=6)

    Label(root,text='Phone').grid(row=19,column=7)
    ph=Entry(root)
    ph.grid(row=19,column=8)

    Label(root,text='Email').grid(row=19,column=9)
    em=Entry(root)
    em.grid(row=19,column=10)
    
    Label(root,text=" ").grid(row=20,column=0)
    Button(root,text='Update',bg='green',command=update).grid(row=21,column=6)
 
Label(root,text=" ").grid(row=14,column=0)
Button(root,text='Add',command=enter_detail,bg='green').grid(row=15,column=5)
Button(root,text='Show',bg='green',command=show).grid(row=15,column=6)
Button(root,text='Edit',bg='green',command=edit).grid(row=15,column=7)

con.commit()
cur.fetchall()
root.mainloop()

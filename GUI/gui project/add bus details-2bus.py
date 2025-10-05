from tkinter import *
from tkinter.messagebox import *
import sqlite3
con=sqlite3.Connection('ByDB')
cur = con.cursor()
cur.execute('create table if not exists bus(busid int(4), bustype varchar(30),address varchar(40),phone int(10),email varchar(30))')
#cur.execute('insert into bus values(1234,"AC 2x2","GUNA",1234567890,"hello@gg.com")')



root=Tk()
root.geometry('850x800')
Label(root,text=" ").grid(row=0,column=0)#.pack()

img=PhotoImage(file='python_bus.png')
Label(root,image=img).grid(row=0,column=2,columnspan=8)#.pack()

Label(root,text="Online Bus Booking System",font='arial 30 bold ',bg='bisque').grid(row=1,column=2,columnspan=8)#.pack()#.grid(row=0,column=0,columnspan=3)
Label(root,text=" ").grid(row=2,column=0)#.pack()
Label(root,text=" ").grid(row=3,column=0)#.pack()
Label(root,text="Add Bus  Details",bg='grey88',fg='green',padx=10).grid(row=4,column=2,columnspan=7)#.pack()
Label(root,text=" ").grid(row=5,column=0)#.pack()

Label(root,text='Bus ID').grid(row=13,column=0)
o=Entry(root)
o.grid(row=13,column=1)
Label(root,text='Bus Type').grid(row=13,column=3)

def select(event):
    clicked.set(event)
    #label.config(text=clicked.get())
clicked=StringVar()    
options=["AC 2x2","AC 2x1 Sleeper","Non AC 2x2","Non AC 2x1 Sleeper"]

drop=OptionMenu(root,clicked,*options)

drop.grid(row=13,column=4)
#clicked=StringVar()
#Button(root,text='select',command=show).grid(row=13,column=4)

Label(root,text='Address').grid(row=13,column=5)
ad=Entry(root)
ad.grid(row=13,column=6)

Label(root,text='Phone').grid(row=13,column=7)
ph=Entry(root)
ph.grid(row=13,column=8)

Label(root,text='Email').grid(row=13,column=9)
em=Entry(root)
em.grid(row=13,column=10)

Label(root,text=" ").grid(row=14,column=0)

def enter_detail():
    b_id=o.get()
    b_type=clicked.get()
    addr=ad.get()
    phn=ph.get()
    email=em.get()
    cur.execute("insert into bus(busid,bustype,address,phone,email) values(?,?,?,?,?)",(b_id,b_type,addr,phn,email))
    print('Bus Details Added Successfully')
    showinfo("Data","Bus Added")
    con.commit()

def show():
    print(*cur.execute('select * from bus'))
    Label(root,text=" ").grid(row=16,column=0)
    Label(root,text=cur.execute('select * from bus')).grid(row = 17,column=3,columnspan=8)
    showinfo("Data","Data Fetched Successfully")

ed=Entry(root)
def delete():
    cur.execute('delete from bus where busid =?',(ed.get(),))
    showinfo("delete","Record Deleted")
    con.commit()

def update():
    b_id=o.get()
    b_type=clicked.get()
    addr=ad.get()
    phn=ph.get()
    email=em.get()
    cur.execute("update bus set bustype=?,address=?,phone=?,email=? where busid=?",(b_type,addr,phn,email,b_id))
    showinfo("Modify","Record Modified")
    print(*cur.execute('select * from bus'))
    con.commit()
    
def edit():
    
    ed.grid(row=15,column=8,columnspan=10)
    Label(root,text='Enter BusID:',padx=5).grid(row=15,column=5,columnspan=8)
    Label(root,text='To Delete Record').grid(row=16,column=5,columnspan=8)
    Button(root,text='delete',bg='green',command=delete).grid(row=15,column=10)

    Label(root,text=" ").grid(row=17,column=0)
    #Label(root,text=" ").grid(row=18,column=0)
    
    Label(root,text='Bus ID').grid(row=19,column=0)
    o=Entry(root)
    o.grid(row=19,column=1)
    Label(root,text='Bus Type').grid(row=19,column=3)

    #def select(event):
    #    clicked.set(event)
        #label.config(text=clicked.get())
    clicked=StringVar()    
    options=["AC 2x2","AC 2x1 Sleeper","Non AC 2x2","Non AC 2x1 Sleeper"]

    drop=OptionMenu(root,clicked,*options)

    drop.grid(row=19,column=4)
    #clicked=StringVar()
    #Button(root,text='select',command=show).grid(row=13,column=4)

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

Button(root,text='Add',bg='green',command=enter_detail).grid(row=15,column=5)

Button(root,text='Show ',bg='green',command=show).grid(row=15,column=6)

Button(root,text='Edit',bg='green',command=edit).grid(row=15,column=7)


#cur.execute('select * from bus')
con.commit()
print(cur.fetchall())

root.mainloop()
